import streamlit as st

st.set_page_config(page_title="Matematika Geometri", page_icon="🏆")

with st.sidebar:
    st.image("logo.png") 
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran"])
    st.caption("Dibuat oleh **farah**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung luas dan keliling `Persegi`")
        
        sisi = st.number_input("Masukkan Sisi", min_value=0.0, value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            
            st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.snow() # Efek animasi salju

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung luas dan keliling `Persegi Panjang`")
        
        panjang = st.number_input("Masukkan Panjang", min_value=0.0, value=0.0)
        lebar = st.number_input("Masukkan Lebar", min_value=0.0, value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            
            st.success(f"Luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons() 

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung luas dan keliling `Lingkaran`")
        
        jari_jari = st.number_input("Masukkan Jari-Jari", min_value=0.0, value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric(label="Keliling", value=f"{keliling:.2f}", border=True)
            st.balloons()