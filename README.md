# 🏥 Patient Record Management System

A modular, secure, and user-friendly **Python desktop application** for managing patient records. Built with a clean **Tkinter GUI** and powered by **Google Sheets as a cloud database**, this system ensures efficient record handling, secure authentication, and seamless communication via automated email confirmations.

---

## 🚀 Overview

This project is designed to simplify patient data management for clinics, small hospitals, or academic purposes. It follows a **modular architecture**, making it easy to maintain, extend, and scale.

---

## ✨ Key Features

* 🧾 **Full CRUD Operations** – Add, Edit, Delete, and View patient records
* 📧 **Automated Email Confirmation** on patient registration
* ☁️ **Cloud Storage with Google Sheets** (real-time access & backup)
* 🖥️ **Modern GUI** using `tkinter` + `ttk`
* 🔐 **Secure Authentication** via OAuth 2.0
* 📊 **Revenue Summary Dashboard**
* 📤 **Export Data to CSV**
* 🧩 **Modular Codebase** (separate logic files for each feature)
* 🔒 **Environment-based Secret Management** using `.env`

---

## 📂 Project Structure

```
patient-record-management/
│
├── main.py                  # Application entry point
├── gui.py                   # Tkinter GUI (frontend)
│
├── modules/                 # Backend logic
│   ├── add_patient.py
│   ├── edit_patient.py
│   ├── delete_patient.py
│   ├── display_patient.py
│   ├── clear_fields.py
│   ├── email_confirmation.py
│   ├── google_sheets.py
│   ├── auth.py
│   ├── utils.py
│   ├── report_summary.py
│   ├── export_data.py
│
├── config/
│   ├── creds.json           # 🔐 Google Service Account Key (ignored)
│   └── creds_template.json  # Template for setup
│
├── assets/
│   └── logo.png             # UI assets
│
├── .env                     # 🔐 Email credentials (ignored)
├── .env_template            # Environment template
├── .gitignore               # Ignored files
└── README.md                # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/patient-record-management.git
cd patient-record-management
```

---

### 2️⃣ Install Dependencies

```bash
pip install gspread oauth2client pandas python-dotenv
```

---

### 3️⃣ Configure Google Sheets API

1. Go to **Google Cloud Console**
2. Create a new project
3. Enable:

   * Google Sheets API
   * Google Drive API
4. Create a **Service Account**
5. Generate and download the JSON key
6. Place it in the `config/` folder as:

```
config/creds.json
```

---

### 4️⃣ Setup Google Sheet

1. Create a sheet named:

```
patient_records
```

2. Add the following headers in the first row:

```
Patient Id | Name | Age | Gender | Diagnosis | Medical History | Current Treatment | Date of Registration | Fees | Email-id
```

3. Share the sheet with your **service account email** (from `creds.json`) and grant **Editor access**

---

### 5️⃣ Configure Email Service

1. Create a `.env` file:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

2. Enable **2-Step Verification** in Gmail
3. Generate an **App Password** and use it above

---

### 6️⃣ Run the Application

```bash
python main.py
```

---

## 🔐 Security Best Practices

* ✅ Sensitive files (`creds.json`, `.env`) are excluded via `.gitignore`
* ✅ Email credentials are never hardcoded
* ✅ OAuth 2.0 ensures secure Google API access
* ✅ All communications use HTTPS

---

## 📊 Future Improvements

* 🔍 Search & filter functionality
* 📱 Web-based version (Flask/Django)
* 🔐 Role-based authentication (Admin/User)
* 📈 Advanced analytics dashboard
* 🗃️ Database migration (SQLite/PostgreSQL)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 📜 License

This project is licensed under the **MIT License**.

---

> 💡 *A simple yet powerful system to digitize patient management efficiently and securely.*
