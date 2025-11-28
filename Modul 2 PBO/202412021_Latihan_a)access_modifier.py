
class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim             # public
        self.nama = nama           # public
        self._semester = semester  # protected
        self.__ipk = ipk           # private

    # Getter untuk protected
    def get_semester(self):
        return self._semester

    # Setter untuk protected
    def set_semester(self, smt):
        if smt <= 0:
            raise ValueError("Semester harus positif.")
        self._semester = smt

    # Getter untuk private
    def get_ipk(self):
        return self.__ipk

    # Setter untuk private
    def set_ipk(self, nilai):
        if not (0.0 <= nilai <= 4.0):
            raise ValueError("IPK harus 0.0 - 4.0")
        self.__ipk = round(nilai, 2)


# --- Contoh penggunaan ---
if __name__ == "__main__":
    m1 = Mahasiswa("202412032", "nesa", 3, 3.9)
    m2 = Mahasiswa("202412030", "sehun", 5, 3.8)

    print("=== Data Awal ===")
    print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())

    # Mengubah semester & IPK
    m1.set_semester(4)
    m1.set_ipk(3.5)

    m2.set_semester(6)
    m2.set_ipk(3.9)

    print("\n=== Data Setelah Diubah ===")
    print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
