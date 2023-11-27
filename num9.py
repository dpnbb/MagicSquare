import numpy as np


# TODO 多进程计算
def backtrack(nums, path, res):
    pathlen = len(path)
    # 同质剪枝
    # 首行判断
    if 2 <= pathlen <= 4 or 18 <= pathlen <= 20:
        if path[pathlen - 1] < path[pathlen - 2]:
            return

    # 首列判断
    if pathlen % 4 == 1:
        if pathlen != 1 and pathlen != 17:
            if path[pathlen - 1] < path[pathlen - 5]:
                return

    # 转置同质剪枝
    if pathlen == 5 or pathlen == 21:
        if path[pathlen - 1] < path[pathlen - 4]:
            return

    # 第二个矩阵左上角取最小值
    if pathlen == 17:
        if np.min(np.array(nums)) < path[pathlen - 1]:
            return

    # 第四列可直接减出来
    # 检查行
    if pathlen % 4 == 3:
        rowSum = np.sum(np.array(path)[pathlen - 3:pathlen])
        index = np.where(nums == 69 - rowSum)
        if len(index[0]) == 0:
            return
        else:
            if pathlen != 15:
                i = index[0][0]
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)
            else:
                i = index[0][0]
                if np.sum(np.array(path)) + nums[i] == 276:
                    backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)
    # 第四行可直接减出来
    # 检查列
    elif 12 <= pathlen <= 15 or 28 <= pathlen <= 31:
        # martix = np.array(path).reshape(-1, 4)
        col = path[pathlen - 12::4]
        # colSum = np.sum(col)
        index = np.where(nums == 69 - np.sum(col))
        if len(index[0]) == 0:
            return
        else:
            i = index[0][0]
            backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)
        # print(col)
    elif not nums:
        res.append(path)
        print(path)
        return
    else:
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)


res = []
nums = list(range(2, 34))
nums.remove(9)

print(nums)
# 同质 1 开头即可
backtrack(nums, [1], res)
print(res)
