import plotly.express as px
import pandas as pd


for prefix in ["", "ff_"]:
    df = pd.read_csv(f"csv/{prefix}data_boxplot.csv")
    fig = px.box(df, x="A", y=df.columns[1:], title="", labels={"A":"", "value": "Time in seconds"}, log_y=True)
    fig.update_layout(
        legend=dict(
            title=None,
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        font=dict(
            size=18
        )
    )
    fig.update_xaxes(
        title_font = {"size": 20},
        title_standoff = 0)
    fig.update_yaxes(
        title_font = {"size": 20})
    fig.write_html(f"html/{prefix}boxplot_overhead.html")
    # Needs pip install -U kaleido
    fig.write_image(f"images/{prefix}boxplot_overhead.png")
