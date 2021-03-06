**位运算**

_位运算符:_<br>
左移:<<:0110 -> 1100<br/>
右移:>>:0110 -> 0011<br>
按位或:|:两者之间有一个为1，结果为1，否则为0. 0011｜1011 -> 1011<br>
按位与:&:两者之间有一个为0，结果为0，否则为1. 0011 & 1011 -> 0011<br>
按位取反:~: 0011 -> 1100<br>
按位异或:^:两者相同为0，不同为1。0011^1011 -> 1000<br>

异或操作的特点：<br>
x^全0 = x <br>
x^全1 = ~x <br>
x^(~x) = 全1 <br>
x^x = 0      <br>
c=a^b -> a^c=b, b^c=a //交换两个数   <br>
a^b^c=a^(b^c)=(a^b)^c //associative  <br>

指定位置的位运算：<br>
将x最右边的n位清零： x&(~0<<n) <br>
获取x的第n位值（0或1）：（x>>n）&1  <br>
获取x的第n位的幂值：x&(1<<n) <br>
仅将第n位置为1：x|(1<<n) <br>
仅将第n位置为0：x&(~(1<<n))<br>
将x最高位至第n位（含）清零：x&((1<<n)-1)<br>

**实战位运算要点：<br>**
判断奇偶：<br>
x % 2 == 1 -> (x & 1) == 1 <br>
x % 2 == 0 -> (x & 1) == 0 <br>

x >> 1 -> x/2 <br>
x = x / 2 -> x = x >> 1 <br>
mid = (left + right) / 2 -> mid = (left + right) >> 1  <br>

X = X & (X - 1) 清零最低位的1

X & -X -> 得到最低位的1

X & ~X -> 0


**布隆过滤器（bloom filter）**
布隆过滤器是一个很长的二进制向量和一系列随机映射函数，用于检索一个元素是否在一个集合中。<br><br>
优点：查询时间复杂度和空间复杂度低于一般算法<br>
缺点：有一定的误识别率和删除困难<br>

布隆过滤器常用于大型的分布式系统，在真正的数据库查询前的快速查询的缓存：因为当一个元素映射到的二进制位，有一个为0，则该元素肯定不在布隆过滤器的索引中且不存在与集合中；但是全为1，该元素在布隆过滤器的索引中，但不一定存在集合中。<br>

**LRU Cache**
要素：大小，替换策略<br>
实现：Hash Table + Double LinkedList<br>
O(1)查询<br>
O(1)修改、更新<br>
更新原则：最近被使用的移到前面；所以最近的放在前面，最少使用/最久时间的放在后面；满了之后：添加新的到前面，并移除后面的；添加已有的元素，则已有的元素移到前面，其他元素位置不变。<br>

替换策略：<br>
LFU-least frequently used：每个元素被使用的频次最少的最先被淘汰出去<br>
LRU-least recently used：最少最近被使用的元素被淘汰出去<br>


**排序算法**
1.比较类排序：<br>
1.1交换排序<br>
1.1.1冒泡排序：时间复杂度O(n^2)<br>
嵌套排序，每次查看相邻元素。如果逆序，则交换。<br>
**1.1.2快速排序**：时间复杂度O(nlogn)<br>
分治思想：数组取标杆pivot，将小元素放pivot左边，大元素放右边，对左右两边递归调用快排；以达到整个序列有序。<br>
1.2插入排序<br>
1.2.1简单插入排序：时间复杂度O(n^2)<br>
从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入<br>
1.2.2希尔排序<br>

1.3选择排序：<br>
1.3.1简单选择排序：时间复杂度O(n^2)<br>
每次找最小值，然后放到待排序数组的起始位置<br>
**1.3.2堆排序**：时间复杂度O(nlogn)<br>
堆插入时间复杂度O(logN)，取最大/小值O(1)<br>
数组元素依次建立小/大顶堆，依次取堆顶元素，并删除。

**1.4归并排序**<br>
1.4.1二路归并排序：时间复杂度O(nlogn)<br>
分治思想：把长度为n的输入序列分成两个长度为n/2的子序列；对这两个子序列分别采用归并排序；将两个排序好的子序列合并成一个最终的排序序列
1.4.2多路归并排序<br>

2.非比较类排序：整型<br>
2.1计数排序:时间复杂度O(n+k)<br>
2.2桶排序:时间复杂度O(n+k)<br>
2.3基数排序:时间复杂度O(nXk)<br>
重点掌握：时间复杂度O(nlogn)的堆排序，快速排序，归并排序<br>

