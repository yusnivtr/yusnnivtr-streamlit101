import streamlit as st
# enable = st.checkbox('Use camera?')
# image = st.camera_input("Take a picture",disabled = not enable)
# if image:
#     st.image(image)


from camera_input_live import camera_input_live

image = camera_input_live()

if image:
  st.image(image)
    


