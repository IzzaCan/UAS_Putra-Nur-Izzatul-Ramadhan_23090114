class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan '{item}' telah ditambahkan ke antrian.")

    def dequeue(self):
        if self.items:
            removed_item = self.items.pop(0)
            print(f"Pesanan '{removed_item}' telah dihapus dari antrian.")
            return removed_item
        else:
            print("Antrian kosong, tidak ada pesanan untuk dihapus.")
            return None

    def display(self):
        if self.items:
            print("Daftar antrian pesanan:")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")
        else:
            print("Antrian kosong.")
