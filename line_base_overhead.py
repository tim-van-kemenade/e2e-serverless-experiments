import plotly.express as px
import pandas as pd

df = pd.read_csv("csv/data_line.csv")
fig = px.line(df, x="A", y=df.columns[1:], title="End-to-End sequential call overhead", labels={"A":"Calls", "value": "Time in seconds"})
fig.write_html("html/line_overhead.html")
# Needs pip install -U kaleido
fig.write_image("images/line_overhead.png")
