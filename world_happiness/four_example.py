from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

# 1. Define components with IDs (removed the trailing comma)
input_text = dcc.Input(id="my-input", value="Change this Text", type="text")
output_text = html.Div(id="my-output")

app.layout = html.Div([input_text, output_text])

# 2. Reference the 'id' strings in the callback
@app.callback(
    Output(component_id="my-output", component_property="children"),
    Input(component_id="my-input", component_property="value")
)
def update_output_div(user_input):
    return f"Text: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)