class Solution:
    def stringSequence(self, target: str) -> List[str]:
        
        result = ["a"]
        idx = 0
        screen = ["a"]

        while "".join(screen) != target:
            if screen[idx] != target[idx]:
                charOrder = ord(screen[idx])
                screen[idx] = chr(charOrder + 1)
            else:
                screen.append("a")
                idx += 1
            result.append("".join(screen))
        return result
