nums = [1,2,2,3,3,3]
s = set(nums)
b = list(s)
d = [nums.count(x) for x in b]
f = d.sort()
