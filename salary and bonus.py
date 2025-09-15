salary = float(input("Enter base salary: "))
experience = int(input("Enter years of experience: "))
if experience >= 10:
    bonus = 0.10 * salary
elif experience >= 5:
    bonus = 0.05 * salary
else:
    bonus = 0.02 * salary
total_salary = salary + bonus
print("Total salary including bonus:", total_salary)