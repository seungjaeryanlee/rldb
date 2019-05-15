from .algo__random import entries as random_entries
from .algo__human import entries as human_entries
from .algo__dqn import entries as dqn_entries
from .algo__gorila_dqn import entries as gorila_dqn_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Massively Parallel Methods for Deep Reinforcement Learning",
    "source-nickname": "Gorila DQN",
    "source-authors": [
        "Arun Nair",
        "Praveen Srinivasan",
        "Sam Blackwell",
        "Cagdas Alcicek",
        "Rory Fearon",
        "Alessandro De Maria",
        "Vedavyas Panneershelvam",
        "Mustafa Suleyman",
        "Charles Beattie",
        "Stig Petersen",
        "Shane Legg",
        "Volodymyr Mnih",
        "Koray Kavukcuoglu",
        "David Silver",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1507.04296",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1507.04296.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1507.04296",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/NairSBAFMPSBPLM15,
  author    = {Arun Nair and
               Praveen Srinivasan and
               Sam Blackwell and
               Cagdas Alcicek and
               Rory Fearon and
               Alessandro De Maria and
               Vedavyas Panneershelvam and
               Mustafa Suleyman and
               Charles Beattie and
               Stig Petersen and
               Shane Legg and
               Volodymyr Mnih and
               Koray Kavukcuoglu and
               David Silver},
  title     = {Massively Parallel Methods for Deep Reinforcement Learning},
  journal   = {CoRR},
  volume    = {abs/1507.04296},
  year      = {2015},
  url       = {http://arxiv.org/abs/1507.04296},
  archivePrefix = {arXiv},
  eprint    = {1507.04296},
  timestamp = {Mon, 13 Aug 2018 16:46:14 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/NairSBAFMPSBPLM15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + random_entries
    + human_entries
    + dqn_entries
    + gorila_dqn_entries
)
entries = [{**entry, **source} for entry in entries]
