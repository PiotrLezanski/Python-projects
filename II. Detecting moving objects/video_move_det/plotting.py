from move_detector import df
from bokeh.plotting import show, figure, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

f = figure(height=350, width=1000, x_axis_type='datetime')

f.title.text = "Motion Graph"
f.title.text_font_size = '15pt'
f.yaxis.minor_tick_line_color = None
f.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])

f.add_tools(hover)
f.quad(left="Start", right="End", bottom=0, top=1, color="Green", source=cds)

output_file('Graph.html')
show(f)

