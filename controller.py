"""
Stock Data Visualizer - Controller Layer
Communicates between Model and View
"""

from model import AlphaVantageAPI, StockData, validate_date_format, validate_date_range
from view import ConsoleUI, ChartGenerator

class StockController:
    """Main app controller"""
    
    def __init__(self):
        """Initialize controller with API client and UI"""
        self.api = AlphaVantageAPI()
        self.ui = ConsoleUI()
        self.chart_gen = ChartGenerator()

    def run(self):
        """Get stock symbol"""
        try:
            symbol = self.ui.get_stock_symbol()
            if not symbol:
                self.ui.display_error("Stock symbol cannot be empty.")
                return
        
            """Get chart type"""  
            chart_type = self.ui.get_chart_type()

            """Get time series selection"""
            time_series = self.ui.get_time_series()

            """Get start date"""
            start_date_str = self.ui.get_date("Enter the start date (YYY-MM-DD):")
            start_date = validate_date_format(start_date_str)

            if not start_date:
                self.ui.display_error("Invalid start date format. Please use YYYY-MM-DD):")
                return
        
            """Get end date"""
            end_date_str = self.ui.get_date("Enter the end date (YYYY-MM-DD):")
            end_date = validate_date_format(end_date_str)

            if not end_date:
                self.ui.display_error("Invalid end date format. Please use YYYY-MM-DD.")
                return
        
            """Validate date range"""
            if not validate_date_range(start_date, end_date):
                self.ui.display_error("End date must be after or equal to start date.")
                return
        
            """Get data from API"""
            print("\nFetching stock data from Alpha Vantage...")
            raw_data = self.api.fetch_stock_data(symbol, time_series)
            
            if not raw_data:
                self.ui.display_error("Failed to fetch stock data. Please check your API key and try again.")
                return
        
            """Process data"""
            stock_data = StockData(symbol, raw_data, time_series)
            filtered_data = stock_data.filter_by_date_range(start_date, end_date)
            
            if not filtered_data:
                self.ui.display_error(f"No data found for {symbol} in the specified date range.")
                return
            
            formatted_data = stock_data.get_formatted_data()
            
            if not formatted_data:
                self.ui.display_error("Failed to format stock data.")
                return
            
            print(f"Successfully retrieved {len(formatted_data['dates'])} data points.")

            """Generate chart"""
            print("Generating chart...")
            chart_file = self.chart_gen.create_chart(
                formatted_data, 
                symbol, 
                chart_type, 
                start_date_str, 
                end_date_str
            )
            
            if not chart_file:
                self.ui.display_error("Failed to generate chart.")
                return
        
            """Open chart in browser"""
            self.chart_gen.open_in_browser(chart_file)
            
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
        except Exception as e:
            self.ui.display_error(f"An unexpected error occurred: {e}")    
            