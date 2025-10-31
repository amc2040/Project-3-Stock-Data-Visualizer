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
