import matplotlib.pyplot as plt
import numpy as np 

thread_nums = [i for i in range(1, 16)]

mac_glic_malloc_small = [0] * 15
mac_glic_malloc_big = [0] * 15
mac_tcmalloc_small = [0] * 15
mac_tcmalloc_big = [0] * 15
mac_jemalloc_small = [0] * 15
mac_jemalloc_big = [0] * 15

linux_glic_malloc_small = [0] * 15
linux_glic_malloc_big = [0] * 15
linux_tcmalloc_small = [0] * 15
linux_tcmalloc_big = [0] * 15
linux_jemalloc_small = [0] * 15
linux_jemalloc_big = [0] * 15

with open('malloc测试.md', 'r') as f:
    lines = f.readlines()

mem_big = lines[2 : 17]
mem_small = lines[20 : 35]

i= 0
for big_line in mem_big:
    (_, mac_glic_malloc_big[i], mac_tcmalloc_big[i], mac_jemalloc_big[i],
        linux_glic_malloc_big[i], linux_tcmalloc_big[i], linux_jemalloc_big[i]
    ) = [int(item) for item in big_line.split()]
    i += 1

i= 0
for small_line in mem_small:
    (_, mac_glic_malloc_small[i], mac_tcmalloc_small[i], mac_jemalloc_small[i],
        linux_glic_malloc_small[i], linux_tcmalloc_small[i], linux_jemalloc_small[i]
    ) = [int(item) for item in small_line.split()]
    i += 1

s1, = plt.plot(thread_nums, linux_glic_malloc_small, 'r-+')
s2, = plt.plot(thread_nums, linux_tcmalloc_small, 'b-*')
s3, = plt.plot(thread_nums, linux_jemalloc_small, 'g-1')
plt.legend([s1, s2, s3], ['linux_glibc_malloc', 'linux_tcmalloc', 'linux_jemallocs'])
plt.xlabel('Thread Number')
plt.ylabel('Time/us')
plt.xlim((1, 15))

plt.show()