from Soal_3 import Queue

def main():
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Tambah pesanan ")
        print("2. Hapus pesanan ")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            pesanan = input("Masukkan nama pesanan: ")
            queue.enqueue(pesanan)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.display()
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid")

main()
