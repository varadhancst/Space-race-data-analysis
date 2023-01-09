import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("mission_launches.csv", encoding="utf-8")
# print(df.head())
print(df.columns)

df = df.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)
# df.head()
# df.describe()
# df.info()
ds = df["Organisation"].value_counts().reset_index()[:30]
# ds.head()

fig = go.Figure(
    go.Bar(x=ds["index"], y=ds["Organisation"], marker=dict(color=ds["Organisation"], colorscale="bluered")))
fig.update_layout(title="Number of Launches by Every Company", xaxis_title="Top 28 Country", yaxis_title="count",
                  hovermode="x")
fig.show()


ds = df["Organisation"].value_counts().reset_index()[:10]

fig = px.pie(ds, values="Organisation", names="index", title="Organisation")
fig.show()
