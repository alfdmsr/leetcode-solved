class Solution(object):
    def maxProfit(self, prices):
        """
        1. buat variabel untuk menyimpan harga minimum, profit maksimum dan hasil akhir
        2. buat loop untuk melakukan iterasi array harga
        3. update harga minimum dan profit 
        4. kembalikan profit maksimum 
        """
        min_price = float('inf')
        max_profit = 0
       
        for price in prices:
            min_price = min(min_price, price)

            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit 
        