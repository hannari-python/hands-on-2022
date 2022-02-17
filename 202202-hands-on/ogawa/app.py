from dash import Dash, html, dcc, Input, Output
import plotly.express as px


def cal_list(y_list, s_value):
    new_list = list()
    for num, i in enumerate(y_list):
        if num % 2 == 0:
            new_list.append(i + s_value)
        else:
            new_list.append(i - s_value)
    return new_list


app = Dash(__name__)

app.layout = html.Div(
    [
        html.P("はんなりPythonへようこそ!", style={"fontSize": "3rem"}),
        html.Div(
            [dcc.Slider(-5, 5, 1, value=0, id="my_slider", updatemode="drag")],
            style={"width": "80%", "margin": "auto"},
        ),
        html.Div([dcc.Graph(id="my_graph")]),
    ],
    style={"textAlign": "center"},
)


@app.callback(Output("my_graph", "figure"), Input("my_slider", "value"))
def update_graph(s_value):
    x_list = [1, 2, 3, 4, 5]
    y_list = [-2, 2, 3, 1, -1]
    new_list = cal_list(y_list, s_value)
    return px.bar(x=x_list, y=new_list)


if __name__ == "__main__":
    app.run_server(debug=True)
