import streamlit as st

st.title("🎈 Image Retrieve Model")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
image = st.camera_input("Take a picture")
if image:
    st.image(image)

