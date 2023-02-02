import speech_recognition as sr
import streamlit as st

# Declaration

recognizer = sr.Recognizer()

# Page Title

st.set_page_config(page_title="STT", page_icon=":smile:", layout="wide")

# Page Header

st.subheader("Welcome to my first web app! :wave:")
st.title("Speech-to-Text Transcription Website Application")
st.write("Developed by Harith through Streamlit and Jupyter Notebook.")
st.write("This web app is still in development so there might be some bugs occuring during the transcription process.")

# Page Main and Sidebar

audio_file = st.sidebar.file_uploader("Upload Audio File", type={"wav"})
if audio_file is not None:
    st.sidebar.subheader("Audio File")
    st.sidebar.audio(audio_file)
if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        with sr.AudioFile(audio_file) as source:
                speech_audio = recognizer.listen(source)
        try:
            transcription_result = recognizer.recognize_google(speech_audio, language="ms-MY")
            st.subheader("Transcription Result:")
            st.write(transcription_result)
            st.sidebar.success("Transcription Complete")  
        except Exception as ex:
            print(ex)
    else:
        st.sidebar.error("Please upload an audio file")