import streamlit as st

st.set_page_config(page_title="Image Retrieval Program", page_icon=":shark:", layout="wide",initial_sidebar_state='auto')

# hide the part of the code, as this is just for adding some custom CSS styling but not a part of the main idea 
hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) # hide the CSS code from the screen as they are embedded in markdown text. Also, allow streamlit to unsafely process as HTML

st.header("Starting Image Retrieval Program")

with st.expander("Upload Image"):
    col1,col2 = st.columns(2,vertical_alignment='center')
    if col1.button('Take a photo',use_container_width=True):
        st.write("Take a photo")
        enable = st.checkbox("Enable for camera")
        image = st.camera_input('Cheer up! Smile for the camera',use_container_width=True,disabled=not enable)
    if col2.button('Upload a photo',use_container_width=True):
        st.write("Upload a photo")
        image = st.file_uploader("Upload an image", type=['jpg','jpeg','png'],use_container_width=True)
    
  