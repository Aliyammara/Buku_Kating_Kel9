import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen MEDKRAF",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobi: {data_list[i]['hobi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c4vPah1Xk96YFEEP7WWAYdlH3lxi_mR7", #1
            "https://drive.google.com/uc?export=view&id=1w6tN0fO-6taKaN4MatP8DS9EBjhpHi69", #2
            "https://drive.google.com/uc?export=view&id=16pCo3MQuL1k9RTefjuFXqtKAK-yDzXfT", #3
            "https://drive.google.com/uc?export=view&id=1jml24USid6KLJZJA7Ijz1YMg9_KaVycO", #4
            "https://drive.google.com/uc?export=view&id=1PHMwZD7ONXCcej12gIy0vbXln9M3akws", #5
            "https://drive.google.com/uc?export=view&id=17cXKBnrVH-HCM2qHaYHlK_366LP9IN-C", #6
            
        ]
        data_list = [
            {
                
                "nama"	    : "Kharisma Gumilang",
                "nim"		: "121450142",
                "umur"	    : "21",
                "asal"		:" Palembang",
                "alamat"	: "Jl. Pulau Damar",
                "hobi"		: "Dengar musik",
                "sosmed"	: "@gumilangkhasirma",
                "kesan"	    : "Sama seperti namanya, memiliki kharisma.",  
                "pesan"	    : "semoga sukses selalu, dan selalau ingat pada HMSD adyatama"# 1
            },
            {
                "nama"	    : "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	    : "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	    : "asik beut orangnya.",  
                "pesan"	    : "semoga semakin erat kedekatan nya dengan bang gumi."# 2
            },
            {
                "nama"      : "Meliza Wulandari",
                "nim"       : "121450065",
                "umur"      : "20",
                "asal"      : "Pagar Alam",
                "alamat"    : "Kota Baru",
                "hobbi"     : "Drakoran",
                "sosmed"    : "@wulandarimeliza",
                "kesan"     : "kakaknya lucu dan baik.",  
                "pesan"     : "selalu semangat kak menjalani hari dengan drakoran."# 3
            },
            {
                "nama"      : "Putri Maulida Chairani",
                "nim"       : "121450050",
                "umur"      : "21",
                "asal"      : "Payakumbuh",
                "alamat"    : "JL. Nangka IV",
                "hobbi"     : "Dengarin Bang Pandra gitaran",
                "sosmed"    : "@ptrimaulidaaa_",
                "kesan"     : "asik banget cara ngomongnya",  
                "pesan"     : "semangat trus belajarnya sambil dengerin bang pandra dengerin gitar"# 4
            },
            {
                "nama"      : "Hartiti Fadilah",
                "nim"       : "121450031",
                "umur"      : "21",
                "asal"      : "Palembang",
                "alamat"    : "pemda",
                "hobbi"     : "nyanyi",
                "sosmed"    : "@hrtfdlh",
                "kesan"     : "wong kito galo",  
                "pesan"     : "semoga bisa karaukean bareng kakaknya."# 5
            },
            {
                "nama"      : "Nadilla Andhara Putri",
                "nim"       : "121450003",
                "umur"      : "21",
                "asal"      : "Metro",
                "alamat"    : "Kota baru",
                "hobbi"     : "membaca",
                "sosmed"    : "@nadillaandr26",
                "kesan"     : "kalem",  
                "pesan"     : "sukses selalu kak."# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak D",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak E",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak D",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
