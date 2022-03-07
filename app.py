import streamlit as st
import os
import time

st.title("Requirements fixer")
st.write("Simply upload a requirements.txt without fixed versions and get back a file with all dependencies fixed to the newest version.")

if not 'file' in st.session_state or st.session_state['file'] is None:
    st.file_uploader("Upload your requirements.txt here", "txt", accept_multiple_files=False, key='file')

if 'file' in st.session_state and st.session_state['file'] is not None:
    if st.button("Clear file"):
        del st.session_state['file']

    data = None
    with st.spinner("Processing file"):
        # save file temporarily
        tempName = str(time.time_ns())
        tempFileNameIn = f"{tempName}_uploaded_requirements.txt"
        tempFileNameOut = f"{tempName}_finished_requirements.txt"
        with open(tempFileNameIn,"wb") as f: 
            f.write(st.session_state['file'].getbuffer())

        # run update script
        os.system(f"bash ./update.sh {tempFileNameIn} {tempName} {tempFileNameOut}")

        # read result
        with open(tempFileNameOut, 'r') as file:
            data = file.read()
        
        os.remove(tempFileNameIn)
        os.remove(tempFileNameOut)

    if data is not None:
        st.download_button('Download fixed file', data, "requirements.txt")