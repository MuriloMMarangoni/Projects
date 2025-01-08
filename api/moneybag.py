import random

money = []

for each in [200,100,50,20,10,5,2,1,0.5,0.25,0.05]:
    for r in range (random.randint(0,5)):
        money.append(each)

parcela_normal = round(sum(money)/72 ,2)

print(parcela_normal)

if str(parcela_normal)[-1] in '1234':
    parcela_normal = str(parcela_normal)[0:-1]+'0'
elif str(parcela_normal)[-1] in '6789':
    parcela_normal = str(parcela_normal)[0:-1]+'5'
    
print(parcela_normal)