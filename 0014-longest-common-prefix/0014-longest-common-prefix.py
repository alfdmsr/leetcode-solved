class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        1. buat variabel array  
        2. buat perulangan untuk melakukan iterasi dan perbandingan 
        3. kembalikan hasil sesuai permintaan 
        """

        awalan = strs[0]
        for string in strs[1:]:
            while not string.startswith(awalan):
                awalan = awalan[:-1]
                if not awalan:
                    return ""
        return awalan


        