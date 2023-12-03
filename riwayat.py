
import streamlit as st

#JANGAN DI SAMAKAN HARAP KEREATIF

st.set_page_config(
    page_title="Riwayat Sekolah | aisa",
    page_icon="👨‍🎓",
    layout="wide"
)
st.title("BEBERAPA JENJANG PENDIDIKAN YANG SAYA LALUI SELAMA MASA HIDUP")

st.container()
col1, col2, col3, col4 = st.columns(4)
with col3:
    st.subheader("MA Plus AL Bukhori")
   
with col4:
    st.subheader("UNU Rombel AL Bukhori")
   
st.container()
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col3:
     
    st.image("ma.png", width= 190)
with col4:
    
    st.image("unuu.png", width= 190)



