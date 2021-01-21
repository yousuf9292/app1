import plotly.express as px
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input
from plotly.subplots import make_subplots
from app import app
import pandas as pd

Co2Emis=pd.read_csv("C:\\Users\\yousuf\\Desktop\\pythonProject\\datasets\\Co2Emis.csv",index_col="date")

print(Co2Emis)



sumfr1=round(Co2Emis.loc[:,"Co21EmisFR"].sum(),3)

sumfr2=round(Co2Emis.loc[:,"Co22EmisFR"].sum(),3)

sumuk1=round(Co2Emis.loc[:,"Co21EmisUK"].sum(),3)

sumuk2=round(Co2Emis.loc[:,"Co22EmisUK"].sum(),3)


layout=dbc.Card([
    dbc.CardBody([
    html.H1("Comparision",className="card-title text-center text-white border border-light"),
        dbc.Row([
            dbc.Col([
    dcc.Dropdown(id="countries-dpdn2",options=[
                                              {'label':"United Kingdom","value":"UK"},
                                              {'label':"France","value":"FR"},
                                              ],value="UK",clearable=False,className="mt-3 w-25"
                 ),
        dcc.RadioItems(
            id="graph-type",
            options=[
                {'label': 'Side By Side Comparision', 'value': 'side'},
                {'label': 'Single Graph Comparision', 'value': 'single'},
            ],
            value='single',className="mt-3 p-2 text-white",
            labelStyle={'display': 'inline-block'}
        ),
                ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.ListGroup(
                            [
                                dbc.ListGroupItem("Sum of Co21EmisFR: "+str(sumfr1),className="text-primary"),
                                dbc.ListGroupItem("Sum of Co22EmisFR: "+str(sumfr2),className="text-primary"),
                                dbc.ListGroupItem("Sum of Co21EmisUK: "+str(sumuk1),className="text-danger"),
                                dbc.ListGroupItem("Sum of Co22EmisUK: "+str(sumuk2),className="text-danger"),
                            ],flush=True,),style={"width": "18rem"},className="mr-3"
                    )
                ])
            ])
            ]),
        dbc.Card([
        dbc.CardBody([
                dbc.CardHeader("Line Graph",className="w-25 text-white border border-light"),
                html.P(id="dates-datee2",children=[],className="text-white"),
                html.P(id="count-dp2",children=[],className="text-white"),
                dcc.Graph(id="line-graph2",figure={},className="mt-3"),
                html.Center(
                    dcc.RangeSlider(
                    id="my-slider2",
                    min=0,
                    max=44581,
                    allowCross=False,
                    step=1,
                    value=[0,44581],
                    className="mt-3 w-50"
                )
                )
            ])
    ],className="mt-4 bg-secondary border border-light")
])
],className="bg-secondary")


@app.callback(Output("line-graph2","figure"),Output("dates-datee2","children"),Output("count-dp2","children"),Input("countries-dpdn2","value"),Input("my-slider2","value"),Input("graph-type","value"))
def update_df(dpdn_option_c,value1,value2):
    dff=Co2Emis
    print(dpdn_option_c)

    if dpdn_option_c=="UK" and value2=="single":
        filtered_df = dff.iloc[value1[0]:value1[1] + 1, :]
        fig=px.line(data_frame=filtered_df,x=filtered_df.index,y=["Co21EmisUK","Co22EmisUK"])
        fig.update_layout(title_text="United Kingdom",title_font_size=30,title_x=0.5,title_font_color="red")
        fig.update_yaxes(title_font_color="red")
        fig.update_xaxes(title_text="")

        text1="Start Date: "+str(filtered_df.index[0])+" "+"End Date: "+str(filtered_df.index[-1])
        text2="Data Points in Current Graph"+" "+str(len(filtered_df.index))

        return fig,text1,text2

    elif dpdn_option_c=="UK" and value2=="side":
        filtered_df = dff.iloc[value1[0]:value1[1] + 1, :]
        fig1 = px.line(filtered_df)
        fig2 = px.line(filtered_df)
        trace1 = fig1['data'][1]
        trace2 = fig2['data'][3]
        fig = make_subplots(rows=1, cols=2, shared_xaxes=False)
        fig.add_trace(trace1, row=1, col=1)
        fig.add_trace(trace2, row=1, col=2)
        fig.update_layout(title_text="United Kingdom",title_font_size=30,title_x=0.5,title_font_color="red")
        fig.update_yaxes(title_font_color="red")
        fig.update_xaxes(title_text="")

        text1="Start Date: "+str(filtered_df.index[0])+" "+"End Date: "+str(filtered_df.index[-1])
        text2="Data Points in Current Graph"+" "+str(len(filtered_df.index))

        return fig,text1,text2

    elif dpdn_option_c=="FR" and value2=="single":
        filtered_df = dff.iloc[value1[0]:value1[1] + 1, :]
        fig=px.line(data_frame=filtered_df,x=filtered_df.index,y=["Co21EmisFR","Co22EmisFR"])
        fig.update_layout(title_text="France",title_font_size=30,title_x=0.5,title_font_color="blue")
        fig.update_yaxes(title_font_color="blue")
        fig.update_xaxes(title_text="")

        text1="Start Date: "+str(filtered_df.index[0])+" "+"End Date: "+str(filtered_df.index[-1])
        text2="Data Points in Current Graph"+" "+str(len(filtered_df.index))

        return fig,text1,text2

    elif dpdn_option_c=="FR" and value2=="side":
        filtered_df = dff.iloc[value1[0]:value1[1] + 1, :]
        fig1 = px.line(filtered_df)
        fig2 = px.line(filtered_df)
        trace1 = fig1['data'][0]
        trace2 = fig2['data'][2]
        fig = make_subplots(rows=1, cols=2, shared_xaxes=False)
        fig.add_trace(trace1, row=1, col=1)
        fig.add_trace(trace2, row=1, col=2)
        fig.update_layout(title_text="France",title_font_size=30,title_x=0.5,title_font_color="blue")
        fig.update_yaxes(title_font_color="blue")
        fig.update_xaxes(title_text="")

        text1="Start Date: "+str(filtered_df.index[0])+" "+"End Date: "+str(filtered_df.index[-1])
        text2="Data Points in Current Graph"+" "+str(len(filtered_df.index))

        return fig,text1,text2





