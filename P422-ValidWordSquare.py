class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        words = [list(row) for row in words]
        return words == [*map(list, zip(*words))]