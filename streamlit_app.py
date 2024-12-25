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

if "vis" not in st.session_state:
    st.session_state.vis = False
    st.session_state.visibility = "visible"
    
col1,col2 = st.columns([1,1])
with col1:
  st.checkbox("Disable selectbox widget", key="disabled")
  st.radio(
      "Set selectbox label visibility 👉",
      key="visibility",
      options=["visible", "hidden", "collapsed"],
  )

with col2:
  option = st.selectbox(
      "How would you like to be contacted?",
      ("Email", "Home phone", "Mobile phone"),
      label_visibility=st.session_state.visibility,
      disabled=st.session_state.disabled,
  )