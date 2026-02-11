# Job Application Sender - Deployment Guide

## 📋 Overview
This application allows you to send job applications to multiple recruiters through a web interface. The application has two parts:
- **Frontend**: HTML interface where you enter emails and compose your application
- **Backend**: Python Flask API that handles sending emails via SMTP

## 🚀 Deployment Options

### **Option 1: Deploy on Render (Recommended - FREE)**

Render is perfect for this application because it supports both frontend and backend in one platform.

#### Steps:

1. **Create a GitHub Repository**
   - Go to github.com and create a new repository
   - Upload these files: `index.html`, `app.py`, `requirements.txt`, `Procfile`

2. **Sign up on Render**
   - Go to https://render.com
   - Sign up with your GitHub account

3. **Deploy the Backend API**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Fill in the details:
     - **Name**: job-application-backend
     - **Environment**: Python
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Copy the URL (e.g., `https://job-application-backend.onrender.com`)

4. **Deploy the Frontend**
   - Click "New +" → "Static Site"
   - Connect your GitHub repository
   - Fill in the details:
     - **Name**: job-application-frontend
     - **Publish Directory**: `.` (current directory)
   - Click "Create Static Site"

5. **Update Frontend to Connect to Backend**
   - In `index.html`, find this line (around line 385):
     ```javascript
     const response = await fetch('/api/send-emails', {
     ```
   - Replace with your backend URL:
     ```javascript
     const response = await fetch('https://your-backend-url.onrender.com/api/send-emails', {
     ```
   - Push the changes to GitHub
   - Render will auto-deploy

6. **Access Your App**
   - Open your frontend URL (e.g., `https://job-application-frontend.onrender.com`)
   - Start sending applications! 🎉

---

### **Option 2: Deploy on Railway (Also FREE)**

Railway is another excellent option with a generous free tier.

#### Steps:

1. **Create GitHub Repository** (same as Option 1)

2. **Sign up on Railway**
   - Go to https://railway.app
   - Sign up with GitHub

3. **Deploy Backend**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway auto-detects Python and deploys
   - Go to Settings → Generate Domain
   - Copy the URL

4. **Update Frontend**
   - Update the fetch URL in `index.html` with your Railway backend URL
   - Push to GitHub

5. **Deploy Frontend**
   - Create another Railway project for the frontend
   - Deploy as static site

---

### **Option 3: Local Deployment (For Testing)**

If you want to test locally before deploying:

#### Steps:

1. **Install Python** (if not already installed)
   - Download from python.org
   - Make sure Python 3.8+ is installed

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Backend**
   ```bash
   python app.py
   ```
   Backend will run on http://localhost:5000

4. **Open Frontend**
   - Double-click `index.html` to open in browser
   - Or use Python's built-in server:
     ```bash
     python -m http.server 8000
     ```
   - Open http://localhost:8000

5. **Update Frontend URL**
   - In `index.html`, the fetch URL should be:
     ```javascript
     const response = await fetch('http://localhost:5000/api/send-emails', {
     ```

---

## 🔐 Security Setup: Gmail App Password

**IMPORTANT**: Never use your regular Gmail password. Use an App Password instead.

### Steps to Generate App Password:

1. Go to your Google Account: https://myaccount.google.com
2. Click "Security" in the left sidebar
3. Enable "2-Step Verification" if not already enabled
4. Go back to Security → "2-Step Verification"
5. Scroll down to "App passwords"
6. Click "App passwords"
7. Select "Mail" and your device
8. Click "Generate"
9. Copy the 16-character password
10. Use this password in the application

---

## 📝 How to Use the Application

1. **Open the deployed website**

2. **Fill in your details**:
   - Your Gmail address
   - App password (16 characters, no spaces)
   - Add recipient emails one by one
   - Edit subject and body as needed
   - Upload your resume (PDF/DOCX)

3. **Click "Send Applications"**

4. **Wait for confirmation**

---

## 🎯 Pre-loaded Features

The application comes with:
- ✅ Professional email template for Power BI Developer role
- ✅ Your contact details pre-filled
- ✅ Sample recipient list (you can change it)
- ✅ Clean, modern interface
- ✅ Real-time status updates
- ✅ Support for PDF and DOCX resumes

---

## 🐛 Troubleshooting

### "Authentication failed" error
- Make sure you're using App Password, not regular password
- Check that 2-Step Verification is enabled
- Regenerate App Password if needed

### Emails not sending
- Check your internet connection
- Verify Gmail account is active
- Make sure recipient emails are valid
- Check Gmail's sending limits (500 emails/day)

### Backend not responding
- Check if backend service is running on Render/Railway
- Verify the backend URL in frontend code
- Check backend logs for errors

### File upload issues
- Make sure file is PDF or DOCX
- Check file size is under 10MB
- Verify file is not corrupted

---

## 📊 Gmail Sending Limits

- **Free Gmail**: 500 emails per day
- **Google Workspace**: 2,000 emails per day
- Add delays between sends if sending many emails

---

## 🔄 Updating Your Application

### To update recipient list or email content:
1. Open your deployed website
2. Make changes directly in the interface
3. No code changes needed!

### To update code:
1. Edit files locally
2. Push to GitHub
3. Render/Railway auto-deploys changes

---

## 💡 Tips for Success

1. **Test First**: Send to your own email first
2. **Personalize**: Customize the email body for each role
3. **Professional**: Keep emails concise and professional
4. **Follow Up**: Track which companies you've applied to
5. **Timing**: Apply during business hours for better visibility

---

## 📞 Support

If you face any issues:
1. Check the troubleshooting section
2. Review backend logs in Render/Railway
3. Test locally first to isolate issues
4. Ensure all credentials are correct

---

## 🎉 You're All Set!

Your job application system is now live and ready to use. Good luck with your job search! 🚀

---

## 📄 File Structure

```
job-application-sender/
├── index.html          # Frontend interface
├── app.py              # Backend Flask API
├── requirements.txt    # Python dependencies
├── Procfile           # Deployment config
└── README.md          # This guide
```

---

## 🌟 Features

- ✨ Modern, responsive UI
- 🔒 Secure credential handling
- 📎 Resume attachment support
- 📧 Multiple recipient support
- ✅ Real-time sending status
- 🎨 Beautiful gradient design
- 📱 Mobile-friendly interface

---

Happy Job Hunting! 💼✨
