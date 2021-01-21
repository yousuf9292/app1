import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app



card_content_1 = [
    html.A(href="apps/step1",children=[dbc.CardImg(src=app.get_asset_url('step1.png'))]),
    dbc.CardBody(
        [
            html.H5("Consommateur", className="card-title"),
        ],className="border border-light m-3 bg-secondary"
    ),
]

card_content_2 = [
    html.A(href="apps/step2",children=[dbc.CardImg(src=app.get_asset_url('step2.png'))]),
    dbc.CardBody(
        [
            html.H5("Prosomateur", className="card-title"),
        ],className="border border-light m-3 bg-secondary"
    ),
]

card_content_3 = [
    html.A(href="apps/step4",children=[dbc.CardImg(src=app.get_asset_url('step2.png'))]),
    dbc.CardBody(
        [
            html.H5("Comparasion", className="card-title"),
        ],className="border border-light m-3 bg-secondary"
    ),
]



layout = html.Div(
    [
    dbc.CardColumns(
    [

        dbc.Card(card_content_1, color="secondary",className="border border-light mt-5"),
        dbc.Card(card_content_2, color="secondary",className="border border-light mt-5"),
        dbc.Card(card_content_3, color="secondary",className="border border-light mt-5"),

    ],className="align-self-center pt-5 pr-3 pl-3"
)
],style={"width":"100","height":"100vh"}
)
