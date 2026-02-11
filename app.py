from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for frontend requests

# Configuration
# Configuration
# Use /tmp for serverless environments (Vercel), 'uploads' for local
if os.environ.get('VERCEL') or not os.path.exists('uploads') and not os.access('.', os.W_OK):
    UPLOAD_FOLDER = '/tmp'
else:
    UPLOAD_FOLDER = 'uploads'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/send-emails', methods=['POST'])
def send_emails():
    try:
        # Get form data
        sender_email = request.form.get('senderEmail')
        sender_password = request.form.get('senderPassword')
        recipients = request.form.get('recipients')  # JSON string
        subject = request.form.get('subject')
        body = request.form.get('body')
        
        # Validate inputs
        if not all([sender_email, sender_password, recipients, subject, body]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Parse recipients
        import json
        recipients_list = json.loads(recipients)
        
        if not recipients_list or len(recipients_list) == 0:
            return jsonify({'error': 'No recipients provided'}), 400
        
        # Handle file upload
        resume_file = None
        resume_path = None
        
        if 'resume' in request.files:
            resume_file = request.files['resume']
            
            if resume_file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            
            if not allowed_file(resume_file.filename):
                return jsonify({'error': 'Invalid file type. Only PDF, DOC, DOCX allowed'}), 400
            
            # Save the file temporarily
            filename = secure_filename(resume_file.filename)
            resume_path = os.path.join(UPLOAD_FOLDER, filename)
            resume_file.save(resume_path)
        
        # Setup SMTP server
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
        except smtplib.SMTPAuthenticationError:
            if resume_path and os.path.exists(resume_path):
                os.remove(resume_path)
            return jsonify({'error': 'Authentication failed. Check your email and app password'}), 401
        except Exception as e:
            if resume_path and os.path.exists(resume_path):
                os.remove(resume_path)
            return jsonify({'error': f'SMTP connection failed: {str(e)}'}), 500
        
        # Send emails
        sent_count = 0
        failed_recipients = []
        
        for recipient in recipients_list:
            try:
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = recipient
                msg["Subject"] = subject
                
                # Attach body text
                msg.attach(MIMEText(body, "plain"))
                
                # Attach resume if provided
                if resume_path and os.path.exists(resume_path):
                    with open(resume_path, "rb") as f:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            "Content-Disposition",
                            f"attachment; filename={os.path.basename(resume_path)}"
                        )
                        msg.attach(part)
                
                # Send email
                server.sendmail(sender_email, recipient, msg.as_string())
                sent_count += 1
                print(f"Sent application to {recipient}")
                
            except Exception as e:
                print(f"Failed to send to {recipient}: {str(e)}")
                failed_recipients.append(recipient)
        
        # Cleanup
        server.quit()
        
        # Delete the uploaded file after sending
        if resume_path and os.path.exists(resume_path):
            os.remove(resume_path)
        
        # Return response
        response_data = {
            'sent': sent_count,
            'total': len(recipients_list),
            'message': f'Successfully sent {sent_count} out of {len(recipients_list)} emails'
        }
        
        if failed_recipients:
            response_data['failed'] = failed_recipients
            response_data['message'] += f'. Failed: {", ".join(failed_recipients)}'
        
        return jsonify(response_data), 200
        
    except Exception as e:
        # Cleanup on error
        if resume_path and os.path.exists(resume_path):
            os.remove(resume_path)
        
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
