import random,time,sys
facade=0
obverse=0
try:
    times=int(input('抛硬币,输入抛硬币次数.'))
except ValueError:
    print('输入错误,需要输入正整数.')
    sys.exit(114514)
for i in range(times):
    fact=random.randint(0,1)
    if fact==0:
        facade+=1
        print('正面.')
        if times < 100:
            time.sleep(0.2)
        elif times>100 and times < 1000:
            time.sleep(0.5)
        else:
            time.sleep(0)
    if fact==1:
        obverse+=1
        print('反面.')
        if times < 100:
            time.sleep(0.2)
        elif times > 100 and times < 1000:
            time.sleep(0.5)
        else:
            time.sleep(0)
print('正面为'+str(facade)+'次'+'反面为'+str(obverse)+'次')
print('正面次数与反面次数之比为'+str(facade)+':'+str(obverse))
print('正面次数与反面次数比值'+str(facade/obverse))