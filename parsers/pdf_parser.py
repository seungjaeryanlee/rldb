class PDFParser:
    def __init__(self):
        self.df = None
        self.report = None

        self._preprocess()

    def _remove_index_and_header(self, df):
        df = df.set_index(0)
        del df.index.name
        df = df.rename(columns=df.iloc[0]).drop(df.index[0])

        return df

    def _preprocess(self):
        raise NotImplementedError("You can only initialize children of PDFParser that defines _preprocess().")
