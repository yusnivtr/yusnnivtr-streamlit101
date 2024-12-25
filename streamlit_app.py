import streamlit as st

st.set_page_config(page_title="Image Retrieval Program", page_icon=":shark:", layout="wide", initial_sidebar_state='auto')

# hide the part of the code, as this is just for adding some custom CSS styling but not a part of the main idea 
hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) # hide the CSS code from the screen as they are embedded in markdown text. Also, allow streamlit to unsafely process as HTML
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.nippon.com/en/ncommon/contents/japan-topics/601750/601750.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)

st.title("Image Retrieval Program")
st.info("Hehe")

st.subheader("Input Image")
col1, col2 = st.columns([1, 3])

method = 'Take a picture'

with col1:
  method = st.radio('Select Input method',options=['Take a picture','Upload a picture'])
  
with col2:
  if method == 'Take a picture':
    enable = st.checkbox('Enable Camera')
    img = st.camera_input('Take a picture',disabled= not enable)
  else:
    img = st.file_uploader('Upload a picture')
    
if img:
  st.image(img, caption='Uploaded Image', width=200,use_container_width=True)
  
st.subheader("Selecting Model")
model = st.selectbox('Select Model',options=['VGG16','ResNet50','InceptionV3'])

st.subheader("Output")

