from dash import Dash, html 

app = Dash(__name__)

app.layout = html.Div([
    html.H1("World happiness Dashboard"), # Fixed: Changed h1 to H1
    html.P([                               # Fixed: Changed p to P
        "This dashboard shows the world happiness score.",
        html.Br(),                         # Added missing comma before this
        html.A(
            "World happiness report Data source",
            href="https://worldhappiness.report/",
            target="_blank"                # Note: standard is "_blank" with underscore
        )
    ])                                     # Closed the P tag correctly
])

if __name__ == "__main__":
    app.run(debug=True)