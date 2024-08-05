class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # hitung frekuensi karakter
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        # periksa apakah ada karakter 
        for char, count in ransomNote_counter.items():
            if magazine_counter[char] < count:
                return False

        return True