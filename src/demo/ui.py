import streamlit as st
from src.data import DATA_DIR
from src.utils.parse_subtitle import Subtitle
 
st.header(':movie_camera: Learning English with Movies Subtile')
uploaded_file = st.file_uploader('Upload a (.srt) subtitle file: ')

# TODO: write uploaded file path in a temporary location for parsing task!

sub_file_path = DATA_DIR / 'subtitles' / 'friends.s01e02.720p.srt'
s = Subtitle(sub_file_path)

cols = st.columns(10)
ind = 0

if cols[3].button('<<'):
    ind -= 1
if cols[6].button('>>'):
    ind += 1

st.write(s.present_subtitle_partitions[ind])
