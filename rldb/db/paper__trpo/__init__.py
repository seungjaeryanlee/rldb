from .algo__ucc_i import entries as ucc_i_entries
from .algo__trpo_single_path import entries as trpo_single_path_entries
from .algo__trpo_vine import entries as trpo_vine_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Trust Region Policy Optimization",
    "source-nickname": "TRPO",
    "source-authors": [
        "John Schulman",
        "Sergey Levine",
        "Philipp Moritz",
        "Michael Jordan",
        "Pieter Abbeel",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1502.05477",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1502.05477.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1502.05477",
    "source-arxiv-version": 5,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/SchulmanLMJA15,
    author    = {John Schulman and
                 Sergey Levine and
                 Philipp Moritz and
                 Michael I. Jordan and
                 Pieter Abbeel},
    title     = {Trust Region Policy Optimization},
    journal   = {CoRR},
    volume    = {abs/1502.05477},
    year      = {2015},
    url       = {http://arxiv.org/abs/1502.05477},
    archivePrefix = {arXiv},
    eprint    = {1502.05477},
    timestamp = {Mon, 13 Aug 2018 16:48:08 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/SchulmanLMJA15},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + ucc_i_entries
    + trpo_single_path_entries
    + trpo_vine_entries
)
entries = [{**entry, **source} for entry in entries]
