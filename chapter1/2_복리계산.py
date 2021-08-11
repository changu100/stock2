#python 3.6.8
#복리 이자 계산

a = 1000
n = 12
r  = 0.05
s_compund = a * ( 1 + ( r / n ) )**n
print(s_compund)


import math 
amount = 1 
rate = 1.0

#기간이 1인 경우 , 즉 1년 복리라면
n = 1
s_compund = a * ( 1 + ( r / n ) )**n
print(s_compund)

#기간이 2인경우, 즉 6개월 복리라면
n = 2
s_compund = a * ( 1 + ( r / n ) )**n
print(s_compund)

#기간이 4인경우, 즉 분기 복리라면
n = 4
s_compund = a * ( 1 + ( r / n ) )**n
print(s_compund)

#기간이 12인경우, 즉 월 복리라면
n = 12
s_compund = a * ( 1 + ( r / n ) )**n
print(s_compund)

#기간이 52인경우, 즉 주 복리라면
n = 52
s_compund = a * ( 1 + ( r / n ) )**n
print(s_compund)

#기간이 365인경우, 즉 일 복리라면
n = 365
s_compund = a * ( 1 + ( r / n ) )**n
print(s_compund)

# 결과값은 오일러 상수와 유사해진다.
# 1051.161897881733
# 1050.0
# 1050.625
# 1050.9453369140622
# 1051.161897881733
# 1051.2458419272002
# 1051.2674964674472