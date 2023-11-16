category_number=int(input("Enter number of categories you want to track: "))
total_budget=0
for i in range(category_number):
    category=input("Enter a category: ")
    initial_budget  = float(input("Enter your budget for this expense: $"))
    total_budget = initial_budget + total_budget
print("You have budgeted " + str(total_budget) + " to spend this Thanksgiving.")






 
   