class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]

        for g in gain:
            newAltitude = altitudes[-1] + g
            altitudes.append(newAltitude)

        return max(altitudes)
