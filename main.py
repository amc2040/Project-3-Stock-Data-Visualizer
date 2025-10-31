from controller import StockController

def main():
    try:
        print("Stock Data Visualizer")
        print("-" * 50)
        print()

        app = StockController
        app.run()

    except KeyboardInterrupt:
        print("\n\nApplication terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try running the application again.")

if __name__ == "__main__":
    main()
