class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim             # public
        self.nama = nama           # public
        self._semester = semester  # protected
        self.__ipk = ipk           # private

    # Getter untuk protected
    def get_semester(self):
        return self._semester

    # Getter untuk private
    def get_ipk(self):
        return self.__ipk

    # Setter untuk protected
    def set_semester(self, smt):
        self._semester = smt

    # Setter untuk private
    def set_ipk(self, nilai):
        self.__ipk = nilai


# --- Membuat 2 objek mahasiswa ---
m1 = Mahasiswa("202412001", "Afan", 3, 3.7)
m2 = Mahasiswa("202412002", "Nesa", 5, 3.9)

# --- Menampilkan data awal ---
print("=== DATA MAHASISWA (AWAL) ===")
print("NIM :", m1.nim)
print("Nama :", m1.nama)
print("Semester :", m1.get_semester())
print("IPK :", m1.get_ipk())

print("\nNIM :", m2.nim)
print("Nama :", m2.nama)
print("Semester :", m2.get_semester())
print("IPK :", m2.get_ipk())

# --- Mengganti semester dan IPK ---
m1.set_semester(4)
m1.set_ipk(3.85)

m2.set_semester(6)
m2.set_ipk(3.95)

# --- Menampilkan data setelah diubah ---
print("\n=== DATA MAHASISWA (SETELAH DIUBAH) ===")
print("NIM :", m1.nim)
print("Nama :", m1.nama)
print("Semester :", m1.get_semester())
print("IPK :", m1.get_ipk())

print("\nNIM :", m2.nim)
print("Nama :", m2.nama)
print("Semester :", m2.get_semester())
print("IPK :", m2.get_ipk())
