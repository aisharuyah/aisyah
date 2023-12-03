
import streamlit as st


st.set_page_config(
    page_title="Organizational Experience|aisa",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Pengalaman Organisasi")
st.write("Hanya Satu Organisasi Yang Saya Ikuti; ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("pelatihan balai lapangan kerja (BLK)")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("blk.jpg", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Menjadi anggota pelatihan balai lapangan kerja*")
   