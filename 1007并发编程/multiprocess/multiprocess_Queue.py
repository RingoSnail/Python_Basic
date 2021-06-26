from  multiprocessing import Process, Queue

# 使用队列实现进程间通信（IPC）
q = Queue(3)  # 队列项数，存放消息

q.put(1)
q.put(2)
q.put(3)
print(q.full())

print(q.get())
print(q.get())
print(q.get())
print(q.empty())