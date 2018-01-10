import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output

# Initialize the Dash server
app = dash.Dash()
app.title = 'Dash App'

################ DOMINO REQUIREMENTS ################
######################################################
# Configure path for dependencies.  This is required for Domino.
app.config.update({
    #### as the proxy server may remove the prefix
    'routes_pathname_prefix': '',

    #### the front-end will prefix this string to the requests
    #### that are made to the proxy server
    'requests_pathname_prefix': ''
})

# This enables the Flask server to be visible to the Domino server
server = app.server
######################################################

# Style sheet for formatting
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Initialize the app framework
app.layout = html.Div([

    # Build the header
    html.Div(
        html.H1('Dash App',style={'textAlign': 'center', 'color': '#fcfcfc','verticalAlign':'middle'}),
        style={'background-color': '#a50000'}
        ),
    # Build the I/O interface
    html.Div(className="row", children=[
        html.Div([
            dcc.Markdown("### Type Something"),
            dcc.Input(id='input_text', value='type here', type="textarea")
            ], className="four columns"),

        html.Div([
            dcc.Markdown('### Number of Characters'),
            html.Div(id='output')
            ], className="four columns")
        ])

])

# Updates the output with changes to input
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input_text', component_property='value')]
)
def num_char(input_value):
    return len(input_value)
    
################ DOMINO REQUIREMENTS ################
######################################################
# host & port need to be explicitly defined for Domino
if __name__ == '__main__':
    #app.run_server() # if running locally
    app.run_server(host='0.0.0.0',port=8888) # on Domino

