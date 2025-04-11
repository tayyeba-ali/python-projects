# 🔐 Secure Data Encryption System

A simple yet secure web-based data encryption and storage application built using **Python** and **Streamlit**. This system allows users to register, login, store encrypted data, and retrieve it securely using a passkey.

## 🚀 Features

- 📟 **User Registration & Login**
- 🔒 **Password Hashing** using SHA-256 with salt
- 🧠 **Encrypted Data Storage** using `cryptography.fernet`
- 🛡️ **Passkey-based Decryption**
- 🚫 **Lockout Mechanism** after multiple failed login attempts
- 📂 **JSON-based Local Data Storage**

## 🧱 Built With

- [Streamlit](https://streamlit.io/) – Web interface
- [Cryptography](https://cryptography.io/en/latest/) – Encryption/Decryption
- [Hashlib](https://docs.python.org/3/library/hashlib.html) – Secure hashing
- [PBKDF2-HMAC](https://en.wikipedia.org/wiki/PBKDF2) – Key derivation
- Python Standard Libraries: `os`, `json`, `time`, `base64`

## 📦 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/secure-data-encryption-system.git
   cd secure-data-encryption-system
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit cryptography
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 📁 File Structure

```
.
├── app.py              # Main Streamlit application
├── secure_data.json    # Data storage (auto-created)
└── README.md           # Project documentation
```

## 🔐 Security Notes

- Passwords and keys are never stored in plaintext.
- Passkey is used to derive an encryption key — be sure to remember it, as it's required for decryption.
- Lockout feature prevents brute-force attacks by disabling login temporarily after 3 failed attempts.

## ✨ Future Improvements

- Add user profile management
- Enable file encryption support
- Deploy on the web (e.g., Streamlit Community Cloud)

## 🧑‍💻 Author

**[Tayyeba Ali]** – Developer of this project  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/tayyeba-ali-71a66029a/) or contribute on [GitHub](https://github.com/tayyeba-ali).


