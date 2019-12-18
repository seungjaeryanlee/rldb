import numpy as np
import textwrap


class PDFParser:
    def __init__(self):
        self.df = None
        self.report = None

        self._preprocess()

    def _to_float_type(self, df):
        return df.astype(float)

    def _hyphen_to_nan(self, df):
        return df.replace("-", np.nan)

    def _remove_index_and_header(self, df):
        df = df.set_index(0)
        del df.index.name
        df = df.rename(columns=df.iloc[0]).drop(df.index[0])

        return df

    def _remove_commas(self, df):
        df = df.replace(',','', regex=True)

        return df

    def _standardize_env_names(self, df):
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace('[^A-Za-z\d ]+', '')

        df = df.rename(columns={
            "b rider": "beam rider",
            "s invaders": "space invaders",
        })

        return df

    def _unicode_to_ascii_minus_sign(self, df):
        df = df.replace("−", "-", regex=True)

        return df

    def _preprocess(self):
        raise NotImplementedError("You can only initialize children of PDFParser that defines _preprocess().")

    def as_dict(self):
        return {
            "df": self.df.to_dict(),
            "report": self.report,
        }

    def _add_paper_metadata(self, title, authors, link, arxiv_id, arxiv_version, bibtex):
        self.df["paper_title"] = title
        self.df["paper_authors"] = authors
        self.df["paper_link"] = link
        self.df["paper_arxiv_id"] = arxiv_id
        self.df["paper_arxiv_version"] = arxiv_version
        self.df["paper_bibtex"] = textwrap.dedent(bibtex)

    def _pre_add_agent_metadata(self):
        self.df["agent_name"] = ""
        self.df["agent_nickname"] = ""

    def _add_agent_metadata(self, row_index, name, nickname):
        self.df.loc[row_index, "agent_name"] = name
        self.df.loc[row_index, "agent_nickname"] = nickname
