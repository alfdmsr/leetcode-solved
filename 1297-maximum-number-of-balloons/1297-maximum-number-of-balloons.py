class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # buat counter untuk menghitung frekuensi huruf 
        string = Counter(text)
        
        # untuk membentuk kata "ballon" kita memerlukan setidaknya 
        # 1 "b"
        # 1 "a"
        # 2 "l"
        # 2 "0"
        # 1 "n"
        # kembalikan sesuai permintaan 
        return min(
            string['b'],
            string['a'],
            string['l'] // 2,
            string['o'] // 2,
            string['n']
        )