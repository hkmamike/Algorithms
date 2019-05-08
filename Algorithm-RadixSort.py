def radixSort(self, num):
        for i in range(32):
            big = []
            small = []
            needle = 1 << i
            for val in num:
                if val & needle != 0:
                    big.append(val)
                else:
                    small.append(val)

            num = []
            num += small
            num += big

        return num