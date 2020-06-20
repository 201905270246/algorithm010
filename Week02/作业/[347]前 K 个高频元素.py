# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表
import collections
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        思路：
        1. 构建hash map: 遍历数组，构建key为元素，value为元素出现频率的字典.
        2. 构建规模为k的小顶堆
        3. 遍历剩余元素，大于堆顶元素的入堆，不断下沉
        :param nums:
        :param k:
        :return:
        """
        # 遍历nums，构建字典{'ele':count}，并将其转换成元素为元组的数组
        freq_count = {}
        for num in nums:
            if num in freq_count:
                freq_count[num] += 1
            else:
                freq_count[num] = 0
        freq_list = list(freq_count.items())

        def sift_up(arr, k):
            new_val = arr[k]
            while k > 0 and arr[(k - 1) // 2][1] > new_val[1]:
                arr[k] = arr[(k - 1) // 2]
                k = (k - 1) // 2
            arr[k] = new_val

        def sift_down(arr, root, k):
            root_val = arr[root]
            while root * 2 + 1 < k:
                child = root * 2 + 1
                if child + 1 < k and arr[child + 1][1] < arr[child][1]:
                    child += 1
                if arr[child][1] < root_val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = root_val

        # 取前k个的数组元素，构建小顶堆，不断上浮
        min_heap = []
        for i in range(k):
            min_heap.append(freq_list[i])
            sift_up(min_heap, i)

        # 遍历剩余(k+1, N)的数组元素，插入小顶堆，维护小顶堆，不断下沉
        for item in freq_list[k:]:
            if min_heap[0][1] < item[1]:
                min_heap[0] = item
                sift_down(min_heap, 0, k)
        return [item[0] for item in min_heap]

# leetcode submit region end(Prohibit modification and deletion)
