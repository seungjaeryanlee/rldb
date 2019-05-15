from .algo__dudqn import entries as dudqn_entries
from .algo__human import entries as human_entries
from .algo__pdd_dqn import entries as pdd_dqn_entries
from .algo__random import entries as random_entries



# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Dueling Network Architectures for Deep Reinforcement Learning",
    "source-nickname": "DuDQN",
    "source-authors": [
        "Ziyu Wang",
        "Tom Schaul",
        "Matteo Hessel",
        "Hado van Hasselt",
        "Marc Lanctot",
        "Nando de Freitas",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1511.06581",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1511.06581.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1511.06581",
    "source-arxiv-version": 3,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/WangFL15,
    author    = {Ziyu Wang and
                 Nando de Freitas and
                 Marc Lanctot},
    title     = {Dueling Network Architectures for Deep Reinforcement Learning},
    journal   = {CoRR},
    volume    = {abs/1511.06581},
    year      = {2015},
    url       = {http://arxiv.org/abs/1511.06581},
    archivePrefix = {arXiv},
    eprint    = {1511.06581},
    timestamp = {Mon, 13 Aug 2018 16:48:17 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/WangFL15},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + dudqn_entries
    + human_entries
    + pdd_dqn_entries
    + random_entries
)
entries = [{**entry, **source} for entry in entries]
