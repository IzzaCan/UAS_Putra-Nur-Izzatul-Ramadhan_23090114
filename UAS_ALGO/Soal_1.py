def tambah_data_mahasiswa():
    data_mahasiswa = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")

        data_mahasiswa.append({'NIM': nim, 'Nama': nama})

        lanjut = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
        if lanjut != 'ya':
            break

    return data_mahasiswa

def tampilkan_data_mahasiswa(data_mahasiswa):
    print("\nData Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")

def main():
    data_mahasiswa = tambah_data_mahasiswa()
    tampilkan_data_mahasiswa(data_mahasiswa)

main()
