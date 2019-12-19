import pandas as pd

def get_sota_dict(df):
    sota_dict = {}

    for column_name in df.columns.values.tolist():
        if "paper_" in column_name or "agent_" in column_name or "Unnamed" in column_name:
            continue
        max_row_index = df[column_name].idxmax(axis=1)
        sota_dict[column_name] = {
            "agent_fullname": df.iloc[max_row_index]["agent_fullname"],
            "agent_nickname": df.iloc[max_row_index]["agent_nickname"],
            "score": df.iloc[max_row_index][column_name],
        }

    return sota_dict


if __name__ == "__main__":
    df = pd.read_csv("merged_df.csv")
    sota_dict = get_sota_dict(df)
    print(sota_dict)
