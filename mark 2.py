"""
Here's an updated problem statement:

## Trading PnL Tracker
### Problem Statement:
Create a program to track the profit and loss of a trading business. The program should:

1. Store trade information (security name, buy/sell, quantity, price) in a list of dictionaries.
2. Calculate the total profit/loss for each security.
3. Calculate the overall profit/loss for the trading business.
4. Print the profit/loss for each security and the overall profit/loss.

### Constraints:
- Use a list of dictionaries to store trade information.
- Use functions to calculate profit/loss for each security and overall profit/loss.
- Use dictionaries to store security-wise profit/loss.

### Sample Input:

trades = [
    {"security": "AAPL", "type": "buy", "quantity": 100, "price": 100.0},
    {"security": "AAPL", "type": "sell", "quantity": 100, "price": 120.0},
    {"security": "GOOG", "type": "buy", "quantity": 50, "price": 500.0},
    {"security": "GOOG", "type": "sell", "quantity": 50, "price": 550.0},
    {"security": "MSFT", "type": "buy", "quantity": 200, "price": 200.0},
    {"security": "MSFT", "type": "sell", "quantity": 200, "price": 220.0}
]


### Expected Output:
The program should display the profit/loss for each security and the overall profit/loss.

### Hints:
- Use a dictionary to store security-wise profit/loss.
- Use functions to calculate profit/loss for each security and overall profit/loss.
- Use a loop to iterate over trades and calculate profit/loss.

You can add more features to this problem, such as:

- Calculating profit/loss by security type (e.g., stocks, options, futures)
- Calculating overall return on investment (ROI)
- Adding more complex calculations or analytics
- Integrating with external data sources or APIs

"""




def create_dict(TICKER,Expenses,Income):



    TICKER = {"Ticker": str(TICKER), "Expenses": float(Expenses), "Income": float(Income)}
    
    LIST_OF_DICTS_OF_STOCKS.append(TICKER)

LIST_OF_DICTS_OF_STOCKS=[]





a = True

while a == True:
    action = str(input("What would you like to do? Enter: BUY to buy a security - SELL to sell a security - LOOK to see profit and loss "))
#rework entire buy
    if action == "BUY":

        b = True

        while b == True:
            print("Beginning of loop")
            repeat = False
            exsisting_ticker = False

            TICKER = str(input("Ticker symbol of stock? "))
            for idx in range(0, len(LIST_OF_DICTS_OF_STOCKS)+1):
                if len(LIST_OF_DICTS_OF_STOCKS) != 0:
                    print(idx)
                    print()
                    which_dict = LIST_OF_DICTS_OF_STOCKS[idx]
                    if str(TICKER) == str(which_dict["Ticker"]):
                        print("MATCH")
                        exsisting_ticker = True
                        break
                    elif str(TICKER) != str(which_dict["Ticker"]) and  which_dict == LIST_OF_DICTS_OF_STOCKS[-1]:
                        print("This should be a new ticker")
                        break
                elif len(LIST_OF_DICTS_OF_STOCKS) == 0:
                    print(idx)
                    print("This should be your first stock")


            buy_price = int(input("Enter buy price: "))
            buy_amt = int(input("Enter number of shares you want to buy: "))
            Expense = buy_amt * buy_price
            print(f"You want to buy {buy_amt} shares of {TICKER} at {buy_price}.")
            conf = str(input("Y/N (Y for yes and N for redo)"))
            if conf == "Y" and exsisting_ticker == False:
                Income = 0
                create_dict(TICKER, Expense, Income)
                print(f"Entry has been made. Your total expense is {Expense}")

            elif conf == "Y" and exsisting_ticker == True:
                which_dict["Expenses"] = which_dict["Expenses"] + int(Expense)
                print(f"Entry has been made. Your total expense is {Expense}")
                repeat = False

            elif conf == "N":
                print("Sending you back to buy prompt")
                repeat = True
            else:
                print("You might have made a mistake somewhere. Sending you back to buy prompt")
                repeat = True


            if repeat == False:
                cont = input("Would you like to continue buying? Enter 'YES' to continue buying. Enter 'NO' to go back to main prompt.")

                if cont == "YES":
                    print("Sending you back to BUY prompt")
                    b = True

                if cont == "NO":
                    print("Sending you back to main prompt")
                    b = False
                    break

                if  cont != "NO" and cont != "YES":
                    print("Error when entering command. Sending you back to main prompt")
                    b = False
                    break

    if action == "SELL":
        RE = False
        s = True
        if len(LIST_OF_DICTS_OF_STOCKS) == 0:
            print("You dont have any stocks yet. Go buy some! ")
            a = True
            s = False
            si= False
            sii = False
            print(a)
        while s == True:
            sii = True
            while sii == True:
                TICKER = str(input("SELL - Ticker symbol of stock? (Enter RE to go back to main prompt)"))
                if TICKER == "RE":
                    s = False
                    sii = False
                    RE = True
                    print("Sending you back to main prompt")
                for idx in range(0, len(LIST_OF_DICTS_OF_STOCKS)):
                    which_dict = LIST_OF_DICTS_OF_STOCKS[idx]
                    if str(TICKER) == str(which_dict["Ticker"]):
                        print("MATCH")
                        sell_price = int(input("Enter sell price: "))
                        sell_amt = int(input("Enter number of shares you want to sell: "))
                        print(f"You want to sell {sell_amt} shares of {TICKER} at {sell_price}.")
                        conf = str(input("Y/N (Y for yes and N for redo)"))
                        if conf == "Y":
                            Income = sell_amt * sell_price
                            print(f" Entry made - Your total income selling the stock is{Income}")
                            which_dict["Income"] = which_dict["Income"] + int(Income)
                            cont = input("Continue selling? Enter 'YES' for yes, 'NO' for no ")
                            if cont == "YES":
                                print("Sending you back to SELL prompt")
                                sii = False
                                break
                            if cont == "NO":
                                print("Sending you back to main prompt")
                                sii = False
                                s = False
                                break
                            else:
                                print("You messed something up - Sending you back to main prompt")
                                sii = False
                                s = False
                                break
                        else:
                            print("Sending you back to sell security prompt")
                            sii = False
                            break
                    elif str(TICKER) != str(which_dict["Ticker"]) and idx == len(LIST_OF_DICTS_OF_STOCKS) - 1 and RE == False :
                        print("This ticker is new. You cannot sell something you do not own. Sending you back to sell prompt")

    if action == "LOOK":

            if len(LIST_OF_DICTS_OF_STOCKS) == 0:

                print("There is nothing for you to see here... go do something first")

            else:
                print("Here you can see the profit/loss for each stock you own")
                print("If the number is positive, it is profit. If the number is negative, it is loss")
                profit_or_loss_list = []
                for idx in range(0, len(LIST_OF_DICTS_OF_STOCKS)):
                    which_dict = LIST_OF_DICTS_OF_STOCKS[idx]
                    print(f"{which_dict['Ticker']} - P/L is {which_dict['Income']-which_dict['Expenses']}")
                    profit_or_loss_list.append(int(which_dict['Income'])-int(which_dict['Expenses']))
                print(profit_or_loss_list)
                print(f"Your total profit/loss is {sum(profit_or_loss_list)}")


                raw_data = input("Would you like to see the raw data? Enter 'YES' to view raw data. Enter anything else to go back to main prompt")
                if raw_data == 'YES':
                    print("Raw data is presented below")
                    print(LIST_OF_DICTS_OF_STOCKS)
                    input("When you are ready to continue, press enter.")


print(a)  

a = True




            
            
        
           
         
    



    


