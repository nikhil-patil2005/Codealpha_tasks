
stock_prices = {
    "RELIANCE": 1520,
    "TCS": 3450,
    "INFY": 1625,
    "HDFCBANK": 1890,
    "ICICIBANK": 1410,
    "SBI": 845,
    "BHARTIARTL": 1985,
    "LT": 3640,
    "TATAMOTORS": 695,
    "ADANIENT": 2480,
    "TATASIVER": 21,
    "TATAGOLD": 14,
}

portfolio = {}
total_investment = 0

print("=" * 55)
print("         STOCK PORTFOLIO TRACKER ")
print("=" * 55)

print("\nAvailable Stocks")
print("-" * 30)

for stock, price in stock_prices.items():
    print(f"{stock:<10} : ₹{price}")

print("\nType 'DONE' when you finish adding stocks.\n")


while True:

    stock = input("Enter Stock Name : ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print(" Stock not available. Please choose from the list.\n")
        continue

    try:
        quantity = int(input("Enter Quantity   : "))

        if quantity <= 0:
            print(" Quantity must be greater than 0.\n")
            continue

    except ValueError:
        print(" Please enter a valid number.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

    print(" Stock added successfully!\n")

print("\n" + "=" * 55)
print("            PORTFOLIO SUMMARY")
print("=" * 55)

if not portfolio:
    print("No stocks were added.")

else:

    print(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Total'}")
    print("-" * 45)

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        print(f"{stock:<10}{quantity:<8}${price:<9}${investment}")

    print("-" * 45)
    print(f"Total Investment Value : ${total_investment}")

    
    with open("portfolio_summary.txt", "w") as file:

        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Total'}\n")
        file.write("-" * 40 + "\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock:<10}{quantity:<8}${price:<9}${investment}\n"
            )

        file.write("\n")
        file.write("=" * 40 + "\n")
        file.write(f"Total Investment Value : ${total_investment}")

    print("\n Portfolio saved successfully as 'portfolio_summary.txt'")

print("\nThank you for using Stock Portfolio Tracker! ")
