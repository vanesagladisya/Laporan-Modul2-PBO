class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul          # public
        self.penulis = penulis      # public
        self.kode_buku = kode_buku  # public
        self._stok = stok           # protected
        self.__lokasi_rak = lokasi_rak  # private

    # Getter lokasi rak (private)
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    # Setter lokasi rak (private)
    def set_lokasi_rak(self, lokasi):
        if lokasi == "":
            raise ValueError("Lokasi tidak boleh kosong")
        self.__lokasi_rak = lokasi

    # Tambah stok
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    # Kurangi stok
    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
        else:
            raise ValueError("Stok tidak cukup!")

    def info_buku(self):
        return f"{self.judul} ({self.kode_buku}) - Stok: {self._stok}, Rak: {self.__lokasi_rak}"


# ============================
#   CLASS PEMINJAMAN (Association)
# ============================
class Peminjaman:
    def __init__(self, buku: Buku, tanggal_pinjam, tanggal_kembali=None, status="Dipinjam"):
        self.buku = buku                      # association
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return (
            f"Buku: {self.buku.judul} | Kode: {self.buku.kode_buku} | "
            f"Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"
        )


# ============================
#   CLASS ANGGOTA (Aggregation)
# ============================
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam, status_aktif=True):
        self.id_anggota = id_anggota      # public
        self.nama = nama                  # public
        self._maks_pinjam = maks_pinjam   # protected
        self.__status_aktif = status_aktif  # private
        self.daftar_peminjaman = []         # aggregation

    # Getter status
    def get_status(self):
        return self.__status_aktif

    # Setter status
    def set_status(self, status):
        self.__status_aktif = status

    # Pinjam buku
    def pinjam_buku(self, buku: Buku, tanggal_pinjam):
        if not self.__status_aktif:
            print(f"Anggota {self.nama} tidak aktif!")
            return

        if buku._stok <= 0:
            print(f"Stok habis untuk buku: {buku.judul}")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Melebihi batas maksimal pinjam!")
            return

        # Kurangi stok buku
        buku.kurangi_stok(1)

        # Buat objek peminjaman
        pem = Peminjaman(buku, tanggal_pinjam)
        self.daftar_peminjaman.append(pem)

    # Kembalikan buku
    def kembalikan_buku(self, kode_buku, tanggal_kembali):
        for pem in self.daftar_peminjaman:
            if pem.buku.kode_buku == kode_buku and pem.status == "Dipinjam":
                pem.status = "Dikembalikan"
                pem.tanggal_kembali = tanggal_kembali
                pem.buku.tambah_stok(1)
                return
        print("Tidak ditemukan peminjaman buku tersebut.")


# ============================
#   CLASS PERPUSTAKAAN (Composition)
# ============================
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []  # composition

    def tambah_buku(self, buku: Buku):
        self.daftar_buku.append(buku)

    def info_buku(self):
        for b in self.daftar_buku:
            print(b.info_buku())


# =========================================================
#                    BAGIAN UTAMA PROGRAM
# =========================================================
if __name__ == "__main__":
    # === 3 Buku ===
    buku1 = Buku("Algoritma", "Darmawan", "B001", 3, "Rak A")
    buku2 = Buku("Python Dasar", "Suryo", "B002", 2, "Rak B")
    buku3 = Buku("Basis Data", "Hadi", "B003", 5, "Rak C")

    # Perpustakaan
    perpus = Perpustakaan("Perpus PBO")
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)
    perpus.tambah_buku(buku3)

    # === 2 Anggota === (nama diganti)
    a1 = Anggota("A01", "Vanesa", maks_pinjam=3)
    a2 = Anggota("A02", "Sehun", maks_pinjam=2)

    # === Anggota 1 pinjam 2 buku ===
    a1.pinjam_buku(buku1, "2024-12-01")
    a1.pinjam_buku(buku2, "2024-12-01")

    # === Anggota 2 pinjam 1 buku ===
    a2.pinjam_buku(buku3, "2024-12-02")

    # === Pengembalian buku ===
    a1.kembalikan_buku("B002", "2024-12-05")

    # =======================================================
    #                      OUTPUT PROGRAM
    # =======================================================
    print("\n=== INFORMASI BUKU ===")
    perpus.info_buku()

    print("\n=== INFORMASI ANGGOTA ===")
    print(f"{a1.id_anggota} - {a1.nama} - Status: {a1.get_status()}")
    print(f"{a2.id_anggota} - {a2.nama} - Status: {a2.get_status()}")

    print("\n=== DAFTAR PEMINJAMAN ANGGOTA 1 ===")
    for p in a1.daftar_peminjaman:
        print("-", p.info_peminjaman())

    print("\n=== DAFTAR PEMINJAMAN ANGGOTA 2 ===")
    for p in a2.daftar_peminjaman:
        print("-", p.info_peminjaman())
