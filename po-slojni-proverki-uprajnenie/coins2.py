coins = float(input())
act = round(coins * 100)
number = 0
lv2 = 0
lv1 = 0
st50 = 0
st20 = 0
st10 = 0
st5 = 0
st2 = 0
st1 = 0

while act > 0:
    if act >= 200:
        number += 1
        act -= 200
        lv2 += 1
    elif act >= 100:
        number += 1
        act -= 100
        lv1 += 1
    elif act >= 50:
        number += 1
        act -= 50
        st50 += 1
    elif act >= 20:
        number += 1
        act -= 20
        st20 += 1
    elif act >= 10:
        number += 1
        act -= 10
        st10 += 1
    elif act >= 5:
        number += 1
        act -= 5
        st5 += 5
    elif act >= 2:
        number += 1
        act -= 2
        st2 += 2
    elif act >= 1:
        number += 1
        act -= 1
        st1 += 1
        break

print(f"Общо монети: {number}")
print(f"{lv2} бр. по 2лв.")
print(f"{lv1} бр. по 1лв.")
print(f"{st50} бр. по 50ст.")
print(f"{st20} бр. по 20ст.")
print(f"{st10} бр. по 10ст.")
print(f"{st5} бр. по 5ст.")
print(f"{st2} бр. по 2ст.")
print(f"{st1} бр. по 1ст.")