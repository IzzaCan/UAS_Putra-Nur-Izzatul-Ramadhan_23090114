class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def set_nama(self, nama):
        self.nama = nama

    def set_warna(self, warna):
        self.warna = warna

    def set_rasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Buah {self.nama} memiliki warna {self.warna} dan rasanya {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def set_vitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        return f"Mangga {self.nama} memiliki warna {self.warna}, rasanya {self.rasa}, dan mengandung vitamin {self.vitamin}"

mangga1 = Mangga("Mangga enak ", "keorenan ", "Manis", "C dan A")

print("Nama mangga:", mangga1.nama)
print("Warna mangga:", mangga1.warna)
print("Rasa mangga:", mangga1.rasa)
print("Vitamin mangga:", mangga1.vitamin)
print(mangga1.information())
