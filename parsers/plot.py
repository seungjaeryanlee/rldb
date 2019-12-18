import pandas as pd
import plotly.graph_objects as go


def plot_single_env(df, env_name):
    df = df.dropna(subset=[env_name])
    df = df.sort_values(by=[env_name], ascending=True)
    fig = go.Figure([go.Bar(x=df["agent_name"]+": "+df["paper_title"], y=df[env_name])])
    fig.show()


if __name__ == "__main__":
    df = pd.read_csv("merged_df.csv")
    plot_single_env(df, "skiing")
