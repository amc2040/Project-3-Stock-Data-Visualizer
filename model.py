"""
Stock Data Visualizer - Model Layer
Handles data fetching, validation, and processing
"""

# Import necessary modules
import requests                      # For making HTTP requests to the API
from datetime import datetime        # For handling and validating dates
from config import API_KEY           # Import API key from config.py