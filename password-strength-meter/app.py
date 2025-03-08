import re  # Regular expression library  number or character data sakhtai han
import streamlit as st

st.set_page_config(page_title="Password Strength Checker By Tayyeba Ali", page_icon="🧊", layout="centered")
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 90% !important; margin:}
    .stButton button {width : 50% ; background-color #4CAF50 ; color: white; font-size: 18px ; }
    .stButton button:hover {background-color: #45a049; color:white;}
</style>
""", unsafe_allow_html=True)

#page title and description
st.title("🔐Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

#function to check password strength
def password_strength( password):
    score = 0
    feedback= []

    if len(password) > 8:
        score += 1
    else:
        feedback.append("❌Password should be **atleast 8 character long**")
    
    if re.search(r"[A-Z]", password ) and re.search(r"[a-z]" , password):
        score += 1
    else:
        feedback.append("❌Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")
    
    if re.search(r"\d", password): #\d is used to match any digit(/d ya check kerta hn digit character)
        score += 1
    else:
        feedback.append("❌Password should include **atleast one number (0-9)**.")

    #special characters
    if re.search(r"[!@#$%^&*()_+{}:;.,<>?]", password):
        score += 1
    else:
        feedback.append("❌Password should include **atleast one special character (!@#$%^&*()_+{}:;.,<>?)**.")

    #display password strength
    if score == 4 :
        st.success("✅ Your password is **Strong**.")
    elif score == 3:
        st.info("⚠️ Your password is **Medium**.")
    else:
        st.error("❗️ Your password is **Weak** - Follow the suggestion below to strength it.")
    
    #feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password** "): #explander multiple element check and show detail
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help = "Enter your password is strong 🔐")

#Button Working
if st.button("Check Strength"):
    if password:
        password_strength(password)
    else:
        st.warning("⚠️Please enter a password first.")



