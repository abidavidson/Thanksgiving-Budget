#Sets up the categories that the user wants to track.
total_budget=0
category_input=input("Do you need to add a category to your budget? (Yes/No): ")
while category_input == "Yes":
    category_1=input("Enter a category: ")
    initial_budget_1  = float(input("Enter your budget for this expense: $"))
    total_budget = initial_budget_1 + total_budget
    print("Your budget for Thanksgiving is $" + str(total_budget) + " so far.")
    category_input_more=input("Do you need to add a category to your budget? (Yes/No): ")
    if category_input_more == "No": 
        break
    else:
        category_2=input("Enter a category: ")
        initial_budget_2  = float(input("Enter your budget for this expense: $"))
        total_budget = initial_budget_2 + total_budget
        print("Your budget for Thanksgiving is $" + str(total_budget) + " so far.")
        category_input_more_2=input("Do you need to add a category to your budget? (Yes/No): ")
        if category_input_more_2 == "No": 
            break
        else: 
            category_3=input("Enter a category: ")
            initial_budget_3  = float(input("Enter your budget for this expense: $"))
            total_budget = initial_budget_3 + total_budget
print("You have budgeted $" + str(total_budget) + " to spend.")

#Compiles a guest list and determines the cost per person of the Thanksgiving dinner.
number=int(input("Enter the number of guests you will have for Thanksgiving: "))
number_stop = number + 1
full_name = " "
space = ", "
for i in range(1,number_stop):
    name=input("Enter name " + str(i) + ": ")
    full_name = full_name + name + space
print("Guest list: " + full_name)
cost_per_person = total_budget / number
cost_per_person_round = round(cost_per_person,2)
print("You are spending $" + str(cost_per_person_round) + " per person.")

#Changes the amount in the budget available after the user inputs an expense.
spending=input("Do you need to input expenses? (Yes/No): ")
while spending == "Yes":
    category_expense=input("Enter category for expense: ")
    if category_expense==category_1:
        expense=float(input("Amount spent: "))
        current_amount=initial_budget_1-expense
        print("You have $" + str(current_amount) + " left for " + category_1)
        if current_amount < 0: 
            budget_adjust=total_budget - initial_budget_1 - current_amount
            print("Uh-oh! You have spent more than the budget for " + category_1 + ". Spend $" + str(budget_adjust) + " less in other categories.")
    elif category_expense==category_2:
        expense=float(input("Amount spent: "))
        current_amount=initial_budget_2-expense
        print("You have $" + str(current_amount) + " left for " + category_2)
        if current_amount < 0: 
            budget_adjust=total_budget - initial_budget_2 - current_amount
            print("Uh-oh! You have spent more than the budget for " + category_2 +  ". Spend $" + str(budget_adjust) + " less in other categories.")
    elif category_expense==category_3:
        expense=float(input("Amount spent: "))
        current_amount=initial_budget_3-expense
        print("You have $" + str(current_amount) + " left for " + category_3)  
        if current_amount < 0: 
            budget_adjust=total_budget - initial_budget_3 - current_amount
            print("Uh-oh! You have spent more than the budget for " + category_3 +  ". Spend $" + str(budget_adjust) + " less in other categories.")
    else:
        category_expense=input("Enter category for expense: ")
    spending=input("Do you need to input expenses? (Yes/No): ")









 
   