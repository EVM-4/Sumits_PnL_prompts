"""
## Simple PnL Tracker
### Problem Statement:
Create a program to track the profit and loss of a small business. The program should:

1. Store the income and expenses of the business in separate lists.
2. Calculate the total income and total expenses.
3. Calculate the net profit or loss (total income - total expenses).
4. Print the total income, total expenses, and net profit or loss.

### Constraints:
- Use lists to store income and expense transactions.
- Use a for loop to calculate the total income and total expenses.
- Use basic arithmetic operations to calculate the net profit or loss.

### Sample Input:

income = [1000, 2000, 3000]
expenses = [500, 1000, 1500]


### Expected Output:
The program should display the total income, total expenses, and net profit or loss.


Sumit problem - 1 (19/04/2025)
"""


#Returns a single value
def list_adder_or_subtracter(list1,operation,list2):

    value = 0

    if str(operation) == "+":
        value = sum(list1) + sum(list2)

    if str(operation) == "-":
        for idx in range(len(list1)):
            value = sum(list1) - sum(list2)
    return(value)

def main():
    # please enter 0 if no income/expense is ready
    income_list = [1000, 2000, 4000]
    expenses = [500, 1000, 1500, 14, 16, 500]
    total_income = sum(income_list)
    total_expenses = sum(expenses)
    total_profit_or_loss = list_adder_or_subtracter(income_list,"-",expenses)


    print(f"Your total income is ${total_income} and your total expenses are ${total_expenses}")

    if total_profit_or_loss >= 0:
        print(f"Your total profit is ${total_profit_or_loss}")
    else:
        print(f"Your total loss is ${total_profit_or_loss}")
main()

