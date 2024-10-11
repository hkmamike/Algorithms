class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.result = []
        
        def backtrack(index, path, value, last_operand):
            # Base case: if we have processed the entire string
            if index == len(num):
                # If the expression evaluates to the target, add it to the result
                if value == target:
                    self.result.append(path)
                return
            
            # Try all possible lengths of the next operand
            for i in range(index, len(num)):
                # Extract the current substring as the next operand
                current_str = num[index:i+1]
                
                # Prevent operands with leading zeros
                if len(current_str) > 1 and current_str[0] == '0':
                    break
                
                current_operand = int(current_str)
                
                # If at the start of the expression, just take the current number
                if index == 0:
                    backtrack(i + 1, current_str, current_operand, current_operand)
                else:
                    # Addition
                    backtrack(i + 1, path + "+" + current_str, value + current_operand, current_operand)
                    
                    # Subtraction
                    backtrack(i + 1, path + "-" + current_str, value - current_operand, -current_operand)
                    
                    # Multiplication
                    backtrack(i + 1, path + "*" + current_str, value - last_operand + (last_operand * current_operand), last_operand * current_operand)
        
        # Start the backtracking process
        backtrack(0, "", 0, 0)
        return self.result