from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# dataset: California real state
# url: https://www.kaggle.com/camnugent/california-housing-prices

# Read The data frame
df = pd.read_csv("housing.csv")

app.layout = html.Div([
    html.H4('ocean proximity correlation distribution based on latitude, longitude, median house value and median '
            'income'),
    dcc.Dropdown(
        id="dropdown",
        options=["latitude", "longitude", "median_house_value", "median_income"],
        value=["latitude", "longitude"],
        multi=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_bar_chart(dims):
    df = pd.read_csv("housing.csv")
    fig = px.scatter_matrix(
        df, dimensions=dims, color="ocean_proximity")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)