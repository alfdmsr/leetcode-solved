class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        1. buat variabel array penampung
        2. buat variabel untuk iterasi loop
        3. tambahkan karakter secara bergantian
        4. tambahkan jika ada sisa 
        5. gabung dan kembalikan sesuai permintaan 
        """
        gabung = []
        i, j = 0,0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                gabung.append(word1[i])
                i += 1
            if j < len(word2):
                gabung.append(word2[j])
                j += 1
        return ''.join(gabung)
        