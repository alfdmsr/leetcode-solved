class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # inisialisasi variabel set kosong
        result = set()

        # iterasi melalui string
        for char in nums:
            # periksa apakah ada duplikasi? jika ada kembalikan True
            if char in result:
                return True
            result.add(char)

        # kembalikan False jika tidak ada duplikasi
        return False
        