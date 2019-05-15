from .algo__dqn import entries as dqn_entries
from .algo__ddqn import entries as ddqn_entries
from .algo__c51 import entries as c51_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "A Distributional Perspective on Reinforcement Learning",
    "source-nickname": "C51",
    "source-authors": [
        "Marc G. Bellemare",
        "Will Dabney",
        "Rémi Munos",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1707.06887",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1707.06887.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1707.06887",
    "source-arxiv-version": 1,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/BellemareDM17,
    author    = {Marc G. Bellemare and
                 Will Dabney and
                 R{\'{e}}mi Munos},
    title     = {A Distributional Perspective on Reinforcement Learning},
    journal   = {CoRR},
    volume    = {abs/1707.06887},
    year      = {2017},
    url       = {http://arxiv.org/abs/1707.06887},
    archivePrefix = {arXiv},
    eprint    = {1707.06887},
    timestamp = {Mon, 13 Aug 2018 16:48:34 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/BellemareDM17},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + dqn_entries
    + ddqn_entries
    + c51_entries
)

entries = [{**entry, **source} for entry in entries]
