import streamlit as st # For web app interface
import hashlib  # For password hashing
import json # For data storage
import os # For file handling
import time # For time management
from cryptography.fernet import Fernet # For encryption/decryption 
from base64 import urlsafe_b64encode # For key generation
from hashlib import pbkdf2_hmac # For password hashing

# Constants
DATA_FILE = 'secure_data.json'
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60  

# Session State Init
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Utility Functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def generate_key(password):
    key = pbkdf2_hmac('sha256', password.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except Exception:
        return None

# Load existing data
stored_data = load_data()

# App UI
st.title("🔐 Secure Data Encryption System")

menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("📚 Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data Encryption System")
    st.markdown("""
    🔒 This system allows you to:
    - Securely store data with encryption
    - Retrieve it using a unique passkey
    - Stay protected with lockout after multiple failed login attempts
    """)

elif choice == "Register":
    st.subheader("🆕 New User Registration")
    username = st.text_input("👤 Choose a username")
    password = st.text_input("🔑 Choose a password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("⚠️ User already exists.")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User registered successfully!")
        else:
            st.error("❌ Both fields are required.")

elif choice == "Login":
    st.subheader("🔐 User Login")

    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"⏳ Too many failed attempts. Please wait {remaining} seconds.")
        st.stop()

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"👋 Welcome back, {username}!")
        else:
            st.session_state.failed_attempts += 1
            remaining_attempts = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invalid Credentials! Attempts left: {remaining_attempts}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("⛔ Too many failed attempts. Locked for 60 seconds.")
                st.stop()

elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("⚠️ Please login first.")
    else:
        st.subheader("🗂️ Store Encrypted Data")
        data = st.text_area("📝 Enter data to encrypt")
        passkey = st.text_input("🔑 Encryption Key (passphrase)", type="password")

        if st.button("🔒 Encrypt and Save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                save_data(stored_data)
                st.success("✅ Data encrypted and stored successfully!")
            else:
                st.error("❌ All fields are required.")

elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("⚠️ Please login first.")
    else:
        st.subheader("📥 Retrieve Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])
        
        if not user_data:
            st.info("ℹ️ No data found for the user.")
        else:
            st.markdown("🔒 Your Encrypted Entries:")
            for i, item in enumerate(user_data):
                st.code(item, language='text')

        encrypted_input = st.text_area("🔐 Enter Encrypted Text")
        passkey = st.text_input("🔑 Enter Passkey to Decrypt", type="password")

        if st.button("🔓 Decrypt"):
            result = decrypt_text(encrypted_input, passkey)
            if result:
                st.success(f"✅ Decrypted Data:\n\n{result}")
            else:
                st.error("❌ Incorrect passkey or invalid data.")
