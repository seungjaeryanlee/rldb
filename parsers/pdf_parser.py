import numpy as np
import textwrap


class PDFParser:
    def __init__(self):
        self.df = None
        self.report = None

        self._format_df()

    def _remove_index_and_header(self, df):
        df = df.set_index(0)
        del df.index.name
        df = df.rename(columns=df.iloc[0]).drop(df.index[0])

        return df

    def _standardize_env_names(self, df):
        df.columns = df.columns.str.lower() # Lowercase
        df.columns = df.columns.str.replace('[^A-Za-z\d]+', '') # Alphanumeric

        df = df.rename(columns={
            "brider": "beamrider",
            "sinvaders": "spaceinvaders",
        })

        return df

    def _standardize_scores(self, df):
        df = df.replace("−", "-", regex=True) # Fix unicode minus signs
        df = df.replace("-", np.nan) # Use NaN for no score
        df = df.replace(',','', regex=True) # Remove commas in numbers
        df = df.astype(float) # Number format

        return df

    def _format_df(self):
        raise NotImplementedError("You can only initialize children of PDFParser that defines _preprocess().")

    def as_dict(self):
        return {
            "df": self.df.to_dict(),
            "report": self.report,
        }

    def _add_paper_metadata(self, title, authors, link, arxiv_id, arxiv_version, bibtex):
        self.df["metadata_paper_title"] = title
        self.df["metadata_paper_authors"] = authors
        self.df["metadata_paper_link"] = link
        self.df["metadata_paper_arxiv_id"] = arxiv_id
        self.df["metadata_paper_arxiv_version"] = arxiv_version
        self.df["metadata_paper_bibtex"] = textwrap.dedent(bibtex)

    def _pre_add_agent_metadata(self):
        self.df["metadata_agent_fullname"] = ""
        self.df["metadata_agent_nickname"] = ""

    def _add_agent_metadata(self, row_index, fullname, nickname):
        self.df.loc[row_index, "metadata_agent_fullname"] = fullname
        self.df.loc[row_index, "metadata_agent_nickname"] = nickname
