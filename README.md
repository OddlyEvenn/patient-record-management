# 🏥 Patient Record Management System

A modular, secure, and user-friendly Python application for managing patient records using a Tkinter-based GUI and Google Sheets as a cloud database. Includes email confirmation for patient registration, with a clean interface and strict authentication.

---

## ✨ Features

- ✅ Add, Edit, Delete, and Display patient records
- ✅ Automatically sends confirmation emails on registration
- ✅ Stores patient data securely in Google Sheets
- ✅ GUI built with `tkinter` and `ttk` for a modern layout
- ✅ OAuth 2.0 authentication for Google API
- ✅ Total Revenue Summary and CSV Export
- ✅ Modular code structure (one file per function)
- ✅ Secure credential handling using `.env`

---

## 📂 Folder Structure

patient-record-management/
│
├── main.py # Main entry point
├── gui.py # Frontend using Tkinter
│
├── modules/ # All backend logic modules
│ ├── add_patient.py
│ ├── edit_patient.py
│ ├── delete_patient.py
│ ├── display_patient.py
│ ├── clear_fields.py
│ ├── email_confirmation.py
│ ├── google_sheets.py
│ ├── auth.py
│ ├── utils.py
│ ├── report_summary.py
│ ├── export_data.py
│
├── config/
│ └── creds.json # 🔐 Google Service Account Key (ignored via .gitignore)
│ └── creds_template.json # 🔑 Template for others to configure
│
├── assets/
│ └── logo.png 
│
├── .env # 🔐 Email credentials (ignored)
├── .env_template # 📄 Template for environment variables
├── .gitignore # Files to exclude from version control
└── README.md

---

## 🔧 Setup Instructions

### ✅ 1. Clone the Repo

```bash
git clone https://github.com/yourusername/patient-record-management.git
cd patient-record-management
```

### ✅ 2. Install Dependencies

```bash
pip install gspread oauth2client pandas python-dotenv
```

### ✅ 3. Setup Google Sheets API

1)Go to Google Cloud Console
2)Create a project → Enable Google Sheets API & Drive API
3)Create Service Account → Generate JSON Key
4)Download and place as creds.json
5)Rename creds_template.json → creds.json

### ✅ 4. Share the Google Sheet

1)Create a Google Sheet named: patient_records

2)First row headers as follows:
Patient Id | Name | Age | Gender | Diagnosis | Medical History | Current Treatment | Date of registration | Fees | Email-id

3)Share it with your service account email (found in creds.json) and give Editor access

### ✅ 5. Configure Email Settings

1)Create a .env file:
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password

2)Enable 2FA in your Gmail and create an App Password

### ✅ 6. Run the App

```bash
python main.py
```
---
## 🔐 Security

-Credentials and secrets are hidden via .gitignore
-Email password stored securely in .env
-OAuth 2.0 used for accessing Google APIs
-All network communication uses HTTPS
---
---
## 🤝 Author

-Even Patel
-📧 Connect via GitHub or email
-🏫 Developed as part of B.Tech CSE at Ahmedabad University
---
