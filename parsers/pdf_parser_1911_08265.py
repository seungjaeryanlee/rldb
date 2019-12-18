import camelot

from pdf_parser import PDFParser


class PDFParser_1911_08265(PDFParser):
    def _preprocess(self):
        tables = camelot.read_pdf("../pdfs/1911.08265.pdf", pages="17,18", flavor="stream")
        # TODO(seungjaeryanlee) Two tables!
        self.df, self.report = tables[0].df, tables[0].parsing_report
        self.df = self.df.iloc[:-1].drop(columns=[7])
        self.df = self.df.T
        self.df = self._remove_index_and_header(self.df)
        self.df = self._remove_commas(self.df)
        self.df = self._standardize_env_names(self.df)
        self.df = self._unicode_to_ascii_minus_sign(self.df)
        self.df = self._hyphen_to_nan(self.df)
        self.df = self._to_float_type(self.df)

        # Remove citation marks
        self.df.rename(index={
            "SimPLe [20]": "SimPLe",
            "Ape-X [18]": "Ape-X",
            "R2D2 [21]": "R2D2",
        }, inplace=True)

        self._add_paper_metadata(
            title="Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model",
            authors="Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert, Karen Simonyan, Laurent Sifre, Simon Schmitt, Arthur Guez, Edward Lockhart, Demis Hassabis, Thore Graepel, Timothy Lillicrap, David Silver",
            link="https://arxiv.org/abs/1911.08265",
            arxiv_id="1911.08265",
            arxiv_version=1,
            bibtex="""
            @misc{1911.08265,
                Author = {Julian Schrittwieser and Ioannis Antonoglou and Thomas Hubert and Karen Simonyan and Laurent Sifre and Simon Schmitt and Arthur Guez and Edward Lockhart and Demis Hassabis and Thore Graepel and Timothy Lillicrap and David Silver},
                Title = {Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model},
                Year = {2019},
                Eprint = {arXiv:1911.08265},
            }""",
        )
        self._pre_add_agent_metadata()
        self._add_agent_metadata("Random", fullname="Random", nickname="Random")
        self._add_agent_metadata("Human", fullname="Human", nickname="Human")
        self._add_agent_metadata("SimPLe", fullname="Simulated Policy Learning", nickname="SimPLe")
        self._add_agent_metadata("Ape-X", fullname="Ape-X", nickname="Ape-X")
        self._add_agent_metadata("R2D2", fullname="Recurrent Replay Distributed Deep Q-Network", nickname="R2D2")
        self._add_agent_metadata("MuZero", fullname="MuZero", nickname="MuZero")

if __name__ == "__main__":
    parser = PDFParser_1911_08265()
    print(parser.df)
    print(parser.report)
