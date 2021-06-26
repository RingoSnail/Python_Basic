import queue

# FIFO队列
# q = queue.Queue()
# LIFO堆栈
# q = queue.LifoQueue()
# q.put("first")
# q.put("second")
# q.put("third")

# 优先级队列
q = queue.PriorityQueue()
q.put((2, "a"))
q.put((1, "b"))
q.put((0, "c"))

print(q.get())
print(q.get())
print(q.get())