import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    select = option_menu('HITUNG LUAS BANGUN',
                         ['Hitung Luas Persegi',
                          'Hitung Luas Segitiga'],
                          default_index=0)
if (select == 'Hitung Luas Persegi Panjang'):
    st.title('HITUNG LUAS PERSEGI PANJANG')

    panjang = st.number_input("Masukan Nilai Panjang", 0)
    lebar = st.number_input ("Masukan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = panjang *lebar
        st.success(f"Luas Persegi Panjang Adalah = {luas}")
if (select == 'Hitung Luas Segitiga'):
    st.title('HITUNG LUAS SEGITIGA')

    alas = st.slider("Masukan Nilai Alas", 0,100)
    tinggi = st.slider("Masukan Nilai Tinggi",0, 100)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 0.5* alas * tinggi 
        st.success(f"Luas segitiga Adalah ={luas}")