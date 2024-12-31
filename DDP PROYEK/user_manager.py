import streamlit as st

class UserManager:
    def __init__(self):
        if "users" not in st.session_state:
            st.session_state.users = {}
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        if "username" not in st.session_state:
            st.session_state.username = ""

    def login(self):
        st.title("Login 🎇")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(f"Selamat datang di Seruni Bookstore, {username}!")
            else:
                st.error("Username atau password salah.")

    def register(self):
        st.title("Registrasi 📁")
        st.write("Silahkan Registrasi terlebih dahulu")
        new_username = st.text_input("Username Baru")
        new_password = st.text_input(" Masukkan Password", type="password")
        confirm_password = st.text_input("Konfirmasi Password", type="password")
        if st.button("Daftar"):
            if new_username in st.session_state.users:
                st.error("Username sudah digunakan.")
            elif new_password != confirm_password:
                st.error("Password tidak cocok.")
            elif new_username and new_password:
                st.session_state.users[new_username] = new_password
                st.success("Pendaftaran berhasil! Silakan login.")
            else:
                st.error("Username dan password tidak boleh kosong.")
