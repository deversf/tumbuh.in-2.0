import random

sayuran_nama = ["Selada", "Bayam", "Brokoli", "Kangkung", "Kubis", "Sawi", "Seledri"]
sayuran_ph_min = [6.0, 6.0, 6.0, 5.5, 6.5, 5.5, 6.5]
sayuran_ph_max = [7.0, 7.0, 6.8, 6.5, 7.0, 6.5, 6.5]
sayuran_ppm_min = [560, 1260, 1960, 1050, 1750, 1050, 1260]
sayuran_ppm_max = [840, 1610, 2450, 1400, 2100, 1400, 1680]

buah_nama = ["Cabe", "Tomat", "Timun", "Melon", "Nanas", "Semangka", "Stroberi"]
buah_ph_min = [6.0, 6.0, 5.5, 5.5, 5.5, 5.8, 6.0]
buah_ph_max = [6.5, 6.5, 5.5, 6.0, 6.0, 5.8, 6.0]
buah_ppm_min = [1260, 1400, 1190, 1400, 1400, 1260, 1260]
buah_ppm_max = [1540, 3500, 1750, 1750, 1680, 1680, 1540]

data_tanaman = {}
for i in range(len(sayuran_nama)):
    data_tanaman[sayuran_nama[i]] = ["Sayuran", sayuran_ph_min[i], sayuran_ph_max[i],
                                     sayuran_ppm_min[i], sayuran_ppm_max[i]]
for i in range(len(buah_nama)):
    data_tanaman[buah_nama[i]] = ["Buah", buah_ph_min[i], buah_ph_max[i],
                                  buah_ppm_min[i], buah_ppm_max[i]]

#data toko: nomor -> [nama, harga]
produk = {
    1: ["Benih", 15000],
    2: ["Nutrisi AB Mix", 35000],
    3: ["pH Meter", 65000],
    4: ["Rockwool", 12000],
    5: ["pH Up", 22000],
    6: ["pH Down", 22000],
}

metode_bayar = ["QRIS", "E-wallet", "Virtual Account", "Kartu debit/kredit", "Minimarket"]
daftar_ewallet = ["GoPay", "OVO", "DANA", "ShopeePay"]
daftar_bank = ["BCA", "BNI", "BRI", "Mandiri"]

#yang dapat berubah selama program berjalan
keranjang = {}                                   # nomor produk -> jumlah
kebun = {"tanaman": "Selada", "hari": 12}        # tanaman yang sedang ditanam
riwayat = [                                      # [tanaman, pH, ppm]
    ["Selada", 6.2, 780],
    ["Selada", 6.0, 800],
    ["Selada", 6.4, 820],
]


#fungsi bantu
def minta_angka(teks, minimum, maksimum):
    """Minta angka dari pengguna, ulangi terus sampai valid."""
    while True:
        try:
            angka = float(input(teks))
            if minimum <= angka <= maksimum:
                return angka
            else:
                print(f"❌ Nilai harus antara {minimum} sampai {maksimum}!")
        except ValueError:
            print("❌ Input harus berupa angka!")


def rupiah(angka):
    return "Rp" + format(int(angka), ",").replace(",", ".")


def cek_ph(ph, bawah, atas):
    if ph < bawah:
        return "Terlalu rendah"
    elif ph > atas:
        return "Terlalu tinggi"
    else:
        return "Normal"


def cek_ppm(ppm, bawah, atas):
    if ppm < bawah:
        return "Kurang"
    elif ppm > atas:
        return "Berlebih"
    else:
        return "Normal"


def hitung_total():
    total = 0
    for nomor in keranjang:
        total = total + produk[nomor][1] * keranjang[nomor]
    return total


