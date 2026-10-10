import streamlit as st

# Custom Style Tampilan Singkat
st.set_page_config(page_title="Kuis Teka-Teki Logika", page_icon="🧩")

st.caption("KUIS INTERAKTIF • TEKA-TEKI LOGIKA")
st.title("🧩 Petualangan Logika & Asah Otak")
st.write("Uji kemampuan berpikir kritismu dengan menjawab 3 soal teka-teki di bawah ini!")

st.divider()

# ==========================================
# SOAL 1
# ==========================================
st.progress(1 / 3)
st.info("SOAL 1 / 3")
st.text("SOAL 01 • TEKA-TEKI WAKTU")
st.subheader("Misteri Umur dan Waktu")
st.write("Jika kamu melempar batu ke udara, batu itu akan jatuh kembali ke tanah. Tapi ada satu hal yang terus naik dan tidak pernah turun sama sekali. Apakah itu?")

col1, col2 = st.columns(2)
with col1:
    s1_a = st.button("A. Balon Udara")
    s1_b = st.button("B. Umur Seseorang")
with col2:
    s1_c = st.button("C. Harga Sembako")
    s1_d = st.button("D. Burung Terbang")

if s1_a:
    st.error("❌ SALAH! Balon udara bisa mendarat dan turun kembali.")
elif s1_b:
    st.success(" BENAR! Umur seseorang akan terus bertambah (naik) dan tidak pernah berkurang (turun).")
elif s1_c:
    st.error("❌ SALAH! Harga barang bisa naik dan turun sesuai pasar.")
elif s1_d:
    st.error("❌ SALAH! Burung pasti akan mendarat lagi.")

st.divider()

# ==========================================
# SOAL 2
# ==========================================
st.progress(2 / 3)
st.info("SOAL 2 / 3")
st.text("SOAL 02 • LOGIKA BENDA")
st.subheader("Benda Berlubang")
st.write("Benda ini penuh dengan lubang dari atas sampai bawah, tapi tetap bisa menampung dan menahan air di dalamnya. Benda apakah itu?")

col1, col2 = st.columns(2)
with col1:
    s2_a = st.button("A. Saringan Teh")
    s2_b = st.button("B. Ember Bocor")
with col2:
    s2_c = st.button("C. Busa / Spons")
    s2_d = st.button("D. Jaring Ikan")

if s2_a:
    st.error("❌ SALAH! Air akan langsung lolos keluar dari saringan.")
elif s2_b:
    st.error("❌ SALAH! Ember bocor tidak bisa menahan air.")
elif s2_c:
    st.success(" BENAR! Spons penuh dengan rongga/lubang kecil, tetapi punya daya serap tinggi untuk menahan air!")
elif s2_d:
    st.error("❌ SALAH! Air tidak bisa tertahan di jaring ikan.")

st.divider()

# ==========================================
# SOAL 3
# ==========================================
st.progress(3 / 3)
st.info("SOAL 3 / 3")
st.text("SOAL 03 • TATA BAHASA & LOGIKA")
st.subheader("Awal dan Akhir")
st.write("Aku ada di awal 'Malam', ada di akhir 'Kelam', tapi aku tidak pernah ada di dalam 'Siang'. Siapakah aku?")

col1, col2 = st.columns(2)
with col1:
    s3_a = st.button("A. Huruf 'M'")
    s3_b = st.button("B. Kegelapan")
with col2:
    s3_c = st.button("C. Bulan & Bintang")
    s3_d = st.button("D. Huruf 'A'")

if s3_a:
    st.success(" BENAR! Kata *Malam diawali huruf 'M', Kelam* diakhiri huruf 'M', sedangkan kata 'Siang' tidak punya huruf 'M' sama sekali!")
elif s3_b:
    st.error("❌ SALAH! Ini bukan tentang suasana, tapi logika kata.")
elif s3_c:
    st.error("❌ SALAH! Perhatikan ejaan katanya.")
elif s3_d:
    st.error("❌ SALAH! Huruf 'A' juga ada di kata 'Siang'.")
