# SmallProject
Some simple projects I completed at the ICT.

# 跨平台编程
使用预编译宏。
```
//windows
#ifdef _WIN32
    //windows 64
    #ifdef _WIN64
    #else
    #endif
#elif __APPLE__
#elif __linux__
#elif __unix__
#elif defined(_POSIX_VERSION)
#else
#endif
```
# Memory Pool (单线程内存池)
**接口**
```
class MemoryPool
{
 static const size_t PAGE_SIZE = 64*1024;
public:
 void* Allocate(size_t size, bool no_throw);
 void  Free(void*);
};
```
**reference**
[WINDOWS系统如何申请内存](https://docs.microsoft.com/en-us/windows/desktop/api/memoryapi/nf-memoryapi-virtualalloc)

[不同系统如何申请内存](https://docs.microsoft.com/en-us/windows/desktop/api/memoryapi/nf-memoryapi-virtualalloc)

**难点**
1. 如何实现跨平台。
2. 如何加快分配、释放速度。

**文献阅读**
[一种实时内存分配算法](http://wks.gii.upv.es/tlsf/files/ecrts04_tlsf_0.pdf)
* 几种常见的分配策略
    - Sequential Fit: 连续的单向，或者双向链表
    - Segregated Free Lists: 

# glibc ptmalloc
**几个问题**
1. Glibc在什么情况下不会将内存归还给操作系统、
2. Glibc的内存管理有哪些约束？适合怎样的内存分配场景
3. Glibc如何管理内存

**linux环境内存的使用**
linux系统中，存在两部分区域可以被申请映射使用，分别是Heap(堆)以及mmap映射区域。
其中，对Heap的操作，操作系统提供了`brk()`函数，C运行时，库提供了`sbrk()`函数。
对于mmap映射区操作，提供了`mmap()`以及`munmap()`函数。上述函数都可以i向进程添加额外
的虚拟内存。

brk(堆的当前最后地址)：`sbrk(intptr_t increment)`当`intptr_t increment`为0时，
返回进程当前的brk值。为正数是扩展brk值，为负数，收缩brk值。

Doug Lea Malloc: 分配程序加入索引，搜索速度快，合并未使用的区块。支持缓存，以便更快使用。
Glibc在内存回收上，做的不好，申请内存，然后释放，只有一小块没释放，也必须等待。极端情况下，会造成
几个G的浪费。

# jemalloc使用
**Advanced config**
* 使用xmalloc，能够返回异常


