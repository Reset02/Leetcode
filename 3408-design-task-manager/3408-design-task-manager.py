class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {} # taskId -> (userId, priority)
        self.heap = [] # max-heap (store as min-heap with negative values)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            self.task_map[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, neg_taskId, userId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                cur_userId, cur_priority = self.task_map[taskId]
                if cur_priority == -priority:  # still valid
                    del self.task_map[taskId]
                    return cur_userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()