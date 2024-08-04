class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Inisialisasi array hasil perkalian kiri dan kanan
        left_products = [1] * n
        right_products = [1] * n

        # Hitung hasil perkalian kiri
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        # Hitung hasil perkalian kanan
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Hitung hasil perkalian array tanpa nums[i]
        result = [1] * n
        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        return result 