"""
1. 解釋 stack 跟 queue 是什麼? 他們的差別是?
"""
print('Q1: stack 先進去的資料最後出來, queue 先進去的資料先出來')
"""
2. 實做一個queue class kqueue, 並提供 kqueue.push(), kqueue.pop(), kqueue.size(), kqueue.front(), kqueue.back() 的功能
"""

"""
3. 實做一個stack class kstack, 並提供 kstack.push(), kstack.pop(), kstack.size(), kstack.top() 的功能
"""

"""
4. 將上面兩個分別打包成 ktool 的 module
"""

"""
5. 分別使用 ktool 裡的 kqueue 及 kstack 對 [2,3,1,9,22,31,8,7,45,9] 由小到大做排序
"""
print('注：我突然發現根本就不需要 stack')

from ktool.kqueueTool import kqueue
from ktool.kstackTool import kstack
kq = kqueue()
ks = kstack()

numberlist=[2,3,1,9,22,31,8,7,45,9]


for n in numberlist:
    if not kq.size():
        kq.push(n)
    else:
        if kq.back() < n:
            kq.push(n)
        else:
            if kq.front()>n:
                kq.push(n)
                for q in range(0,kq.size()-1):
                    kq.push(kq.pop())
            else:
                for x in range(0,kq.size()):
                    if kq.front()<n:
                        kq.push(kq.pop())
                    else:
                        kq.push(n)
                        break
                while kq.front()>=kq.back():
                        kq.push(kq.pop())



