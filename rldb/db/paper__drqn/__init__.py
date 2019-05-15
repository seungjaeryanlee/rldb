from .algo__dqn_ours import entries as dqn_ours_entries
from .algo__drqn import entries as drqn_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Deep Recurrent Q-Learning for Partially Observable MDPs",
    "source-nickname": "DRQN",
    "source-authors": [
        "Matthew Hausknecht",
        "Peter Stone",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1507.06527",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1507.06527.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1507.06527",
    "source-arxiv-version": 4,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/HausknechtS15,
    author    = {Matthew J. Hausknecht and
                 Peter Stone},
    title     = {Deep Recurrent Q-Learning for Partially Observable MDPs},
    journal   = {CoRR},
    volume    = {abs/1507.06527},
    year      = {2015},
    url       = {http://arxiv.org/abs/1507.06527},
    archivePrefix = {arXiv},
    eprint    = {1507.06527},
    timestamp = {Mon, 13 Aug 2018 16:48:38 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/HausknechtS15},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + dqn_ours_entries
    + drqn_entries
)
entries = [{**entry, **source} for entry in entries]
