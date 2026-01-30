from dash import Dash, html 
app = Dash()
app.layout = html.Div("My Dashboard is live")
if __name__ == "__main__":
    app.run(debug=True)
