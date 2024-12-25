import streamlit as st

st.set_page_config(page_title="Image Retrieval Program", page_icon=":shark:", layout="wide",initial_sidebar_state='auto')

# # hide the part of the code, as this is just for adding some custom CSS styling but not a part of the main idea 
# hide_streamlit_style = """
# 	<style>
#   #MainMenu {visibility: hidden;}
# 	footer {visibility: hidden;}
#   </style>
# """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) # hide the CSS code from the screen as they are embedded in markdown text. Also, allow streamlit to unsafely process as HTML

st.title("Image Retrieval Program")
st.info("Hehe")
    
col1,col2 = st.columns(2)

if col1.button("Button 1",use_container_width=True):
    enable = st.checkbox("Enable",value=False)
    image = st.camera_input('Cheer up!')
if col2.button("Button 2",use_container_width=True):
    st.write("Button 2 is clicked")