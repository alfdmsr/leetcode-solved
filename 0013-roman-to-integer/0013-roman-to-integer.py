class Solution(object):
    def romanToInt(self, s):
        """
        1. buat dictionary untuk menyimpan mapping antara simbol roman dan nilai integernya
        2. buat variabel untuk mengiterasi karater dalam angka roman 
        3. buat fungsi untuk mengecek karakter berikutnya, apakah lebih besar atau lebih kecil sehingga apakah perlu dikurangkan atau ditambahkan
        4. hitunglah nilainya dan kembalikan hasilnya sesuai permintaan 
        """
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        hasil = 0
        nilaiSebelumnya = 0

        for i in range(len(s) - 1, -1, -1):
            nilaiSaatIni = roman_to_int[s[i]]
            if nilaiSaatIni >= nilaiSebelumnya:
                hasil += nilaiSaatIni
            else:
                hasil -= nilaiSaatIni
            nilaiSebelumnya = nilaiSaatIni
        return hasil 
        