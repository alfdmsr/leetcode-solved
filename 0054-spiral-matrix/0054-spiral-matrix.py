class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Inisialisasi batasan
        a = len(matrix) # jumlah baris 
        b = len(matrix[0]) # jumlah kolom

        atas = 0
        bawah = a - 1
        kiri = 0
        kanan = b - 1

        result = []
        # lakukan iterasi dan kumpulkan elemen
        while atas <= bawah and kiri <= kanan:
            # iterasi dari kiri ke kanan sepanjang batas atas
            for i in range(kiri, kanan + 1):
                result.append(matrix[atas][i])
            atas += 1

            # iterasi dari atas ke bawah sepanjang kanan
            for i in range(atas, bawah + 1):
                result.append(matrix[i][kanan])
            kanan -= 1

            if atas <= bawah:
                # iterasi dari kanan ke kiri sepanjang batas bawah 
                for i in range(kanan, kiri -1, -1):
                    result.append(matrix[bawah][i])
                bawah -= 1

            if kiri <= kanan:
                # iterasi dari bawah ke atas sepanjang batas kiri
                for i in range(bawah, atas - 1, -1):
                    result.append(matrix[i][kiri])
                kiri += 1

        # kembalikan hasil sesuai permintaan 
        return result 




        