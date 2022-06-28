import plotly.express as px
import pandas as pd

df = pd.read_csv ('https://raw.githubusercontent.com/prarsena/courseware-status-visualization/main/CourseListReal.csv')

dict_map = {'Beginner': 1, 'Intermediate': 2, 'Advanced': 3}
numericLevel = df["Level"].map(dict_map)
df['NumericLevel'] = numericLevel

# # dict_map_color = {'Move It': '#00D5C7', 
	# 'WhatsUp Gold': '#50DD50', 
	# 'Sitefinity': '#653DD3',
	# 'OpenEdge': '#0051d3',
	# 'Corticon': '#ffd000',
	# 'Kemp': '#ffe600'}

#pointColor = df["Product"].map(dict_map_color)
#df['ColorLevel'] = pointColor

print(df)

fig = px.scatter(df, x="Title", y="Status", title="Courseware", color="Product", symbol="Persona", size="NumericLevel", size_max=40, category_orders={"Status": ["Done", "In Process", "Planned"]}, custom_data=["Level", "Persona", "Product", "Title"])

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
	"<b>Level:</b> %{customdata[0]}"
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
	showlegend=False,
	hoverlabel=dict(
		bgcolor="white"
	)
	)

fig.update_xaxes(showticklabels=True, tickangle=0)

fig.show()