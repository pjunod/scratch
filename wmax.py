import numpy

nums=[1,3,-1,-3,5,3,6,7]

k = 3
p0 = 0
p1 = p0 + k - 1
wmax = 0
while p1 <= len(nums):
    if numpy.max(nums[p0:p1]) > wmax:
        wmax = numpy.max(nums[p0:p1])
    p1 += 1
    p0 += 1
print(wmax)