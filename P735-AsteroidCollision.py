class Solution:
    def asteroidCollision(self, asteroids):

        stack = []
        index = 0
        
        while index < len(asteroids):
            if not stack or stack[-1] < 0 or asteroids[index] > 0:
                stack.append(asteroids[index])
                index += 1
            elif stack[-1] == abs(asteroids[index]):
                stack.pop()
                index += 1
            elif stack[-1] > abs(asteroids[index]):
                index += 1
            else:
                stack.pop()
                
        return stack