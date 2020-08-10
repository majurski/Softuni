import math
w = 50.3232
h = 25.29382

a = 2.9384
  
zala = (w*100)*(h*100)
garderob = (a*100)*(a*100)
peika = zala/10

freespace = zala - garderob - peika

alldancer = freespace/(40+7000)

print(round(alldancer))
