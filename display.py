import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('task.csv')
df = df.sort_values('date') # sorts oldest to newest

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    html.Div([
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All',   'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East',  'value': 'east'},
                {'label': 'West',  'value': 'west'},
            ],
            value='all',  # default selection
            inline=True,
        )
    ], className="radio-container"),
    dcc.Graph(id='sales-chart')
])

@app.callback( # makes chart reactive
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered = df
    else:
        filtered = df[df['region'] == selected_region]

    fig = px.line(filtered, x='date', y='sales', color='region',
                  labels={'date': 'Date', 'sales': 'Sales'})

    return fig

if __name__ == '__main__':
    app.run()