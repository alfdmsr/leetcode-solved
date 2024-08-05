class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # buat counter untuk menghitung frekuensi huruf
        input_count = Counter(s)
        output_count = Counter(t)

        # kembailkan hasil dari perbandingan kedua Counter tersebut
        return input_count == output_count 
        