

import math
 
income = float(input())
grades = float(input())
minimum_wage = float(input())
 
sub = minimum_wage * 0.35
sub2 = grades * 25
 
if income <= minimum_wage and 4.5 < grades <= 5.49:
    print(f"You get a Social scholarship {(math.floor(sub))} BGN")
elif income >= minimum_wage and grades >= 5.5:
    print(f"You get a scholarship for excellent results {(math.floor(sub2))} BGN")
elif income <= minimum_wage and grades >= 5.5:
    if sub > sub2:
        print(f"You get a Social scholarship {(math.floor(sub))} BGN")
    elif sub < sub2:
        print(f"You get a scholarship for excellent results {(math.floor(sub2))} BGN")
    elif sub == sub2:
        print(f"You get a scholarship for excellent results {(math.floor(sub2))} BGN")
else:
    print("You cannot get a scholarship!")