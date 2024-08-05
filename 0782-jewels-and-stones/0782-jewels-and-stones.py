class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # buat set dari variabel jewels
        jewels_set = set(jewels)

        # iterasi melalui stones dan hitung jumlah permata 
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1

        # kembalikan hasil 
        return count
        