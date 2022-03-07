import streamlit as st
import os
import time

st.title("Requirements fixer")
st.write("Simply upload a requirements.txt without fixed versions and get back a file with all dependencies fixed to the newest version.")

file = st.file_uploader("Upload your requirements.txt here", "txt", accept_multiple_files=False)

if file is not None:
    
    data = None
    with st.spinner("Processing file"):
        # save file temporarily
        tempName = str(time.time_ns())
        tempFileNameIn = f"{tempName}_uploaded_requirements.txt"
        tempFileNameOut = f"{tempName}_finished_requirements.txt"
        with open(tempFileNameIn,"wb") as f: 
            f.write(file.getbuffer())

        # run update script
        os.system(f"bash ./update.sh {tempFileNameIn} {tempName} {tempFileNameOut}")

        # read result
        with open(tempFileNameOut, 'r') as file:
            data = file.read()
        
        os.remove(tempFileNameIn)
        os.remove(tempFileNameOut)

    if data is not None:
        st.download_button('Download fixed file', data, "requirements.txt")