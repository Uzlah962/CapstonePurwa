import sys

# List untuk menyimpan semua buku
books = [
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

# List untuk menyimpan buku yang sedang dipinjam
borrowed_books = []  

# Fungsi untuk mencetak teks berwarna 
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[00m")

# Kita akan membuat fungsi create_book yang meminta input dari pengguna dan menambahkan buku baru ke dalam list books.
def create_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan penulis buku: ")
    
    # Periksa apakah judul buku sudah ada
    for book in books:
        if book["title"] == title:
            print_color("Data sudah ada.", "91")
            return
    
    # Jika judul buku belum ada, konfirmasi penambahan buku baru
    confirmation = input(f"Anda yakin ingin menambahkan buku '{title}' oleh {author}? (Y/N): ")
    if confirmation.lower() == 'y':
        # Tambahkan buku baru
        new_book = {"title": title, "author": author}
        books.append(new_book)
        print_color(f"Buku '{title}' telah ditambahkan.", "92")
    else:
        print_color("Penambahan buku dibatalkan.", "91")

# Kita akan membuat dua fungsi read_all_books dan read_specific_book untuk menampilkan semua buku atau buku spesifik berdasarkan judul.
def read_all_books():
    available_books = False
    print_color("Buku yang Tersedia:", "95")
    for book in books:
        print(f"Judul: {book['title']}, Penulis: {book['author']}")
        available_books = True

    if not available_books:
        print_color("Tidak ada buku yang tersedia.", "91")
    
    print_color("Buku yang Sedang Dipinjam:", "95")
    borrowed_books_found = False
    for book in borrowed_books:
        print_color(f"Judul: {book['title']} (Dipinjam), Penulis: {book['author']}", "91")
        borrowed_books_found = True
    
    if not borrowed_books_found:
        print_color("Tidak ada buku yang sedang dipinjam.", "91")


def read_specific_book():
    title = input("Masukkan judul buku yang ingin dicari: ")
    found = False
    for book in books:
        if book["title"] == title:
            if book in borrowed_books:
                print_color(f"Judul: {book['title']} (Dipinjam), Penulis: {book['author']}", "91")
            else:
                print(f"Judul: {book['title']}, Penulis: {book['author']}")
            found = True
            break
    if not found:
        print_color("Buku tidak ditemukan.", "91")

# Kita akan membuat fungsi update_book yang memungkinkan pengguna untuk mengubah detail buku yang sudah ada.
def update_book():
    title_input = input("Masukkan judul buku (minimal 3 huruf pertama): ")
    found = False
    for book in books:
        if book["title"].startswith(title_input):
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
                print_color("Detail buku telah diperbarui.", "92")
                return
            else:
                print_color("Perubahan dibatalkan.", "91")
                return
            found = True
            break
    if not found:
        print_color("Buku tidak ditemukan.", "91")

# Kita akan membuat fungsi delete_book yang memungkinkan pengguna untuk menghapus buku dari daftar.
def delete_book():
    title = input("Masukkan judul buku yang ingin dihapus: ")
    for i, book in enumerate(books):
        if book["title"] == title:
            # Konfirmasi penghapusan
            confirmation = input(f"Anda yakin ingin menghapus buku '{title}'? (Y/N): ")
            if confirmation.lower() == 'y':
                del books[i]
                print_color("Buku telah dihapus.", "91")
                return
            else:
                print_color("Penghapusan dibatalkan.", "92")
                return
    print_color("Buku tidak ditemukan.", "91")

def borrow_book():
    read_all_books()
    title = input("Masukkan judul buku yang ingin dipinjam: ")
    found = False
    for book in books:
        if book["title"].startswith(title):
            print_color(f"Judul: {book['title']}, Penulis: {book['author']}", "94")
            confirmation = input("Apakah Anda ingin meminjam buku ini? (Y/N): ")
            if confirmation.lower() == 'y':
                borrowed_books.append(book)
                books.remove(book)
                print_color(f"Buku '{book['title']}' telah berhasil dipinjam.", "92")
            else:
                print_color("Peminjaman buku dibatalkan.", "91")
            found = True
            break
    if not found:
        print_color("Buku tidak ditemukan.", "91")

def return_book():
    read_all_books()
    title = input("Masukkan judul buku yang ingin dikembalikan: ")
    found = False
    for book in borrowed_books:
        if book["title"].startswith(title):
            books.append(book)
            borrowed_books.remove(book)
            print_color(f"Buku '{book['title']}' telah berhasil dikembalikan.", "92")
            found = True
            break
    if not found:
        print_color("Buku tidak ditemukan atau belum dipinjam.", "91")


# Setelah semua fungsi dibuat, kita bisa membuat menu
def main():
    while True:
        print_color("\n=== Menu Perpustakaan ===", "95")
        print_color("1. Tambah Buku", "93")
        print_color("2. Lihat Semua Buku", "93")
        print_color("3. Cari Buku", "93")
        print_color("4. Ubah Detail Buku", "93")
        print_color("5. Hapus Buku", "93")
        print_color("6. Pinjam Buku", "93")
        print_color("7. Kembalikan Buku", "93")
        print_color("8. Keluar", "93")
        print_color("=" * 35, "92")
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
            borrow_book()
        elif choice == '7':
            return_book()
        elif choice == '8':
            print_color("Terima kasih telah menggunakan layanan perpustakaan.", "92")
            break
        else:
            print_color("Opsi tidak valid. Silakan coba lagi.", "91")

if __name__ == "__main__":
    main()



