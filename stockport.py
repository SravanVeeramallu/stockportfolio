class MyStock:
    def __init__(self, name, quantity, purchase_price):
        self.name = name
        self.quantity = quantity
        self.purchase_price = purchase_price

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = []

    def add_stock(self, stock):
        self.portfolio.append(stock)

    def remove_stock(self, name):
        for s in self.portfolio:
            if s.name == name:
                self.portfolio.remove(s)
                return
        print(f"{name} not found in portfolio.")

    def track_performance(self):
        total_investment = 0
        for stock in self.portfolio:
            current_price = self.get_current_price(stock.name)
            investment_value = current_price * stock.quantity
            total_investment += investment_value
            print(f"\n{stock.name} : {stock.quantity} shares")
            print(f"Current Price: ${current_price:.2f}")
            print(f"Investment Value: ${investment_value:.2f}")
        print(f"\nTOTAL INVESTMENT VALUE: ${total_investment:.2f}")

    def get_current_price(self, name):
        # Simulated current price for demonstration
        simulated_prices = {
            "AAPL": 150.0,
            "MSFT": 250.0,
            "GOOGL": 2800.0,
            "AMZN": 3500.0
        }
        return simulated_prices.get(name, 0)

# Create portfolio tracker instance
portfolio = StockPortfolioTracker()

# Add stocks
portfolio.add_stock(MyStock("AAPL", 10, 120))
portfolio.add_stock(MyStock("MSFT", 5, 200))
portfolio.add_stock(MyStock("GOOGL", 3, 1500))
portfolio.add_stock(MyStock("AMZN", 8, 500))

# Remove stock
portfolio.remove_stock("AMZN")

# Track performance
portfolio.track_performance()
