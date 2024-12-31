import streamlit as st

books = [
    {
        "title": "Python Programming",
        "author": "John Doe",
        "price": 103000,
        "image": "https://deepublishstore.com/wp-content/uploads/2023/05/Python.png "
    },
    {
        "title": "Rumah Ini Tak Lagi Sama",
        "author": "Jane Smith",
        "price": 70400,
        "image": "https://mojokstore.com/wp-content/uploads/2024/01/Rumah-Ini-Tak-Lagi-Sama.jpeg"
    },
    {
        "title": "Peluk Hangat Untuk Diri Sendiri",
        "author": "Emily Davis",
        "price": 77000,
        "image": "https://gagasmedia.net/wp-content/uploads/2024/09/peluk-hangat_cover-Resita-Febiratri.jpg"
    },
    {
        "title": "Dasar Pemrograman Web",
        "author": "Ach.Khozami S.Kom., M.Kom",
        "price": 35000,
        "image": "https://a.cdn-myedisi.com/book/cover/mncpublishing-a_61fa34187d36c089993630.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Maaf, Ternyata Aku Tidak Sekuat Itu",
        "author": "Coretan Lena",
        "price": 70100,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/items/Maaf_Ternyata_Aku_Tidak_Sekuat_Itu.jpg"
    },
    {
        "title": "Bandung After Rain",
        "author": "Wulan Nur Amalia",
        "price": 89100,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/products/3ccna3dv64.jpg"
    },
    {
        "title": "Untuk Kamu Yang Malas Dan Suka Menunda",
        "author": "Noura",
        "price": 80000,
        "image": "https://lib.atim.ac.id/uploaded_files/sampul_koleksi/original/Monograf%20-%20Buku%20Teks,%20Buku%20Ajar/13021.jpg"
    },
    {
        "title": "Kamu Terlalu Banyak Bercanda",
        "author": "Marchella FP",
        "price": 120000,
        "image": "https://html.scribdassets.com/9j7gwc02ps8t31yr/images/1-4ef0985d8a.jpg"
    },
    {
        "title": "Rusak Saja Buku Ini Girl Version",
        "author": "Sony Adams",
        "price": 36000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/1/9/es2e9r363pcja8bhc9pplx.jpg"
    },
    {
        "title": "Kamu Tak Harus Sempurna",
        "author": "Anastasia Satrio M.Psi, Psi",
        "price": 37200,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/items/KAMU_TAK_HARUS_SEMPURNA.jpg"
    },
    {
        "title": "Before We Say Goodbye",
        "author": "Toshikazu Kawaguchi",
        "price": 238000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/products/xz-xor9539.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1387700008i/301347.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
    {
        "title": "Kamu Tenang Kamu Menang",
        "author": "Astrid Savitri",
        "price": 56000,
        "image": "https://image.gramedia.net/rs:fit:0:0/plain/https://cdn.gramedia.com/uploads/picture_meta/2024/6/15/p7mgvtr2j42r8xc2czzbxm.jpg"
    },
]
    

class BookStore:
    def __init__(self):
        if "cart" not in st.session_state:
            st.session_state.cart = []

    def display_books(self):
        st.title("Daftar Buku 📚📖")
        for idx, book in enumerate(books):
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(book["image"], width=100)
            with col2:
                st.text(f"{book['title']}\n{book['author']}\nRp {book['price']}")
                if st.button(f"Tambahkan ke Keranjang 🛒", key=f"add_{idx}"):
                    st.session_state.cart.append(book)
                    st.success(f"{book['title']} telah ditambahkan ke keranjang!")

    def display_cart(self):
        st.title("Keranjang Belanja 🛒")
        if not st.session_state.cart:
            st.write("Keranjang Anda kosong.")
        else:
            total = 0
            for idx, book in enumerate(st.session_state.cart):
                st.write(f"**{book['title']}** - Rp {book['price']}")
                total += book["price"]
                if st.button(f"Hapus", key=f"remove_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.experimental_rerun()
            st.write(f"**Total Harga: Rp {total}**")
            if st.button("Checkout"):
                st.success("Terima kasih telah berbelanja di toko buku kami!")
                st.session_state.cart = []
