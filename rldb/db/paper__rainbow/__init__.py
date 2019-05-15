from .algo__dqn import entries as dqn_entries
from .algo__distributional_dqn import entries as distributional_dqn_entries
from .algo__rainbow import entries as rainbow_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Rainbow: Combining Improvements in Deep Reinforcement Learning",
    "source-nickname": "Rainbow",
    "source-authors": [
        "Matteo Hessel",
        "Joseph Modayil",
        "Hado van Hasselt",
        "Tom Schaul",
        "Georg Ostrovski",
        "Will Dabney",
        "Dan Horgan",
        "Bilal Piot",
        "Mohammad Azar",
        "David Silver",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1710.02298",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1710.02298.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1710.02298",
    "source-arxiv-version": 1,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1710-02298,
    author    = {Matteo Hessel and
                 Joseph Modayil and
                 Hado van Hasselt and
                 Tom Schaul and
                 Georg Ostrovski and
                 Will Dabney and
                 Daniel Horgan and
                 Bilal Piot and
                 Mohammad Gheshlaghi Azar and
                 David Silver},
    title     = {Rainbow: Combining Improvements in Deep Reinforcement Learning},
    journal   = {CoRR},
    volume    = {abs/1710.02298},
    year      = {2017},
    url       = {http://arxiv.org/abs/1710.02298},
    archivePrefix = {arXiv},
    eprint    = {1710.02298},
    timestamp = {Mon, 13 Aug 2018 16:48:05 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-02298},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + dqn_entries
    + distributional_dqn_entries
    + rainbow_entries
)
entries = [{**entry, **source} for entry in entries]
