from .algo__random import entries as random_entries
from .algo__human import entries as human_entries
from .algo__ddqn import entries as ddqn_entries
from .algo__ddqn_tuned import entries as ddqn_tuned_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Deep Reinforcement Learning with Double Q-learning",
    "source-nickname": "DDQN",
    "source-authors": [
        "Hando van Hasselt",
        "Arthur Guez",
        "David Silver",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1509.06461",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1509.06461.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1509.06461",
    "source-arxiv-version": 3,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/HasseltGS15,
    author    = {Hado van Hasselt and
                 Arthur Guez and
                 David Silver},
    title     = {Deep Reinforcement Learning with Double Q-learning},
    journal   = {CoRR},
    volume    = {abs/1509.06461},
    year      = {2015},
    url       = {http://arxiv.org/abs/1509.06461},
    archivePrefix = {arXiv},
    eprint    = {1509.06461},
    timestamp = {Mon, 13 Aug 2018 16:47:32 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/HasseltGS15},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + random_entries
    + human_entries
    + ddqn_entries
    + ddqn_tuned_entries
)
entries = [{**entry, **source} for entry in entries]
