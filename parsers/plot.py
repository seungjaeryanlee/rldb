import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py


def plot_single_env(df, env_name, online):
    df = df.dropna(subset=[env_name])
    df = df.sort_values(by=[env_name], ascending=True)
    fig = go.Figure([go.Bar(
        x=df["metadata_agent_nickname"] + df["metadata_paper_title"],
        y=df[env_name],
        text=df[env_name],
        textposition='auto',
        hovertext="<b>Paper: </b>" + df["metadata_paper_title"] + "<br><b>Agent: </b>" + df["metadata_agent_fullname"],
    )])
    fig.update_layout(
        barmode='group',
        xaxis=dict(
            tickmode="array",
            tickvals=df["metadata_agent_nickname"] + df["metadata_paper_title"],
            ticktext=df["metadata_agent_nickname"],
        ),
    )
    fig.show()
    py.plot(fig, filename=env_name, auto_open=True)


if __name__ == "__main__":
    df = pd.read_csv("merged_df.csv")
    plot_single_env(df, "skiing", online=True)
