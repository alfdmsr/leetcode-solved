class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Urutkan interval
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        # Inisialisasi daftar hasil
        merged_intervals = []

        # lakukan iterasi melalui interval
        for interval in sorted_intervals:
            # Jika ada daftar hasil kosong atau tidak ada tumpang tindih
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # Jika ada tumpang tindih, gabungkan interval 
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        # kembalikan hasil sesuai permintaan 
        return merged_intervals

        
        
        