import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import seaborn as sns
import plotly.graph_objects as go


def create_chart_plt(calculations):

    register_matplotlib_converters()
    sns.set()
    pal = sns.color_palette('Set1')
    plt.tight_layout()

    year = [x[0] for x in calculations]
    total_net_worth = [x[1] for x in calculations]
    savings_without_interests = [x[2] for x in calculations]
    net_interests = [x[3] for x in calculations]

    # plt.plot(year, total_net_worth, label='total net worth', color='green')
    # plt.plot(year, savings_without_interests, label='net savings', color='orange')
    # plt.plot(year, net_interests, label='net interests', color='blue')
    plt.stackplot(year, savings_without_interests, net_interests,
                  labels=['net savings', 'net interests'],
                  colors=pal, alpha=0.4)

    plt.xlabel('Year')
    plt.ylabel('Net worth')
    plt.title('Net worth calculations until reaching financial independence')
    plt.legend(loc='upper left')
    plt.show()


def create_chart_interactive(calculations):

    year = [x[0] for x in calculations]
    total_net_worth = [x[1] for x in calculations]
    savings_without_interests = [x[2] for x in calculations]
    net_interests = [x[3] for x in calculations]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=year,
        y=savings_without_interests,
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='rgb(131, 90, 241)'),
        stackgroup='one'
    ))

    fig.add_trace(go.Scatter(
        x=year,
        y=net_interests,
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='rgb(111, 231, 219)'),
        stackgroup='one'
    ))

    fig.add_trace(go.Scatter(
        x=year,
        y=total_net_worth,
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='rgb(0, 0, 0)'),
    ))

    fig.show()




