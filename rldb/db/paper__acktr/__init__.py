from .algo__acktr import entries as acktr_entries
from .algo__a2c import entries as a2c_entries
from .algo__trpo import entries as trpo_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation",
    "source-nickname": "ACKTR",
    "source-authors": [
        "Yuhuai Wu",
        "Elman Mansimov",
        "Shun Liao",
        "Roger Grosse",
        "Jimmy Ba",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1708.05144",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1708.05144.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1708.05144",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1708-05144,
    author    = {Yuhuai Wu and
                 Elman Mansimov and
                 Shun Liao and
                 Roger B. Grosse and
                 Jimmy Ba},
    title     = {Scalable trust-region method for deep reinforcement learning using
                 Kronecker-factored approximation},
    journal   = {CoRR},
    volume    = {abs/1708.05144},
    year      = {2017},
    url       = {http://arxiv.org/abs/1708.05144},
    archivePrefix = {arXiv},
    eprint    = {1708.05144},
    timestamp = {Mon, 13 Aug 2018 16:48:28 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1708-05144},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + acktr_entries
    + a2c_entries
    + trpo_entries
)
entries = [{**entry, **source} for entry in entries]
