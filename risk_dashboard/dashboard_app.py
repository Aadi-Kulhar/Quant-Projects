import dash
from dash import dcc, html
import plotly.graph_objs as go
from data_loader import get_stock_returns
from var_models import historical_var, parametric_var, monte_carlo_var, cvar
from drawdown import max_drawdown
import numpy as np

app = dash.Dash(__name__)
ticker = 'AAPL'
data = get_stock_returns(ticker)
returns = data['Returns'].values

layout = go.Layout(title='Daily Returns of ' + ticker,
                   xaxis={'title': 'Date'},
                   yaxis={'title': 'Return'})

fig = go.Figure([go.Scatter(x=data.index, y=data['Returns'])], layout=layout)

app.layout = html.Div([
    html.H1(f'Risk Analytics Dashboard - {ticker}'),
    dcc.Graph(figure=fig),
    html.Div([
        html.P(f'Historical VaR (95%): {historical_var(returns):.4f}'),
        html.P(f'Parametric VaR (95%): {parametric_var(returns):.4f}'),
        html.P(f'Monte Carlo VaR (95%): {monte_carlo_var(100, np.mean(returns), np.std(returns)):.4f}'),
        html.P(f'Conditional VaR (CVaR): {cvar(returns):.4f}'),
        html.P(f'Maximum Drawdown: {max_drawdown(returns):.4f}')
    ])
])

if __name__ == '__main__':
    app.run_server(debug=False)
