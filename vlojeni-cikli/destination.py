dest = input()

while dest != "End":
    budget = float(input())
    save = 0
    while save < budget:
        save += float(input())
    print(f"Going to {dest}!")
    dest = input()
