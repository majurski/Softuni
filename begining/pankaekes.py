days = int(input())
sladkari = int(input())
torti = int(input())
gofreti = int(input())
palachinki = int(input())
  
alltorti = 45*torti
allgofreti = 5.8*gofreti
allpalachinki = 3.2*palachinki

perday = (alltorti + allgofreti + allpalachinki)*sladkari
allprofit = perday*days
finalprofit = allprofit - allprofit/8
print({finalprofit:.2f})
