import streamlit as st

st.set_page_config(page_title="Matematika Geometri", page_icon="🏆")

st.markdown("""
    <style>
    .stAppDeployButton {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("logo.png") 
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Trapesium"])
    st.caption("Dibuat oleh **Farah & Alifa**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung luas dan keliling `Persegi`")
        
        sisi = st.number_input("Masukkan Sisi", min_value=0.0, value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric(label="Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung luas dan keliling `Persegi Panjang`")
        
        panjang = st.number_input("Masukkan Panjang", min_value=0.0, value=0.0)
        lebar = st.number_input("Masukkan Lebar", min_value=0.0, value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric(label="Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

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
            st.snow()

    case "Segitiga":
        st.title("📐 Bangun Datar: Segitiga")
        st.write("Aplikasi ini akan menghitung Luas dan Keliling Segitiga.")
        
        alas = st.number_input("Masukkan Alas", min_value=0.0, value=0.0, step=0.5)
        tinggi = st.number_input("Masukkan Tinggi", min_value=0.0, value=0.0, step=0.5)
        sisi_miring = st.number_input("Masukkan Sisi Miring", min_value=0.0, value=0.0, step=0.5)
        
        if st.button("Hitung Segitiga", type="primary"):
            if alas > 0 and tinggi > 0:
                luas = 0.5 * alas * tinggi
                keliling = alas + tinggi + sisi_miring
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Luas Segitiga", value=f"{luas:.2f}", border=True)
                with col2:
                    st.metric(label="Keliling Segitiga", value=f"{keliling:.2f}", border=True)
                st.snow()
            else:
                st.warning("Silakan masukkan nilai alas dan tinggi!")

    case "Trapesium":
        st.title("📐 Bangun Datar: Trapesium")
        st.write("Aplikasi ini akan menghitung Luas dan Keliling Trapesium.")
        
        sisi_atas = st.number_input("Masukkan Sisi Atas", min_value=0.0, value=0.0, step=0.5)
        sisi_bawah = st.number_input("Masukkan Sisi Bawah", min_value=0.0, value=0.0, step=0.5)
        tinggi_t = st.number_input("Masukkan Tinggi", min_value=0.0, value=0.0, step=0.5)
        sisi_miring_t = st.number_input("Masukkan Sisi Miring", min_value=0.0, value=0.0, step=0.5)
        
        if st.button("Hitung Trapesium", type="primary"):
            if sisi_atas > 0 and sisi_bawah > 0 and tinggi_t > 0:
                luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi_t
                keliling = sisi_atas + sisi_bawah + (2 * sisi_miring_t)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Luas Trapesium", value=f"{luas:.2f}", border=True)
                with col2:
                    st.metric(label="Keliling Trapesium", value=f"{keliling:.2f}", border=True)
                st.snow()
            else:
                st.warning("Silakan masukkan nilai trapesium yang valid!")