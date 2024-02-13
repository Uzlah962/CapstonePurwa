# Pertama, kita perlu mendefinisikan struktur data untuk menyimpan informasi tentang buku dan peminjaman. 
# Kita bisa menggunakan list of dictionary untuk ini. Setiap dictionary akan merepresentasikan satu buku atau peminjaman, 
# dengan key sebagai nama field dan value sebagai nilai field tersebut.
books = []  # List untuk menyimpan semua buku
borrowed_books = []  # List untuk menyimpan buku yang sedang dipinjam

# Kita akan membuat fungsi create_book yang meminta input dari pengguna dan menambahkan buku baru ke dalam list books.
def create_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan penulis buku: ")
    
    # Periksa apakah judul buku sudah ada
    for book in books:
        if book["title"] == title:
            print("Data sudah ada.")
            return
    
    # Jika judul buku belum ada, konfirmasi penambahan buku baru
    confirmation = input(f"Anda yakin ingin menambahkan buku '{title}' oleh {author}? (Y/N): ")
    if confirmation.lower() == 'y':
        # Tambahkan buku baru
        new_book = {"title": title, "author": author}
        books.append(new_book)
        print(f"Buku '{title}' telah ditambahkan.")
    else:
        print("Penambahan buku dibatalkan.")

# Kita akan membuat dua fungsi read_all_books dan read_specific_book untuk menampilkan semua buku atau buku spesifik berdasarkan judul.
def read_all_books():
    if not books:
        print("Tidak ada buku yang tersedia.")
    else:
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}")

def read_specific_book():
    title = input("Masukkan judul buku yang ingin dicari: ")
    found = False
    for book in books:
        if book["title"] == title:
            print(f"Judul: {book['title']}, Penulis: {book['author']}")
            found = True
            break
    if not found:
        print("Buku tidak ditemukan.")

# Kita akan membuat fungsi update_book yang memungkinkan pengguna untuk mengubah detail buku yang sudah ada.
def update_book():
    title = input("Masukkan judul buku yang ingin diubah: ")
    for i, book in enumerate(books):
        if book["title"] == title:
            print(f"Buku ditemukan. Detail saat ini:")
            print(f"Judul: {book['title']}, Penulis: {book['author']}")
            new_title = input("Masukkan judul baru (biarkan kosong jika tidak ingin diubah): ")
            new_author = input("Masukkan penulis baru (biarkan kosong jika tidak ingin diubah): ")
            
            # Konfirmasi perubahan
            confirmation = input("Apakah Anda yakin ingin mengubah detail buku? (Y/N): ")
            if confirmation.lower() == 'y':
                if new_title:
                    book["title"] = new_title
                if new_author:
                    book["author"] = new_author
                print("Detail buku telah diperbarui.")
                return
            else:
                print("Perubahan dibatalkan.")
                return
    print("Buku tidak ditemukan.")

# Kita akan membuat fungsi delete_book yang memungkinkan pengguna untuk menghapus buku dari daftar.
def delete_book():
    title = input("Masukkan judul buku yang ingin dihapus: ")
    for i, book in enumerate(books):
        if book["title"] == title:
            # Konfirmasi penghapusan
            confirmation = input(f"Anda yakin ingin menghapus buku '{title}'? (Y/N): ")
            if confirmation.lower() == 'y':
                del books[i]
                print("Buku telah dihapus.")
                return
            else:
                print("Penghapusan dibatalkan.")
                return
    print("Buku tidak ditemukan.")

# Setelah semua fungsi dibuat, kita bisa membuat menu utama yang memungkinkan pengguna untuk memilih operasi yang ingin dilakukan. Selain itu, 
# kita juga bisa memastikan bahwa kode tetap rapi dan mudah dibaca dengan mengorganisir fungsi-fungsi ini dalam class atau module.
def main():
    while True:
        print("\nMenu Perpustakaan Kelompok 5:")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Cari Buku Spesifik")
        print("4. Ubah Detail Buku")
        print("5. Hapus Buku")
        print("6. Keluar")
        choice = input("Pilih opsi: ")
        if choice == '1':
            create_book()
        elif choice == '2':
            read_all_books()
        elif choice == '3':
            read_specific_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()



