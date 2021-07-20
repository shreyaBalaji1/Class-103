import pandas as pd
import plotly.express as px

data = [1,2,3,4,5]
#df = pd.DataFrame(data)
df = pd.read_csv("line_chart.csv")

fig = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per Captia Income")

fig.show()
