class Solution(object):
    def summaryRanges(self, nums):
        """
        1. buat variabel list kosong untuk menyimpan hasil
        2. buat variabel untuk menandai awal 
        3. iterasi memlalui setiap elemen dalam 'nums'
        4. Jika angka saat ini tidak berurutan dengan angka sebelumnya, tambahkan rentang tersebut ke dalam result dan mulai rentang baru.
        5. Setelah iterasi selesai, tambahkan rentang terakhir yang belum dimasukkan ke dalam result.
        6. Setiap rentang harus diformat sebagai string "a->b" jika terdiri dari lebih dari satu angka, atau "a" jika hanya satu angka.
        """
        result = []
        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i -1]:
                    result.append(str(start))
                else:
                    result.append("{}->{}".format(start, nums[i - 1]))
                start = nums[i]

        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, nums[-1]))

        return result 

        