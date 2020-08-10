whyskiprice = float(input())
beer = float(input())
wine = float(input())
rakia = float(input())
whyski = float(input())

rakiaprice = whyskiprice / 2
wineprice = rakiaprice - rakiaprice * 0.4
beerprice = rakiaprice - rakiaprice * 0.8

beertotal = beer*beerprice
whyskitotal = whyski*whyskiprice
rakiatotal = rakia*rakiaprice
winetotal = wine*wineprice

all = beertotal + whyskitotal + rakiatotal + winetotal

print(f'{all:.2f}')