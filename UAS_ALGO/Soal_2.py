import pandas as pd

data = {
    'Nama': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma dan Struktur Data': [90, 50, 65],
    'Matematika Numerik': [80, 60, 70]
}

df = pd.DataFrame(data)


rata_rata_mata_kuliah = df[['Algoritma dan Struktur Data', 'Matematika Numerik']].mean()
print("Rata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mata_kuliah)


print("\nRata-rata nilai untuk setiap mahasiswa:")
df['Rata-rata'] = df[['Algoritma dan Struktur Data', 'Matematika Numerik']].mean(axis=1)
print(df[['Nama', 'Rata-rata']])
