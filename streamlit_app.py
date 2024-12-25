import streamlit as st

st.title("🎈 Image Retrieve Model")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("This is a simple example to show how to build an image retrieval model using Streamlit.")
enable = st.checkbox('Use camera?')
image = st.camera_input("Take a picture",disabled = not enable)
if image:
    st.write("Hehe")
    st.image(image)
    


