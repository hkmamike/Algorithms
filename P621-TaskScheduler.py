class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        def defaultTime():
            return -101

        remainingTasks = len(tasks)
        taskTime = defaultdict(defaultTime)

        taskCnt = defaultdict(int)
        for task in tasks:
            taskCnt[task] += 1

        taskHeap = sorted([(-taskCnt[key], key) for key in taskCnt])

        currentTime = 0
        while remainingTasks > 0:
            for i in range(len(taskHeap)):
                task = taskHeap[i][1]
                taskCnt = -taskHeap[i][0]
                if currentTime - taskTime[task] >= (n+1) and taskCnt != 0:
                    remainingTasks -= 1
                    taskTime[task] = currentTime
                    taskCnt -= 1
                    taskHeap[i] = (-taskCnt, task)
                    taskHeap.sort()
                    break

            currentTime += 1

        return currentTime 