## Vigenère Encryption / Decryption Tool

A small web application for encrypting and decrypting text using a Vigenère-style cipher.
The interface is built with Streamlit and allows users to easily generate keys, encrypt messages, and decrypt previously encrypted text.

This project was created as part of my Computer Science learning and experimentation with encryption concepts.

Features

* Encrypt text using a Vigenère-style cipher

* Decrypt previously encrypted text using the same key

* Generate a random key with customizable length

* Supports all printable ASCII characters

* Simple web interface built with Streamlit

* Copy encrypted or decrypted results directly to the clipboard

## How It Works

The program uses a variation of the Vigenère cipher, where each character in the plaintext is shifted based on a repeating key.

* Each character is mapped to an index in the printable ASCII character set.

* The key determines how much each character is shifted.

* During encryption, characters are shifted forward.

* During decryption, characters are shifted backward.

Characters that are not part of the supported character set are left unchanged.

## Installation

Clone the repository:

```bash
git clone https://github.com/Eonaris/school-projects.git
```
```bash
cd school-projects/encryption-and-decryption
```

Install the required packages:

  pip install streamlit pyperclip
## Running the Program

Run the Streamlit application:

  streamlit run main.py

This will start a local web interface where you can interact with the encryption tool.

## Usage

1. Choose Encryption or Decryption mode.

2. Enter the text you want to process.

3. Enter a key or generate a random one.

4. Click the button to encrypt or decrypt.

5. Copy the result if needed.
