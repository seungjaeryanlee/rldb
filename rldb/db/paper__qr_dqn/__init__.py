from .algo__qr_dqn_0 import entries as qr_dqn_0_entries
from .algo__qr_dqn_1 import entries as qr_dqn_1_entries

# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Distributional Reinforcement Learning with Quantile Regression",
    "source-nickname": "QR-DQN",
    "source-authors": [
        "Will Dabney",
        "Mark Rowland",
        "Marc G. Bellemare",
        "Rémi Munos",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1710.10044",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1710.10044.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1710.10044",
    "source-arxiv-version": 1,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1710-10044,
    author    = {Will Dabney and
                 Mark Rowland and
                 Marc G. Bellemare and
                 R{\'{e}}mi Munos},
    title     = {Distributional Reinforcement Learning with Quantile Regression},
    journal   = {CoRR},
    volume    = {abs/1710.10044},
    year      = {2017},
    url       = {http://arxiv.org/abs/1710.10044},
    archivePrefix = {arXiv},
    eprint    = {1710.10044},
    timestamp = {Mon, 13 Aug 2018 16:48:27 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-10044},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + qr_dqn_0_entries
    + qr_dqn_1_entries
)
entries = [{**entry, **source} for entry in entries]
