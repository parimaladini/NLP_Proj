import streamlit as st
from gtts import gTTS
import speech_recognition as sr

st.title('Text-To-Speech and Speech-To-Text Converter')

option = st.selectbox('Select Operation:', ('Text-To-Speech Conversion', 'Speech-To-Text Conversion'))

if option == 'Text-To-Speech Conversion':
    text_input = st.text_area('Enter Text:', '')
    if st.button('Convert to Speech'):
        if text_input:
            language = 'en'
            speech = gTTS(text=text_input, lang=language, slow=False)
            speech.save("text.mp3")
            st.audio("text.mp3", format='audio/mp3')

elif option == 'Speech-To-Text Conversion':
    st.write('Click the button below and start speaking...')
    if st.button('Start Recording'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text_output = r.recognize_google(audio, language='en-IN')
                st.text("Recognized Text: " + text_output)
            except sr.UnknownValueError:
                st.warning("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                st.error("Could not request results from Google Speech Recognition service; {0}".format(e))

