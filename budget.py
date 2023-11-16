total_budget=0
category_1=input("Enter a category: ")
initial_budget_1  = float(input("Enter your budget for this expense: $"))
category_2=input("Enter a category: ")
initial_budget_2  = float(input("Enter your budget for this expense: $"))
category_3=input("Enter a category: ")
initial_budget_3  = float(input("Enter your budget for this expense: $"))
total_budget = initial_budget_1 + initial_budget_2 + initial_budget_3 + total_budget
print("You have budgeted $" + str(total_budget) + " to spend this Thanksgiving.")
more_categories=input("Do you have another category to add? (Yes/No) ")
while more_categories=="Yes":
    category=input("Enter a category: ")
    initial_budget = float(input("Enter your budget for this expense: $"))
    more_categories=input("Do you have another category to add? (Yes/No) ")
    

spending=input("Do you need to input expenses? (Yes/No): ")
while spending == "Yes":
    category_expense=input("Enter category for expense: ")
    if category_expense==category_1:
        expense=float(input("Amount spent: "))
        current_amount=initial_budget_1-expense
        print("You have $" + str(current_amount) + " left for " + category_1)
        if current_amount < 0: 
            budget_adjust=total_budget - initial_budget_1 - current_amount
            print("Uh-oh! You have spent more than the budget. Spend $" + str(budget_adjust) + " less in other categories.")
    elif category_expense==category_2:
        expense=float(input("Amount spent: "))
        current_amount=initial_budget_2-expense
        print("You have $" + str(current_amount) + " left for " + category_2)
        if current_amount < 0: 
            budget_adjust=total_budget - initial_budget_2 - current_amount
            print("Uh-oh! You have spent more than the budget. Spend $" + str(budget_adjust) + " less in other categories.")
    elif category_expense==category_3:
        expense=float(input("Amount spent: "))
        current_amount=initial_budget_3-expense
        print("You have $" + str(current_amount) + " left for " + category_3)  
        if current_amount < 0: 
            budget_adjust=total_budget - initial_budget_3 - current_amount
            print("Uh-oh! You have spent more than the budget. Spend $" + str(budget_adjust) + " less in other categories.")
    else:
        category_expense=input("Enter category for expense: ")
    spending=input("Do you need to input expenses? (Yes/No): ")








 
   