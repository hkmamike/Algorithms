class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        result = [0] * n
        stack = []

        for log in logs:
            id, event, timestamp = log.split(":")
            id = int(id)
            timestamp = int(timestamp)

            if event == "start":
                if stack:
                    result[stack[-1][0]] += timestamp - stack[-1][1]
                stack.append([id, timestamp])
            else:
                lastCallId, lastCallT = stack.pop()
                result[lastCallId] += timestamp - lastCallT + 1
                if stack:
                    stack[-1][1] = timestamp + 1
        
        return result

                