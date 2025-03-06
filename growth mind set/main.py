import streamlit as st

st.set_page_config(page_title="Growth mindset project", page_icon=":✨:")
st.title("Growth Mindset Project 🌱")
st.header("🚀Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes , and unlock your full potential . This AI-powerd app helps you build a growth mindset with reflaction, challenges , and achievements 🌟")

st.header("💡Today's Growth Mindset Quote")
st.write("I am not afraid of storms, for I am learning how to sail my ship.")

st.header("🌟What's Your Challenge Today?")
user_input = st.text_input("Enter your challenge here:")

if user_input:
    st.success(f"You are facing: {user_input}.Keep pushing yourself and remember that challenges are opportunities to grow! 🌱")
else:
    st.warning("Tell us your challenge today! 🌟")

st.header("🌱Your Reflections")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Thank you for sharing your reflections: {reflection}🌟")
else:
    st.info("Reflecting on past experiences helps you grow. Share your thoughts with us! 🌱")  

st.header("🏆Your Achievements")
achievement = st.text_area("Share something you've recently accomplished:")

if achievement:
    st.success(f"Congratulations on your achievement: {achievement}! Keep up the great work! 🌟")
else:
    st.info("Celebrate your wins, no matter how small! Share your achievements with us! 🏆")


st.write("---")
st.write("Challenges are what make life interesting. Overcoming them is what makes life meaningful.🚀")
st.write("Created by Tayyeba Ali")
