import dash
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from dash import dcc, html  # Correct import for html and dcc components
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("📈 Stock Market Tracker", className="title"),
    
    html.Div([
        dcc.Dropdown(
            id='stock-dropdown',
            options=[{'label': symbol, 'value': symbol} for symbol in ['AAPL', 'MSFT', 'GOOGL', 'AMZN']],
            multi=True,
            className="dropdown"
        ),
        
        dcc.DatePickerRange(
            id='date-picker',
            start_date='2024-01-01',
            end_date='2025-01-01',
            display_format='YYYY-MM-DD',
            className="date-picker"
        ),
        
        html.Button("Download Data", id="download-btn", className="download-btn"),
    ], className="form-container"),
    
    dcc.Graph(id='stock-chart', className="chart-container")
])

# Callback to update stock chart
@app.callback(
    Output('stock-chart', 'figure'),
    [Input('stock-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graph(selected_stocks, start_date, end_date):
    if not selected_stocks:
        return go.Figure()  # Return an empty figure if no stocks are selected

    fig = go.Figure()
    
    for stock in selected_stocks:
        data = yf.download(stock, start=start_date, end=end_date)
        print(f"Fetched data for {stock}:\n", data.head())  # Debugging output

        if data.empty:
            print(f"No data found for {stock}")
            continue  # Skip if no data is available
        
        # Check that data has the correct columns
        print(f"Columns: {data.columns}")

        # Add Candlestick trace
        fig.add_trace(go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name=stock
        ))

    fig.update_layout(
        title="Stock Price Chart", 
        xaxis_title="Date", 
        yaxis_title="Price",
        xaxis_rangeslider_visible=True
    )
    return fig



if __name__ == '__main__':
    app.run(debug=True)
