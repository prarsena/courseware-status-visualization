import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
import math 

app = dash.Dash(__name__)
server = app.server

df = pd.read_csv ('https://raw.githubusercontent.com/prarsena/courseware-status-visualization/main/CourseList.csv')
#df = pd.read_csv ('D:\Sandbox\Progress\coursedata\python\CourseList.csv')

dict_map = {'Beginner': 1, 'Intermediate': 2, 'Advanced': 3}
numericLevel = df["Level"].map(dict_map)
df['NumericLevel'] = numericLevel

#if(math.isnan(df['Details'][0])):
#	print("not a number")

fig = px.scatter(df, x="Title", y="Status", title="Courseware", color="Product", symbol="Persona", size="NumericLevel", size_max=40, category_orders={"Status": ["Done", "In Process", "Planned"]}, custom_data=["Level", "Persona", "Product", "Title", "Details"])

#fig.add_vrect(x0=-1, x1=4.7, line_width=0, fillcolor="#00D5C7", opacity=0.8)
#fig.add_vrect(x0=4.8, x1=14.7, line_width=0, fillcolor="#50DD50", opacity=0.8)
#fig.add_vrect(x0=14.8, x1=23.7, line_width=0, fillcolor="#653DD3", opacity=0.8)
#fig.add_vrect(x0=23.8, x1=32.7, line_width=0, fillcolor="#0051d3", opacity=0.8)
#fig.add_vrect(x0=32.8, x1=33.7, line_width=0, fillcolor="#ffd000", opacity=0.8)
#fig.add_vrect(x0=33.8, x1=35, line_width=0, fillcolor="#ffe600", opacity=0.8)

fig.update_traces(mode="markers", marker=dict(
	opacity=1
), hovertemplate="<br>".join([
	"<br><br><b>Title:</b> %{customdata[3]}",
	"<b>Product:</b> %{customdata[2]}",
	"<b>Status:</b> %{y}",
	"<b>Persona:</b> %{customdata[1]}",
	"<b>Level:</b> %{customdata[0]}",
	"<b>Details:</b> %{customdata[4]}"
]))
fig.update_layout(
	height=600,
		title={
		'text': "Progress Courseware, June 2022",
		'y': 0.9,
		'x': 0.5,
		'xanchor': 'center',
		'yanchor': 'top'
	},
	xaxis= dict(
		tickmode = 'array',
		tickvals = [0, 5, 15, 24, 33, 34],
		ticktext = ['MoveIt', 'WhatsUp Gold', 'Sitefinity', 'OpenEdge', 'Corticon', 'Kemp'],
		tickfont = dict(size=15)
	),
	yaxis = dict(
		tickfont = dict(size=15)
	),
	xaxis_title = "Courses by Product",
	yaxis_title = "Course Status",
	showlegend=True,
	hoverlabel=dict(
		bgcolor="white"
	)
	)

fig.update_xaxes(showticklabels=True, tickangle=0)

fig.show()

########### Set up the layout
app.layout = html.Div(children=[
    dcc.Graph(
        id='courses',
        figure=fig
    )
    ]
)

if __name__ == '__main__':
	app.run_server()