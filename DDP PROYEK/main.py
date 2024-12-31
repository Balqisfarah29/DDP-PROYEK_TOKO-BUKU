import streamlit as st
from user_manager import UserManager
from book_store import BookStore

class MainApp:
    def __init__(self):
        self.user_manager = UserManager()
        self.book_store = BookStore()

    def run(self):
        if not st.session_state.logged_in:
            option = st.sidebar.selectbox("Pilih Opsi", ["Login", "Registrasi"])
            if option == "Login":
                self.user_manager.login()
            else:
                self.user_manager.register()
        else:
            option = st.sidebar.selectbox(
                f"Selamat datang, {st.session_state.username}!",
                ["Toko Buku", "Keranjang", "Logout"]
            )
            if option == "Toko Buku":
                self.book_store.display_books()
            elif option == "Keranjang":
                self.book_store.display_cart()
            elif option == "Logout":
                st.session_state.logged_in = False
                st.session_state.cart = []
                st.session_state.username = ""
                st.success("Anda telah logout.")
                st.write("Terima Kasih Sudah Berkunjung Ke Toko Buku Kami!")

# Jalankan aplikasi
if __name__ == "__main__":
    app = MainApp()
    app.run()
