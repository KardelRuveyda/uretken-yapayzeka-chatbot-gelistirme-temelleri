import streamlit as st

# Şifreleme ve şifre çözme fonksiyonları
def mesaj_sifrele(mesaj):
    alfabe = 'abcdefghijklmnopqrstuvwxyz'
    sifrelenmis = ''
    for karakter in mesaj:
        if karakter.lower() in alfabe:  # Harf kontrolü
            index = (alfabe.index(karakter.lower()) + 5) % 26
            sifrelenmis += alfabe[index] if karakter.islower() else alfabe[index].upper()
        elif karakter.isdigit():  # Sayı kontrolü
            sifrelenmis += karakter[::-1]  # Sayıyı ters çevir
        else:  # Noktalama veya boşluklar aynı kalır
            sifrelenmis += karakter
    return sifrelenmis

def sifre_coz(mesaj):
    alfabe = 'abcdefghijklmnopqrstuvwxyz'
    cozulmus = ''
    for karakter in mesaj:
        if karakter.lower() in alfabe:  # Harf kontrolü
            index = (alfabe.index(karakter.lower()) - 5) % 26
            cozulmus += alfabe[index] if karakter.islower() else alfabe[index].upper()
        elif karakter.isdigit():  # Sayı kontrolü
            cozulmus += karakter[::-1]  # Sayıyı ters çevir
        else:  # Noktalama veya boşluklar aynı kalır
            cozulmus += karakter
    return cozulmus

# Streamlit uygulaması
st.title("🔐 Şifre Kırıcı Chatbot")

# CSS ile arka plan ve metin kutuları
custom_css = """
<style>
    .stApp {
        background-color: #FDEEF4; /* Pudra rengi arka plan */
    }
    input {
        background-color: #FFFFFF !important; /* Tam beyaz */
        border: 1px solid #DDDDDD !important; /* Açık gri çerçeve */
        color: #000000 !important; /* Siyah yazı */
        border-radius: 5px !important; /* Hafif yuvarlak köşeler */
        padding: 5px !important; /* Metin alanı dolgusu */
    }
    textarea {
        background-color: #FFFFFF !important; /* Tam beyaz */
        border: 1px solid #DDDDDD !important; /* Açık gri çerçeve */
        color: #000000 !important;
        border-radius: 5px !important;
        padding: 5px !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Giriş ekranında örnek mesaj ve çözümü göster
st.write("### Örnek Kullanım")
st.write("**Şifrelenmiş Mesaj:** ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl")
st.write("**Çözülmüş Mesaj:** the quick brown fox jumps over the lazy dog")

# İki sütun yapısı
col1, col2 = st.columns(2)

# Sol sütun: Şifreleme
with col1:
    st.subheader("🔒 Mesaj Şifreleme")
    sifrelenecek_mesaj = st.text_input("Şifrelemek istediğiniz mesajı yazın:")
    if sifrelenecek_mesaj:
        sifrelenmis_mesaj = mesaj_sifrele(sifrelenecek_mesaj)
        st.write(f"**Şifrelenmiş Mesaj:** {sifrelenmis_mesaj}")

# Sağ sütun: Şifre Çözme
with col2:
    st.subheader("🔓 Mesaj Çözme")
    cozulmesi_gereken_mesaj = st.text_input("Çözmek istediğiniz şifreli mesajı yazın:")
    if cozulmesi_gereken_mesaj:
        cozulmus_mesaj = sifre_coz(cozulmesi_gereken_mesaj)
        st.write(f"**Çözülmüş Mesaj:** {cozulmus_mesaj}")
