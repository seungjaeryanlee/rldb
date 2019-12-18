import camelot

from pdf_parser import PDFParser


class PDFParser_1312_5602(PDFParser):
    def _preprocess(self):
        tables = camelot.read_pdf("../pdfs/1312.5602.pdf", pages="8", flavor="lattice")
        self.df, self.report = tables[0].df, tables[0].parsing_report
        self.df = self._remove_index_and_header(self.df)
        self.df = self._remove_commas(self.df)
        self.df = self._standardize_env_names(self.df)
        self.df = self._unicode_to_ascii_minus_sign(self.df)

        # Remove citation marks
        self.df.rename(index={
            "Sarsa [3]": "Sarsa",
            "Contingency [4]": "Contingency",
        }, inplace=True)

        self._add_paper_metadata(
            title="Playing Atari with Deep Reinforcement Learning",
            authors="Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller",
            link="https://arxiv.org/abs/1312.5602",
            arxiv_id="1312.5602",
            arxiv_version=1,
            bibtex="""
            @article{DBLP:journals/corr/MnihKSGAWR13,
                author    = {Volodymyr Mnih and
                            Koray Kavukcuoglu and
                            David Silver and
                            Alex Graves and
                            Ioannis Antonoglou and
                            Daan Wierstra and
                            Martin A. Riedmiller},
                title     = {Playing Atari with Deep Reinforcement Learning},
                journal   = {CoRR},
                volume    = {abs/1312.5602},
                year      = {2013},
                url       = {http://arxiv.org/abs/1312.5602},
                archivePrefix = {arXiv},
                eprint    = {1312.5602},
                timestamp = {Mon, 13 Aug 2018 16:47:42 +0200},
                biburl    = {https://dblp.org/rec/bib/journals/corr/MnihKSGAWR13},
                bibsource = {dblp computer science bibliography, https://dblp.org}
            }""",
        )
        self._pre_add_agent_metadata()
        self._add_agent_metadata("Random", name="Random", nickname="Random")
        self._add_agent_metadata("Sarsa", name="Sarsa", nickname="Sarsa")
        self._add_agent_metadata("Contingency", name="Contingency", nickname="Contingency")
        self._add_agent_metadata("DQN", name="Deep Q-Network", nickname="DQN")
        self._add_agent_metadata("Human", name="Human", nickname="Human")


if __name__ == "__main__":
    parser = PDFParser_1312_5602()
    print(parser.df)
    print(parser.report)
