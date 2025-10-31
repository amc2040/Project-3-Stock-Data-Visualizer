"""
Stock Data Visualizer - Model Layer
Handles data fetching, validation, and processing
"""

# Import necessary modules
import requests                      # For making HTTP requests to the API
from datetime import datetime        # For handling and validating dates
from config import API_KEY           # Import API key from config.py

# Class: AlphaVantageAPI

class AlphaVantageAPI:
    """Handles API communication with Alpha Vantage"""
    
    BASE_URL = "https://www.alphavantage.co/query"  # Base URL for the Alpha Vantage API
    
    def __init__(self):
        """Initialize the API client with API key"""
        self.api_key = API_KEY  # Store API key for authentication
    
    def fetch_stock_data(self, symbol, time_series):
        """
        Fetch stock data from Alpha Vantage API
        
        Args:
            symbol (str): Stock symbol (e.g., 'GOOGL')
            time_series (int): Time series function 
                               (1=Intraday, 2=Daily, 3=Weekly, 4=Monthly)
        
        Returns:
            dict: JSON response from API or None if an error occurs
        """
        # Map user’s choice (1–4) to the correct API function name
        function_map = {
            1: "TIME_SERIES_INTRADAY",
            2: "TIME_SERIES_DAILY",
            3: "TIME_SERIES_WEEKLY",
            4: "TIME_SERIES_MONTHLY"
        }
        
        # Set up API request parameters
        params = {
            'function': function_map[time_series],
            'symbol': symbol,
            'apikey': self.api_key,
            'outputsize': 'full'  # Get full historical data (up to 20 years)
        }
        
        # If user selects Intraday, add an interval
        if time_series == 1:
            params['interval'] = '60min'
        
        try:
            # Send GET request to API
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raises error for 4xx/5xx responses
            
            data = response.json()
            
            # Check if API returned an error message
            if "Error Message" in data:
                print(f"API Error: {data['Error Message']}")
                return None
            
            # Check if API returned a note (e.g., rate limit reached)
            if "Note" in data:
                print(f"API Note: {data['Note']}")
                return None
            
            # Return valid JSON data
            return data
            
        except requests.exceptions.RequestException as e:
            # Handle network or connection errors
            print(f"Network error: {e}")
            return None