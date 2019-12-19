import pandas as pd
import numpy as np

from pdf_parser import PDFParser


class PDFParser_DQN(PDFParser):
    def _format_df(self):
        df = pd.DataFrame([
            ["Game", "Random Play", "Best Linear Learner", "Contingency (SARSA)", "Human", "DQN",],
            ["Alien", 227.8, 939.2, 103.2, 6875, 3069],
            ["Amidar", 5.8, 103.4, 183.6, 1676, 739.5],
            ["Assault", 222.4, 628, 537, 1496, 3359],
            ["Asterix", 210, 987.3, 1332, 8503, 6012],
            ["Asteroids", 719.1, 907.3, 89, 13157, 1629],
            ["Atlantis", 12850, 62687, 852.9, 29028, 85641],
            ["Bank Heist", 14.2, 190.8, 67.4, 734.4, 429.7],
            ["Battle Zone", 2360, 15820, 16.2, 37800, 26300],
            ["Beam Rider", 363.9, 929.4, 1743, 5775, 6846],
            ["Bowling", 23.1, 43.9, 36.4, 154.8, 42.4],
            ["Boxing", 0.1, 44, 9.8, 4.3, 71.8],
            ["Breakout", 1.7, 5.2, 6.1, 31.8, 401.2],
            ["Centipede", 2091, 8803, 4647, 11963, 8309],
            ["Chopper Command", 811, 1582, 16.9, 9882, 6687],
            ["Crazy Climber", 10781, 23411, 149.8, 35411, 114103],
            ["Demon Attack", 152.1, 520.5, 0, 3401, 9711],
            ["Double Dunk", -18.6, -13.1, -16, -15.5, -18.1],
            ["Enduro", 0, 129.1, 159.4, 309.6, 301.8],
            ["Fishing Derby", -91.7, -89.5, -85.1, 5.5, -0.8],
            ["Freeway", 0, 19.1, 19.7, 29.6, 30.3],
            ["Frostbite", 65.2, 216.9, 180.9, 4335, 328.3],
            ["Gopher", 257.6, 1288, 2368, 2321, 8520],
            ["Gravitar", 173, 387.7, 429, 2672, 306.7],
            ["H.E.R.O.", 1027, 6459, 7295, 25763, 19950],
            ["Ice Hockey", -11.2, -9.5, -3.2, 0.9, -1.6],
            ["James Bond", 29, 202.8, 354.1, 406.7, 576.7],
            ["Kangaroo", 52, 1622, 8.8, 3035, 6740],
            ["Krull", 1598, 3372, 3341, 2395, 3805],
            ["Kung-Fu Master", 258.5, 19544, 29151, 22736, 23270],
            ["Montezuma's Revenge", 0, 10.7, 259, 4367, 0],
            ["Ms. Pacman", 307.3, 1692, 1227, 15693, 2311],
            ["Name This Game", 2292, 2500, 2247, 4076, 7257],
            ["Pong", -20.7, -19, -17.4, 9.3, 18.9],
            ["Private Eye", 24.9, 684.3, 86, 69571, 1788],
            ["Q*Bert", 163.9, 613.5, 960.3, 13455, 10596],
            ["River Raid", 1339, 1904, 2650, 13513, 8316],
            ["Road Runner", 11.5, 67.7, 89.1, 7845, 18257],
            ["Robotank", 2.2, 28.7, 12.4, 11.9, 51.6],
            ["Seaquest", 68.4, 664.8, 675.5, 20182, 5286],
            ["Space Invaders", 148, 250.1, 267.9, 1652, 1976],
            ["Star Gunner", 664, 1070, 9.4, 10250, 57997],
            ["Tennis", -23.8, -0.1, 0, -8.9, -2.5],
            ["Time Pilot", 3568, 3741, 24.9, 5925, 5947],
            ["Tutankham", 11.4, 114.3, 98.2, 167.6, 186.7],
            ["Up and Down", 533.4, 3533, 2449, 9082, 8456],
            ["Venture", 0, 66, 0.6, 1188, 380.0],
            ["Video Pinball", 16257, 16871, 19761, 17298, 42684],
            ["Wizard of Wor", 563.5, 1981, 36.9, 4757, 3393],
            ["Zaxxon", 32.5, 3365, 21.4, 9173, 4977],
        ])
        print(df)
        df = df.T
        df = self._remove_index_and_header(df)
        df = self._standardize_env_names(df)
        df = self._standardize_scores(df)
        df = df.add_suffix("_noop")
        self.df = df

        print(self.df)

        # Remove citation marks
        self.df.rename(index={
            "Random Play": "Random",
        }, inplace=True)

        self._add_paper_metadata(
            title="Human-level control through deep reinforcement learning",
            authors="Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, Demis Hassabis",
            link="https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf",
            arxiv_id=np.nan,
            arxiv_version=np.nan,
            bibtex="""
            @article{DQN,
                author = {Mnih, Volodymyr and Kavukcuoglu, Koray and Silver, David and Rusu, Andrei A. and Veness, Joel and Bellemare, Marc G. and Graves, Alex and Riedmiller, Martin and Fidjeland, Andreas K. and Ostrovski, Georg and Petersen, Stig and Beattie, Charles and Sadik, Amir and Antonoglou, Ioannis and King, Helen and Kumaran, Dharshan and Wierstra, Daan and Legg, Shane and Hassabis, Demis},
                issn = {00280836},
                journal = {Nature},
                month = feb,
                number = 7540,
                pages = {529--533},
                publisher = {Nature Publishing Group, a division of Macmillan Publishers Limited. All Rights Reserved.},
                timestamp = {2015-08-26T14:46:40.000+0200},
                title = {Human-level control through deep reinforcement learning},
                url = {http://dx.doi.org/10.1038/nature14236},
                volume = 518,
                year = 2015
            }""",
        )
        self._pre_add_agent_metadata()
        self._add_agent_metadata("Random", fullname="Random", nickname="Random")
        self._add_agent_metadata("Best Linear Learner", fullname="Best Linear Learner", nickname="Linear")
        self._add_agent_metadata("Contingency (SARSA)", fullname="Contingency (SARSA)", nickname="Contingency")
        self._add_agent_metadata("Human", fullname="Human", nickname="Human")
        self._add_agent_metadata("DQN", fullname="Deep Q-Network", nickname="DQN")

if __name__ == "__main__":
    parser = PDFParser_DQN()
    print(parser.df)
