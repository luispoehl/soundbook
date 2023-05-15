import streamlit as st
import requests
import json
import os
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play

def play_wav_file(wav_file):
    audio = AudioSegment.from_wav(wav_file)
    play(audio)

st.set_page_config(page_title="Let us explore the depths of generative storytelling.", page_icon="🚀")


st.text("")
st.image(
    "https://krea-prod-v1-generations.s3.us-east-1.amazonaws.com/images/fe82b2f6-cd12-48ef-bbec-1dec9fc90cd2.webp",
    width=125,
)

st.title("Generative storytelling")

st.write(
    """  
-   Create a fictional or real author, describe the book you want to listen to and enjoy!
-   Use cases: new books of existing authors, information gathering, educating children.
	    """
)

st.text("")

wav_file = "GENERATED WAV FILE FROM TEXT FROM HUGGINGFACE LUIS"
file_path = "tmp_chunks_story_name/preamble10.wav"
wav_file, sr = sf.read(file_path)
if wav_file is not None:
    st.audio(wav_file, sample_rate=sr, format="audio/wav")
    if st.button("Play"):
        play_wav_file(wav_file)

else:
    path_in = None
    st.stop()