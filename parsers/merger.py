import pandas as pd

from pdf_parser_1312_5602 import PDFParser_1312_5602
from pdf_parser_1911_08265 import PDFParser_1911_08265


def merge(parsers):
    dfs = [parser.df for parser in parsers]
    merged_df = pd.concat(dfs)

    return merged_df


if __name__ == "__main__":
    parsers = [
        PDFParser_1312_5602(),
        PDFParser_1911_08265(),
    ]

    merged_df = merge(parsers)
    print(merged_df)
