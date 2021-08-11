# NPV
# 미래의 현금 유입 유출을 현재 시점을 가져와 계산하는 방식
# 투자에 사용되는 방법

cashflows = [12000, 15000, 18000, 21000, 26000]
i = 0
r = 0.015
npv = -70000
for c in cashflows:
    i = i + 1 
    npv = npv+c/(1+r)**i

print(npv)
# npv 가 양수이면 투자 결정 가능

# scipy 를 이용한 계산 방식

import scipy as sp

cashflows = [-70000, 12000, 15000, 18000, 21000, 26000]
npv = sp.npv(r, cashflows)
print(npv)



##########
# IRR 

# IRR > 시장 이자율 이면 투자 채택 

irr = sp.irr (cashflows)
npv = sp.npv (irr , cashflows)
print('IRR {0:.1%} makes NPV {1:.2f} '.format(irr,npv))
