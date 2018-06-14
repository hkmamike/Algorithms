"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employeesMap = {e.id: e for e in employees}
        totalValue = 0
        pipeLine = [employeesMap[id]]
        
        while pipeLine:
            nextID = pipeLine.pop()
            totalValue += nextID.importance
            
            for sub in nextID.subordinates:
                pipeLine.append(employeesMap[sub])
            
        return totalValue