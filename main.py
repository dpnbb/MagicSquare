import numpy as np


# TODO 多进程计算
def backtrack(nums, path, res):
    pathlen = len(path)
    # 第四列可直接减出来
    # 检查行
    if pathlen % 4 == 3:
        rowSum = np.sum(np.array(path)[pathlen - 3:pathlen])
        index = np.where(nums == 66 - rowSum)
        if len(index[0]) == 0:
            return
        else:
            if pathlen != 15:
                i = index[0][0]
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)
            else:
                i = index[0][0]
                if np.sum(np.array(path)) + nums[i] == 264:
                    backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)
    # TODO 第四行可直接减出来
    # 检查列
    elif 12 <= pathlen <= 15 or 28 <= pathlen <= 31:
        # martix = np.array(path).reshape(-1, 4)
        col = path[pathlen - 12::4]
        # colSum = np.sum(col)
        index = np.where(nums == 66 - np.sum(col))
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
nums = list(range(2, 33))
print(nums)
# 同质 1 开头即可
backtrack(nums, [1], res)
print(res)
