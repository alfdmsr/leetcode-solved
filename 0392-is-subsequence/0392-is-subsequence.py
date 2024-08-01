class Solution(object):
    def isSubsequence(self, s, t):
        """
        1. buat variabel untuk inisialisasi penanda  
        2. buat looping untuk iterasi melalui string s dan lakukan pengecekan pada string t
        3. kembalikan hasil sesuai permintaan 
        """
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
        