# 기간별 수익률을 returns 리스트에 저장한다. 
returns = [0.1, 0.06, 0.05]
sumOfReturn = 0.0
arimean = 0.0
geomean = 1.0
n = len(returns)

cnt = 0
for r in returns:
    sumOfReturn = sumOfReturn + r   
    cnt += 1
arimean = sumOfReturn / cnt
print('AriMean is {:.2%}'.format(arimean))


######################
for r in returns:
    geomean = geomean*(1+r)

geomean = geomean**(1/cnt) -1
print('geoMean is {:.2%}'.format(geomean))




