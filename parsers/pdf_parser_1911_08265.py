import camelot

from pdf_parser import PDFParser


class PDFParser_1911_08265(PDFParser):
    def _preprocess(self):
        tables = camelot.read_pdf("../pdfs/1911.08265.pdf", pages="17,18", flavor="stream")
        df = tables[0].df
        df = df.iloc[:-1].drop(columns=[7])
        df = self._remove_index_and_header(df)
        df = self._remove_commas(df)
        df = self._standardize_env_names(df)

        report = tables[0].parsing_report

        self.df, self.report = df, report


if __name__ == "__main__":
    parser = PDFParser_1911_08265()
    print(parser.df)
    print(parser.report)
