#python 3.6.8
#단리 이자 계산
a = 1000
n = 1 
r = 0.05

s_simple = a *( 1 + r * n )
print(s_simple)


#단리 계산 월계산
a = 1000
n = 12 
r = 0.05/n

s_simple = a *( 1 + r * n )
print(s_simple)


#!pip install scipy
#scipy라이브러리의 fv함수를 이용해 계산
import scipy as sp

a = 1000
n = 1 
r = 0.05
s_simple = sp.fv(r, n , 0 , a)
print(s_simple)


a = 1000
n = 12 
r = 0.05
s_simple = sp.fv(r/n, n , 0 , a)
print(s_simple)