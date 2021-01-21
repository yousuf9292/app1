import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Output,Input
from app import app




uk=pd.read_csv("C:\\Users\\yousuf\\Desktop\\pythonProject\\datasets\\uk2.csv",index_col="date")

print(uk.head())



fr=pd.read_csv("C:\\Users\\yousuf\\Desktop\\pythonProject\\datasets\\fr2.csv",index_col="date")

print(fr.head())





layout=dbc.Card([
    dbc.CardBody([
    html.H1("Prosomateur",className="card-title text-center text-white border border-light"),
    dcc.Dropdown(id="countries-dpdn1",options=[
                                              {'label':"United Kingdom","value":"UK"},
                                              {'label':"France","value":"FR"},
                                              ],value="UK",clearable=False,className="mt-3 w-25"
                 ),

    dcc.Dropdown(id="variable-dpdn1",options=[
        {"label":"EnergyRest","value":"energyRest"},
        {"label":"Co2","value":"Co2Emis"},
        {"label":"Price","value":"price_"},
        {"label":"PowerFromGrid","value":"PowerFromGrid"},

    ],value="Co2Emis",clearable=False,className="mt-3 w-25"),

    dbc.Card([
        dbc.CardBody([
                dbc.CardHeader("Line Graph",className="w-25 text-white border border-light"),
                html.P(id="dates-datee1",children=[],className="text-white"),
                html.P(id="count-dp1",children=[],className="text-white"),
                dcc.Graph(id="line-graph1",figure={},className="mt-3"),
               html.Center(
                   dcc.RangeSlider(
                       id="my-slider1",
                       min=0,
                       max=44581,
                       allowCross=False,
                       step=1,
                       value=[0, 44581],
                       className="mt-3 w-50",
                   ),
               )
            ],className="border border-light")
    ],className="mt-4 bg-secondary")
])
],className="bg-secondary")





@app.callback(Output("line-graph1","figure"),Output("dates-datee1","children"),Output("count-dp1","children"),Input("countries-dpdn1","value"),Input("variable-dpdn1","value"),Input("my-slider1","value"))
def update_df(dpdn_option_c,dpdn_option_v,value):
    ukk=uk
    frr=fr
    print(dpdn_option_v)
    print(dpdn_option_c)
    print(value)

    if dpdn_option_c=="UK":
        filtered_uk = ukk.iloc[value[0]:value[1] + 1, :]
        # print(filtered_uk.index[0],filtered_uk.index[-1])
        # print(len(filtered_uk.index))
        fig=px.line(data_frame=filtered_uk,x=filtered_uk.index,y=dpdn_option_v+dpdn_option_c)
        fig.update_traces(line_color='red')
        fig.update_layout(title_text="United Kingdom",title_font_size=30,title_x=0.5,title_font_color="red")
        fig.update_yaxes(title_font_color="red")
        fig.update_xaxes(title_text="")

        text1="Start Date: "+str(filtered_uk.index[0])+" "+"End Date: "+str(filtered_uk.index[-1])
        text2="Data Points in Current Graph"+" "+str(len(filtered_uk.index))

        return fig,text1,text2

    elif dpdn_option_c=="FR":
        filtered_fr = frr.iloc[value[0]:value[1] + 1, :]
        fig=px.line(data_frame=filtered_fr,x=filtered_fr.index,y=dpdn_option_v+dpdn_option_c)
        fig.update_traces(line_color='blue')
        fig.update_layout(title_text="France",title_font_size=30,title_x=0.5,title_font_color="blue")
        fig.update_yaxes(title_font_color="blue")
        fig.update_xaxes(title_text="")

        text1="Start Date: "+str(filtered_fr.index[0])+" "+"End Date: "+str(filtered_fr.index[-1])
        text2="Data Points in Current Graph"+" "+str(len(filtered_fr.index))

        return fig,text1,text2