def pilih_tanaman():
    """Pilih kategori, lalu pilih tanaman. Hasilnya: nama tanaman."""
    # VALIDASI KATEGORI TANAMAN
    while True:
        print("\nPilih Kategori:")
        print("1. Sayuran")
        print("2. Buah")
        try:
            pilih_kategori = int(input("\nMasukkan pilihan kategori (1/2): "))
            if pilih_kategori in [1, 2]:
                break
            else:
                print("❌ Pilihan tidak valid! Harap masukkan angka 1 atau 2.")
        except ValueError:
            print("❌ Input harus berupa angka (1 atau 2)!")

    if pilih_kategori == 1:
        nama_kategori = "Sayuran"
        daftar_nama = sayuran_nama
    else:
        nama_kategori = "Buah"
        daftar_nama = buah_nama

    # VALIDASI PILIHAN TANAMAN
    while True:
        print(f"\nPilih Jenis {nama_kategori}:")
        for i in range(len(daftar_nama)):
            print(f"{i + 1}. {daftar_nama[i]}")
        try:
            pilih = int(input("\nMasukkan pilihan tanaman (angka): "))
            if 1 <= pilih <= len(daftar_nama):
                return daftar_nama[pilih - 1]
            else:
                print(f"❌ Pilihan tidak valid! Masukkan angka antara 1 sampai {len(daftar_nama)}.")
        except ValueError:
            print("❌ Input harus berupa angka!")


#menu beranda
def beranda():
    print("\n=== BERANDA ===")
    print(f"Tanaman : {kebun['tanaman']} - hari ke-{kebun['hari']}")

    nama, ph, ppm = riwayat[-1]                  # data terakhir
    d = data_tanaman[nama]
    print(f"Data terakhir ({nama}):")
    print(f"pH   : {ph} ({cek_ph(ph, d[1], d[2])})")
    print(f"PPM  : {ppm} ({cek_ppm(ppm, d[3], d[4])})")
    print("Tugas hari ini: cek pH sore (16.00), tambah nutrisi A & B")


#menu panduan
def menu_panduan():
    print("\n=== PANDUAN TANAM ===")
    nama = pilih_tanaman()
    d = data_tanaman[nama] # [kategori, ph_min, ph_max, ppm_min, ppm_max]

    print(f"\nCara menanam {nama} ({d[0]}):")
    print("1. Semai benih (lembapkan rockwool, taruh di tempat teduh)")
    print("2. Pindah ke netpot (saat daun sejati muncul)")
    print(f"3. Atur nutrisi (pH {d[1]} - {d[2]}, PPM {d[3]} - {d[4]})")
    print("4. Perawatan harian (cek air, suhu, dan hama)")
    print("5. Penggantian larutan (setiap 7-10 hari)")
    print("6. Panen")

    jawab = input(f"\nMulai tanam {nama}? (y/n): ")
    if jawab == "y":
        kebun["tanaman"] = nama
        kebun["hari"] = 1
        print(f"Selamat menanam {nama}! Tanaman aktif diganti.")


#menu analisis data
def menu_input():
    print("\n=== INPUT DATA HARI INI ===")
    nama = pilih_tanaman()
    d = data_tanaman[nama]
    ph_bawah, ph_atas = d[1], d[2]
    ppm_bawah, ppm_atas = d[3], d[4]
    print("\nTanaman Dipilih :", nama)

    print("\n=== INPUT HASIL PENGUKURAN ===")
    ph = minta_angka("Masukkan pH Air : ", 0, 14)
    ppm = int(minta_angka("Masukkan ppm Air : ", 0, 100000))

    print("\n=== HASIL ANALISIS ===")
    status_ph = cek_ph(ph, ph_bawah, ph_atas)
    status_ppm = cek_ppm(ppm, ppm_bawah, ppm_atas)
    print(f"pH   : {ph} - {status_ph} (normal {ph_bawah} - {ph_atas})")
    print(f"PPM  : {ppm} - {status_ppm} (normal {ppm_bawah} - {ppm_atas})")

    rekomendasi = []                  # nomor produk yang disarankan
    if status_ph == "Terlalu rendah":
        rekomendasi.append(5)         # pH Up
    if status_ph == "Terlalu tinggi":
        rekomendasi.append(6)         # pH Down
    if status_ppm == "Kurang":
        rekomendasi.append(2)         # Nutrisi AB Mix

    if status_ph == "Normal" and status_ppm == "Normal":
        print("\n🌱 Kondisi tanaman baik dan sesuai parameter ideal.")
    else:
        print("\n⚠️ Ada parameter yang tidak sesuai!")
        if status_ppm == "Berlebih":
            print("💡 Saran: tambahkan air bersih untuk mengencerkan nutrisi.")
        if len(rekomendasi) > 0:
            print("💡 Produk yang membantu:")
            for nomor in rekomendasi:
                print("   -", produk[nomor][0], rupiah(produk[nomor][1]))
            jawab = input("Masukkan ke keranjang? (y/n): ")
            if jawab == "y":
                for nomor in rekomendasi:
                    keranjang[nomor] = keranjang.get(nomor, 0) + 1
                print("Sudah masuk keranjang. Buka menu Toko untuk membayar.")

    simpan = input("\nSimpan ke riwayat? (y/n): ")
    if simpan == "y":
        riwayat.append([nama, ph, ppm])
        print("Tersimpan.")


