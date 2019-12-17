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

    def _remove_commas(self, df):
        df = df.replace(',','', regex=True)

        return df

    def _standardize_env_names(self, df):
        df.index = df.index.str.lower()
        df.index = df.index.str.replace('[^A-Za-z\d ]+', '')

        df = df.rename(index={
            "b rider": "beam rider",
            "s invaders": "space invaders",
        })
        
        return df

    def _preprocess(self):
        raise NotImplementedError("You can only initialize children of PDFParser that defines _preprocess().")
