#평균과 기댓값

nums = [1,2,3,4,5,6]
print(sum (nums) / len(nums))


import numpy as np
from numpy.lib.polynomial import polyfit

a = np.array(nums)

print(a.mean())


case = [1,2,3,4,5,6]
prob = [1/6,1/6,1/6,1/6,1/6,1/6,1/6]
ex = 0.0
for c, p in zip(case, prob):
    ex = ex + c * p


#ex = sum (c*p for c,p in zip(case,prob))
print(ex)




#이동평균

prices = [4480,44850, 44600, 43750, 44000,43900, 44350,44350,45500,45700]
n = 5
for p in range(n,len(prices)):
    end_index = p
    begin_index = end_index - n
    print(begin_index, end_index)
    print(prices[begin_index:end_index])
    print(sum(prices[begin_index:end_index])/n)



#가중 산술 평균
score = [82,90,76]
weight = [0.2 , 0.35 , 0.45]

wgt_avg = 0.0

for s,w in zip(score,weight):
    wgt_avg += s * w

print(wgt_avg) 


# 분산과 표준편차

nums = [1,2,3,4,5]
avg= sum (nums) / len(nums)
sumsquare = 0.0
for n in nums:
    sumsquare += (n-avg)**2
var = sumsquare/(len(nums) - 1)
print("var = ",var)

#sumsquare = sum ((n-avg)**2 for n in nums)

import math
stdev = math.sqrt(var)
print("stdev = ",stdev)

import matplotlib.pyplot as plt
from scipy.stats import norm
x_axis = np.arange(-10,10 ,0.001)
plt.plot(x_axis,norm.pdf(x_axis,0,2))

#plt.show()

## 자유도 
