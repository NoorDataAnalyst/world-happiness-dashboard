from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# 1. Use the Raw link you provided
url = "https://raw.githubusercontent.com/PacktPublishing/Python-Interactive-Dashboards-with-Plotly-Dash/refs/heads/main/world_happiness.csv"
happiness = pd.read_csv(url)

# 2. Create the graph variable (Note: using underscore, not dot)
line_fig = px.line(
    happiness[happiness["country"] == "United States"],
    x="year",
    y="happiness_score",
    title="Happiness Score in USA"
)

app = Dash(__name__)

# 3. Layout with corrected commas and capitalization
app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    html.P([
        "This dashboard shows the world happiness score.",
        html.Br(),
        html.A(
            "World happiness report Data source",
            href="https://worldhappiness.report/",
            target="_blank"
        )
    ]), # Ensure this comma is here
    
    dcc.RadioItems(
        options=happiness["region"].unique(), 
        value="North America"
    ), # Ensure this comma is here
    
    dcc.Checklist(
        options=happiness["region"].unique(), 
        value=["North America"]
    ), # Ensure this comma is here
    
    dcc.Dropdown(
        options=happiness["country"].unique(), 
        value="United States"
    ), # Ensure this comma is here
    
    dcc.Graph(figure=line_fig)
])

if __name__ == "__main__":
    app.run(debug=True) # Use 'run' instead of 'run_server'