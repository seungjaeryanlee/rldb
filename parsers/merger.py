import pandas as pd

from pdf_parser_1312_5602 import PDFParser_1312_5602
from pdf_parser_1911_08265 import PDFParser_1911_08265
from pdf_parser_dqn import PDFParser_DQN

def merge(parsers):
    dfs = [parser.df for parser in parsers]
    merged_df = pd.concat(dfs, sort=True)

    return merged_df


if __name__ == "__main__":
    parsers = [
        PDFParser_1312_5602(),
        PDFParser_1911_08265(),
        PDFParser_DQN(),
    ]

    merged_df = merge(parsers)
    merged_df.to_csv("merged_df.csv")
    print(merged_df)
