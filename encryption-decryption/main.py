import streamlit as st
import random
import string
import pyperclip

# https://docs.streamlit.io/develop/quick-reference/cheat-sheet

ALL_CHARS = string.printable[:-5]  # excludes last 5 non-printable chars

# Encryption function
def encryption(text, key):
    if not key:
        st.error("Key cannot be empty!")
        return ""
    
    encrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char not in ALL_CHARS:
            encrypted_text += char
            continue
        
        k = ALL_CHARS.index(key[i % key_length])
        c = (ALL_CHARS.index(char) + k) % len(ALL_CHARS)
        encrypted_text += ALL_CHARS[c]
    
    return encrypted_text

# Decryption function
def decryption(text, key):
    if not key:
        st.error("Key cannot be empty!")
        return ""
    
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char not in ALL_CHARS:
            decrypted_text += char
            continue
        
        k = ALL_CHARS.index(key[i % key_length])
        p = (ALL_CHARS.index(char) - k) % len(ALL_CHARS)
        decrypted_text += ALL_CHARS[p]
    
    return decrypted_text

# Initialize key in session state (So it dosen't disappear)
if "key" not in st.session_state:
    st.session_state.key = ""

key = st.session_state.key

st.title("Vigenère Encryption / Decryption")
st.subheader("By Elliot S")
mode = st.radio("Select Mode", ["Encryption", "Decryption"])

text = st.text_area("Enter your text here:")

nr = st.slider("Pick length of key", min_value=1, max_value=99, value=25)

# Generate random key using all printable characters
if st.button("Generate Random Key"):
    st.session_state.key = "".join(random.choice(ALL_CHARS) for _ in range(nr))

# Text area for key, keeping the generated key in session state (again, so it won't disappear before you can copy it..)
keytext = st.text_area("Enter Your Key and don't forget it", value=st.session_state.key)
st.session_state.key = keytext

# Encrypt / Decrypt button - Where the functions get called.
action = "encrypt" if mode == "Encryption" else "decrypt"

if st.button(f"Click to {action}"):
    if action == "encrypt":
        st.session_state.result = encryption(text, st.session_state.key)
    else:
        st.session_state.result = decryption(text, st.session_state.key)

# Show result and copy button if result exists
if "result" in st.session_state and st.session_state.result:
    label = "Encrypted text:" if action == "encrypt" else "Decrypted text:"
    st.text_area(label, st.session_state.result)
    
    if st.button(f"Copy {label}"):
        pyperclip.copy(st.session_state.result)
        st.success(f"{label} copied to clipboard!")