#menu toko
def menu_toko():
    nomor_bayar = len(produk) + 1
    while True:
        print("\n=== TOKO ===")
        for nomor in produk:
            print(f"{nomor} - {produk[nomor][0]} {rupiah(produk[nomor][1])}")
        print(f"{nomor_bayar} - Lihat keranjang & bayar")
        print("0 - Kembali")
        pilih = int(minta_angka("Pilih: ", 0, nomor_bayar))

        if pilih == 0:
            break
        elif pilih in produk:
            jumlah = int(minta_angka("Jumlah: ", 1, 99))
            keranjang[pilih] = keranjang.get(pilih, 0) + jumlah
            print(produk[pilih][0], "ditambahkan ke keranjang.")
        else:
            bayar()


def bayar():
    if len(keranjang) == 0:
        print("Keranjang masih kosong.")
        return

    print("\n--- Keranjang ---")
    for nomor in keranjang:
        print(f"{produk[nomor][0]} x {keranjang[nomor]} = {rupiah(produk[nomor][1] * keranjang[nomor])}")
    print("Total:", rupiah(hitung_total()))

    alamat = input("Alamat pengiriman: ")

    while True: # ulangi jika pembayaran gagal
        print("\nMetode pembayaran:")
        for i in range(len(metode_bayar)):
            print(f"{i + 1} - {metode_bayar[i]}")
        pilih = int(minta_angka("Pilih metode: ", 1, len(metode_bayar)))
        metode = metode_bayar[pilih - 1]

        if metode == "QRIS":
            print("Pindai kode QR ini dengan aplikasi bank/e-wallet: TB-" + str(random.randint(1000, 9999)))
        elif metode == "E-wallet":
            for i in range(len(daftar_ewallet)):
                print(f"{i + 1} - {daftar_ewallet[i]}")
            w = int(minta_angka("Pilih e-wallet: ", 1, len(daftar_ewallet)))
            print(f"Buka aplikasi {daftar_ewallet[w - 1]} dan konfirmasi pembayaran.")
        elif metode == "Virtual Account":
            for i in range(len(daftar_bank)):
                print(f"{i + 1} - {daftar_bank[i]}")
            b = int(minta_angka("Pilih bank: ", 1, len(daftar_bank)))
            print(f"Transfer ke VA {daftar_bank[b - 1]}: {random.randint(10**9, 10**10 - 1)}")
        elif metode == "Kartu debit/kredit":
            print("Isi data kartu lalu verifikasi OTP (simulasi).")
        else:
            print(f"Kode bayar: {random.randint(10**11, 10**12 - 1)} - bayar di kasir minimarket.")

        hasil = input("Pembayaran berhasil? (y/n): ")      # simulasi
        if hasil == "y":
            print("\n✅ Pesanan dikonfirmasi! Dikirim ke:", alamat)
            keranjang.clear()
            break
        else:
            print("❌ Pembayaran gagal.")
            ulang = input("Coba lagi / ganti metode? (y/n): ")
            if ulang != "y":
                print("Pesanan dibatalkan.")
                break


#program utama
print("================================")
print("        tumbuh.in 🌱          ")
print(" Monitoring Nutrisi Hidroponik")
print("================================")

while True:
    print("\n===== MENU UTAMA =====")
    print("1. Beranda")
    print("2. Panduan Tanam")
    print("3. Input Data & Analisis")
    print("4. Toko")
    print("0. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        beranda()
    elif menu == "2":
        menu_panduan()
    elif menu == "3":
        menu_input()
    elif menu == "4":
        menu_toko()
    elif menu == "0":
        print("\nTerima kasih telah menggunakan tumbuh.in 🌱!")
        break
    else:
        print("Menu tidak ada.")