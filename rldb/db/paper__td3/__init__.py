from .algo__acktr import entries as acktr_entries
from .algo__ddpg import entries as ddpg_entries
from .algo__our_ddpg import entries as our_ddpg_entries
from .algo__ppo import entries as ppo_entries
from .algo__sac import entries as sac_entries
from .algo__td3 import entries as td3_entries
from .algo__trpo import entries as trpo_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Addressing Function Approximation Error in Actor-Critic Methods",
    "source-nickname": "TD3",
    "source-authors": [
        "Scott Fujimoto",
        "Herke van Hoof",
        "David Meger",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1802.09477",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1802.09477.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1802.09477",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1802-09477,
    author    = {Scott Fujimoto and
                 Herke van Hoof and
                 Dave Meger},
    title     = {Addressing Function Approximation Error in Actor-Critic Methods},
    journal   = {CoRR},
    volume    = {abs/1802.09477},
    year      = {2018},
    url       = {http://arxiv.org/abs/1802.09477},
    archivePrefix = {arXiv},
    eprint    = {1802.09477},
    timestamp = {Mon, 13 Aug 2018 16:47:21 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1802-09477},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + acktr_entries
    + ddpg_entries
    + our_ddpg_entries
    + ppo_entries
    + sac_entries
    + td3_entries
    + trpo_entries
)
entries = [{**entry, **source} for entry in entries]
