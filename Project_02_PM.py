import re
import streamlit as st
import secrets
import string

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "password123", "abc123", "letmein",
    "monkey", "football", "iloveyou", "admin", "welcome", "1234", "passw0rd", "zaq1zaq1"
}

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ Your password is too common! Choose a more secure one."]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    """Generates a secure random password"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(length))

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter a password:", type="password")

if password:
    score, feedback = check_password_strength(password)
  
    if score == 4:
        st.success("✅ **Strong Password!** 🎉")
    elif score == 3:
        st.warning("⚠️ **Moderate Password - Consider adding more security features.**")
    else:
        st.error("❌ **Weak Password - Improve it using the suggestions below.**")

    for msg in feedback:
        st.write(msg)

    if score < 4:
        st.info(f"🔹 Suggested Strong Password: `{generate_strong_password()}`")

