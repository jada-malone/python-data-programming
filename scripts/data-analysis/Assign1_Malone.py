# Constants
TOTAL_SHARES = 200
PURCHASE_PRICE_PER_SHARE = 30.00
CAPITAL_GAINS_TAX_RATE = 0.15

# Inputs for first sale
print("Sales 1 Details:\n")
shares_sold1 = int(input("How many shares out of 200 do you  wish to sell? "))
price_per_share1 = float(input("Enter the sales price per share: $"))

# Inputs for second sale
print("\nSales 2 Details:\n")
shares_sold2 = int(input(f"How many shares out of {TOTAL_SHARES - shares_sold1} do you  wish to sell? "))
price_per_share2 = float(input("Enter the sales price per share: $"))

# Calculations
total_spent = TOTAL_SHARES * PURCHASE_PRICE_PER_SHARE
total_earned = (shares_sold1 * price_per_share1) + (shares_sold2 * price_per_share2)
capital_gain = total_earned - total_spent
capital_gains_tax = CAPITAL_GAINS_TAX_RATE * capital_gain if capital_gain > 0 else 0
net_profit = capital_gain - capital_gains_tax

# Output
print("\n")
print("Total Spend on Purchase: ${:.2f}".format(total_spent))
print(f"Total Earning from sales: ${total_earned:.2f}")
print("Capital Gain Tax: ${:.2f}".format(capital_gains_tax))
print(f"Net Profit after Tax: ${net_profit:.2f}")

