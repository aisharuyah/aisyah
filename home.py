
import streamlit as st

#SILAHKAN TINGGAL DI GANTI 2 SAM FOTO2NYA JAN LUPA !!!!

st.set_page_config(
    page_title="Portfolio | aisa",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("My Profile")
   st.image("ruyah01.jpg", width= 300)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : Ru'yatun Aisha")
   st.caption("NIM : 0402201093")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 13 juni 2002 
            - Alamat               : Pengabean Losari Brebes
            - Hobi                 : Menulis
            - Cita-cita            : Pengusaha
            - Hal yang disukai     : Mayoran
            - Status               : Jomblo
            """
        )
st.header("*Call Me If You Want*")