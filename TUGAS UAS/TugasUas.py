# Minta input data customer
nama = input("Masukkan nama customer: ")
tanggal_belanja = input("Masukkan tanggal belanja (YYYY-MM-DD): ")

# Simpan data customer ke tuple
data_customer = (nama, tanggal_belanja)

# Minta jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# List untuk menampung dictionary barang
daftar_belanja = []  # Ini array/list of dict

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}")
    barang_nama = input("Nama barang: ")
    harga_satuan = int(input("Harga satuan: "))
    qty = int(input("Jumlah (qty): "))
    
    # Simpan data barang ke dictionary
    barang = {
        "nama": barang_nama,
        "harga_satuan": harga_satuan,
        "qty": qty,
        "subtotal": harga_satuan * qty
    }
    
    # Tambahkan dictionary barang ke list array
    daftar_belanja.append(barang)

# Hitung total belanja
total_belanja = sum(item["subtotal"] for item in daftar_belanja)

# Cetak output
print("\nData customer :")
print(f"Nama : {data_customer[0]}")
print(f"Tanggal belanja : {data_customer[1]}")
print("Daftar belanja :")

for idx, item in enumerate(daftar_belanja, start=1):
    print(f"{idx}. {item['nama']} - harga satuan : {item['harga_satuan']}, qty {item['qty']}")

print(f"Total belanja : Rp {total_belanja:,}".replace(",", "."))

