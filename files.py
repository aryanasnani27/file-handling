import streamlit as st
import pandas as pd
st.subheader('Uploading the CSV File')
df=st.file_uploader("Upload the CSV file: ",type=['csv','xlsx'])

st.subheader('Loading the CSV file')
df=pd.read_csv('C:/Users/asnan/Desktop/CFG/streamlit/Products.csv')
st.table(df.head())
if df is not None:
    st.table(df.head())


st.subheader('Working with images')
img_file=st.file_uploader("Upload the image file",type=['png','jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader('Working with Video')
video_file=st.file_uploader('Upload the video: ',type=['mkv','mp4'])
if video_file is not None:
    st.video(video_file,start_time=0)

st.subheader("Working with Audios")
audio_file=st.file_uploader("Upload the audio file: ",type=['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file,start_time=0)