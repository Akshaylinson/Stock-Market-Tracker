StockTracker Web Application
StockTracker is a web-based stock tracking application built with Dash and Python. The application provides real-time stock data for multiple companies, allowing users to monitor stock prices, view historical data, and visualize stock trends through interactive charts. The app utilizes the Yahoo Finance API to fetch stock data for major companies such as Google (GOOGL), Apple (AAPL), Microsoft (MSFT), and Amazon (AMZN).

This project aims to give users an easy-to-use platform to track their preferred stocks, analyze historical trends, and gain insights into stock performance over time.

Features
Stock Data Fetching: Real-time stock data is retrieved using the Yahoo Finance API.

Time Range Selection: Users can select the time range for historical data (e.g., 1 month, 6 months, 1 year).

Interactive Charts: Displays stock performance on interactive charts, including line charts showing stock prices over time.

Company Stock Data: Provides the following metrics for each stock:

Open: The price at which the stock opened for the day.

High: The highest price the stock reached during the trading day.

Low: The lowest price the stock reached during the trading day.

Close: The price of the stock at market close.

Volume: The number of shares traded.

Multiple Stock Support: The app supports multiple tickers, including GOOGL (Google), AAPL (Apple), MSFT (Microsoft), and AMZN (Amazon).

Requirements
To run the app, you need to have the following Python packages installed:

dash

yfinance

pandas

plotly

You can install the required packages using the following command:

bash
Copy
Edit
pip install dash yfinance pandas plotly
How to Run
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Akshaylinson/StockTracker.git
cd StockTracker
Install the necessary dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
The application will start running on http://127.0.0.1:8050/ by default.

Open the URL in your web browser to interact with the app.

How it Works
Data Fetching: The app uses the yfinance library to fetch stock data for selected companies. When you select a company from the dropdown menu, the app fetches the corresponding stock data for that ticker from Yahoo Finance.

Displaying Data: After fetching the data, the app displays key stock information such as Open, High, Low, Close, and Volume for each selected day.

Chart Visualization: The data is visualized using Plotly charts, providing a clean and interactive line graph representation of stock price movements over time. Users can interact with the chart to zoom in and out for better analysis.

Example
When you select GOOGL (Google) from the dropdown menu, the app will fetch data for that ticker and display its price movements, including Open, Close, High, Low, and Volume for each trading day. You can also select different time frames, such as 1 month, 3 months, or 1 year, to analyze the stock's historical performance.

Contributing
Feel free to fork this repository, contribute with improvements, or open issues. Pull requests are welcome!

Fork the repository.

Create your feature branch: git checkout -b feature-name.

Commit your changes: git commit -m 'Add new feature'.

Push to the branch: git push origin feature-name.

Open a pull request.
