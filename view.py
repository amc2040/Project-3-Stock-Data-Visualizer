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
        date_str = input(f"\n{prompt} ").strip()
        return date_str
    
    @staticmethod
    def display_error(message):
        print(f"\nError: {message}")

    @staticmethod
    def display_success(message):
        print(f"n{message}")


class ChartGenerator:
        
        @staticmethod
        def create_chart(data, symbol, chart_type, start_date, end_date):
            if not data or not data['dates']:
                return None
            
            chart_type_str = 'bar' if chart_type == 1 else 'line'

            html_content = f"""
<!DOCTYPE HTML>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
        }}
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }}
        .chart-container {{
            position: relative;
            height: 600px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Stock Data for {symbol}: {start_date} to {end_date}</h1>
        <div class="chart-container">
            <canvas id="stockChart"></canvas>
        </div>
    </div>
    
    <script>
        const ctx = document.getElementById('stockChart').getContext('2d');
        const chart = new Chart(ctx, {{
            type: '{chart_type_str}',
            data: {{
                labels: {data['dates']},
                datasets: [
                    {{
                        label: 'Open',
                        data: {data['open']},
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 2
                    }},
                    {{
                        label: 'High',
                        data: {data['high']},
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 2
                    }},
                    {{
                        label: 'Low',
                        data: {data['low']},
                        backgroundColor: 'rgba(75, 192, 192, 0.5)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2
                    }},
                    {{
                        label: 'Close',
                        data: {data['close']},
                        backgroundColor: 'rgba(255, 206, 86, 0.5)',
                        borderColor: 'rgba(255, 206, 86, 1)',
                        borderWidth: 2
                    }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{
                        beginAtZero: false,
                        title: {{
                            display: true,
                            text: 'Price ($)'
                        }}
                    }},
                    x: {{
                        title: {{
                            display: true,
                            text: 'Date'
                        }},
                        ticks: {{
                            maxRotation: 45,
                            minRotation: 45
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: true,
                        position: 'top'
                    }},
                    title: {{
                        display: false
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""
            
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False)
            temp_file.write(html_content)
            temp_file.close()

            return temp_file.name
        
        @staticmethod
        def open_in_browser(file_path):
            try:
                webbrowser.open('file://' + os.path.abspath(file_path))
                print(f"\nChart opened in your default browser.")
            except Exception as e:
                print(f"\nError opening browser: {e}")
                print(f"You can manually open the file at: {file_path}")
