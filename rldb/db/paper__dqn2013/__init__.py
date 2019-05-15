from .algo__contingency import entries as contingency_entries
from .algo__dqn2013 import entries as dqn2013_entries
from .algo__dqn2013_best import entries as dqn2013_best_entries
from .algo__hneat_best import entries as hneat_best_entries
from .algo__hneat_pixel import entries as hneat_pixel_entries
from .algo__human import entries as human_entries
from .algo__random import entries as random_entries
from .algo__sarsa import entries as sarsa_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Playing Atari with Deep Reinforcement Learning",
    "source-nickname": "DQN2013",
    "source-authors": [
        "Volodymyr Mnih",
        "Koray Kavukcuoglu",
        "David Silver",
        "Alex Graves",
        "Ioannis Antonoglou",
        "Daan Wierstra",
        "Martin Riedmiller",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1312.5602",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1312.5602.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1312.5602",
    "source-arxiv-version": 1,

    #  MISC.
    "source-bibtex": """\
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
}

# Populate entries
entries = (
    []
    + contingency_entries
    + dqn2013_entries
    + dqn2013_best_entries
    + hneat_best_entries
    + hneat_pixel_entries
    + human_entries
    + random_entries
    + sarsa_entries
)
entries = [{**entry, **source} for entry in entries]
