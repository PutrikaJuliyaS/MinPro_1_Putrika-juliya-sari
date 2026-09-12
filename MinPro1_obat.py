#list atau tuple
stok_obat = [
    # Pereda nyeri dan demam
    ("pereda nyeri dan demam","paracetamol", 20),
    ("pereda nyeri dan demam","ibuprofen", 10),
    ("pereda nyeri dan demam","aspirin", 10),
    
    # Batuk dan flu
    ("batuk dan flu", "Guaifenesin", 10),
    ("batuk dan flu", "Dextromethorphan", 5),
    
    # Alergi
    ("alergi", "Cetirizine", 15),
    ("alergi", "CTM", 20),
    
    # Vitamin
    ("vitamin", "Vitamin c", 12),
    ("vitamin", "Vitamin b complex", 22),
    ("vitamin", "Multivitamin", 20)
]

#Program berbentuk menu pilihan berulang (while)
while True:
    print("1. tampilkan semua stok obat")
    print("2. tambah obat baru")
    print("3. ubah jumlah stok")
    
    pilihan = input("pilih nomor (1-3): ")

#conditional statement
    if pilihan == "1":
        print("DAFTAR STOK OBAT")
        for obat in stok_obat:
            kategori, nama_obat, jumlah_stok = obat
            print("kategori:", kategori)
            print("nama obat:", nama_obat, jumlah_stok, "pcs")
            print()

#Menambahkan data baru
    elif pilihan == "2":
        print("MENAMBAH OBAT BARU")
        kategori = input("masukkan kategori obat: ")
        nama_obat = input("masukkan nama obat: ")
        jumlah_stok = int(input("masukkan jumlah stok obat: "))
        stok_obat.append((kategori, nama_obat, jumlah_stok))
        print("obat berhasil ditambahkan ke kategori.")

#Mengubah data yang sudah ada
    elif pilihan == "3":
        print("MENGUBAH JUMLAH STOK OBAT")
        kategori = input("masukkan kategori obat: ")
        nama_obat = input("masukkan nama obat: ")
        jumlah_stok = int(input("masukkan jumlah stok baru: "))
        print("stok obat berhasil diubah.")


#input salah diminta ulang, bukan error/crash
    else:
        print("input tidak valid, silahkan masukkan pilihan yang benar")