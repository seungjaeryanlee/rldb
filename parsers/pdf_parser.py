class PDFParser:
    def __init__(self):
        self.df = None
        self.report = None

        self._preprocess()

    def _preprocess(self):
        raise NotImplementedError("You can only initialize children of PDFParser that defines _preprocess().")
