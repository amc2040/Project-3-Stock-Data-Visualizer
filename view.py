@ -0,0 +1,28 @@
import webbrowser
import os
import tempfile

class ConsoleUI:
    
    @staticmethod
    def get_stock_symbol():
        symbol = input("Enter the stock symbol: ").strip().upper()
        return symbol
    
    @staticmethod
    def get_chart_type():
        print("\nChart Types")
        print("-" * 10)
        print("1. Bar")
        print("2. Line")

        while True:
            try:
                choice = int(input("\nEnter the chart type you want (1, 2): "))
                if choice in [1, 2]:
                    return choice
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid choice. Please enter 1 or 2.")
 @staticmethod
    def get_time_series():
        print("\nSelect the Time Series of the chart you want to Generate")
        print("-" * 10)
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")

        while True:
            try:
                choice = int(input("\nEnter time series option (1, 2, 3, 4): "))
                if choice in [1, 2, 3, 4]:
                    return choice
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
            except ValueError:
                print("Invalid input. Please enter a number (1-4).")

    @staticmethod
    def get_date(prompt):
        date_str = input(f"\n{prompt}").strip()
        return date_str
    
    @staticmethod
    def display_error(message):
        print(f"\nError: {message}")

    @staticmethod
    def display_success(message):
        print(f"n{message}")
