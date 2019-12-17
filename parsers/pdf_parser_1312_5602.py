import camelot

from pdf_parser import PDFParser


class PDFParser_1312_5602(PDFParser):
    def _preprocess(self):
        tables = camelot.read_pdf("../pdfs/1312.5602.pdf", pages="8", flavor="lattice")
        df = tables[0].df
        df = df.T
        df = self._remove_index_and_header(df)
        df = self._remove_commas(df)
        df = self._standardize_env_names(df)

        report = tables[0].parsing_report

        self.df, self.report = df, report


if __name__ == "__main__":
    parser = PDFParser_1312_5602()
    print(parser.df)
    print(parser.report)
