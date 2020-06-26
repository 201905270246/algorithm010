

def climbStairs(n):
    # res = [0] * (n+1)
    # res[0] = 1
    # res[1] = 2
    # for i in range(2, len(res)):
    #     res[i] = res[i - 1] + res[i - 2]
    # print(res)
    # return res[n-1]
    fst = 1
    scd = 2
    res = 0
    for i in range(2, n):
        res = fst + scd
        fst = scd
        scd = res
    return max(n, res)


print(climbStairs(2))
print(climbStairs(1))
print(climbStairs(3))
