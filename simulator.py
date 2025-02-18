import random
import time

# Class to represent a Stock
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    # Update stock price by a random percentage (simulating price change)
    def update_price(self):
        change_percentage = random.uniform(-0.05, 0.05)  # -5% to +5% fluctuation
        self.price *= (1 + change_percentage)
        self.price = round(self.price, 2)

# Class to represent a User
class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.portfolio = {}

    # Buy stocks
    def buy_stock(self, stock, quantity):
        cost = stock.price * quantity
        if self.balance >= cost:
            if stock.symbol in self.portfolio:
                self.portfolio[stock.symbol] += quantity
            else:
                self.portfolio[stock.symbol] = quantity
            self.balance -= cost
            print(f"{self.name} bought {quantity} shares of {stock.symbol} at ${stock.price} each.")
        else:
            print(f"{self.name} doesn't have enough balance to buy {quantity} shares of {stock.symbol}.")

    # Sell stocks
    def sell_stock(self, stock, quantity):
        if stock.symbol in self.portfolio and self.portfolio[stock.symbol] >= quantity:
            revenue = stock.price * quantity
            self.portfolio[stock.symbol] -= quantity
            self.balance += revenue
            print(f"{self.name} sold {quantity} shares of {stock.symbol} at ${stock.price} each.")
        else:
            print(f"{self.name} doesn't have enough shares of {stock.symbol} to sell.")

    # Display user portfolio
    def display_portfolio(self):
        print(f"\n{self.name}'s Portfolio:")
        if self.portfolio:
            for stock_symbol, quantity in self.portfolio.items():
                print(f"{stock_symbol}: {quantity} shares")
        else:
            print("No stocks in portfolio.")
        print(f"Cash Balance: ${self.balance}")

# Function to simulate market behavior and users' interactions
def market_simulation():
    # Initialize some stocks in the market
    stocks = [
        Stock("AAPL", 150.0),  # Apple
        Stock("GOOG", 2800.0),  # Google
        Stock("AMZN", 3500.0),  # Amazon
        Stock("TSLA", 700.0),   # Tesla
        Stock("MSFT", 300.0),   # Microsoft
    ]
    
    # Initialize user(s)
    user = User("John", 10000.0)  # John has $10,000 to trade
    
    # Start the simulation
    rounds = 10
    for round_num in range(rounds):
        print(f"\n--- Round {round_num + 1} ---")
        
        # Randomly update stock prices
        for stock in stocks:
            stock.update_price()
            print(f"{stock.symbol} updated price: ${stock.price}")
        
        # Simulate some random buying and selling actions for the user
        action = random.choice(["buy", "sell"])
        stock = random.choice(stocks)
        quantity = random.randint(1, 5)
        
        if action == "buy":
            user.buy_stock(stock, quantity)
        else:
            user.sell_stock(stock, quantity)
        
        # Display portfolio and balance
        user.display_portfolio()

        # Sleep for a moment to simulate real-time updates
        time.sleep(1)

# Run the simulation
market_simulation()
