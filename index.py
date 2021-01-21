import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app


# Connect to your app pages
from apps import step1,step2,home,step4



app.layout =dbc.Container([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        [
            dbc.NavLink("Consommateur",href="/apps/step1"),
            dbc.NavLink("Prosomateur",href="/apps/step2"),
            dbc.NavLink("Comparasion",href="/apps/step4"),

        ],
        className="border border-light w-100",
        brand="Analytics Dashboard Home",
        brand_href="/",
        color="dark",
        dark=True,
    ),
    html.Div(id='page-content', children=[],className="bg-secondary ")

],fluid=True)



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/step1':
        return step1.layout
    if pathname == '/apps/step2':
        return step2.layout
    if pathname == '/apps/step4':
        return step4.layout
    if pathname=="/":
        return home.layout




if __name__ == '__main__':
    app.run_server(debug=False)