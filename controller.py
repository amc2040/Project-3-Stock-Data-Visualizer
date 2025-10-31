"""
Stock Data Visualizer - Controller Layer
Communicates between Model and View
"""

from model import AlphaVantageAPI, StockData, validate_date_format, Validate_date_range
from view import ConsoleUI, ChartGenerator

class StockController:
    """Main app controller"""
    
    def __init__(self):
        """Initialize controller with API client and UI"""
        self.api = AlphaVantageAPI()
        self.ui = ConsoleUI()
        self.chart_gen = ChartGenerator()