# 加一
### 求解思路: 利用数组可遍历，字符串可拼接、可遍历特性。list -> str -> int -> str -> list
### 复杂度分析: 单层for循环，时间复杂度是O(n); 结果返回时新建数组，空间复杂度是O(n)
```
def plusOne(digits):
    j = ''
    for i in range(len(digits)):
        j += str(digits[i])
    return [int(i) for i in str(int(j) + 1)]
    
    
print(plusOne([1, 3, 4]))
print(plusOne([0]))
```

***
# 移动零
### 求解思路：利用双指针法，j记录不为零的元素位置;i遍历数组，遇到不为零的元素即与j交换；同时j指向下一个不为零的元素位置。
### 复杂度分析：单层for循环，时间复杂度为O(n);原地排序，空间复杂度为O(1)

```
def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums


print(moveZeroes([0, 0, 1, 2, 4]))
```
