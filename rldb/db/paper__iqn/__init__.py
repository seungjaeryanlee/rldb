from .algo__iqn import entries as iqn_entries

# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Implicit Quantile Networks for Distributional Reinforcement Learning",
    "source-nickname": "IQN",
    "source-authors": [
        "Will Dabney",
        "Georg Ostrovski",
        "David Silver",
        "Rémi Munos",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1806.06923",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1806.06923.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1806.06923",
    "source-arxiv-version": 1,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1806-06923,
    author    = {Will Dabney and
                 Georg Ostrovski and
                 David Silver and
                 R{\'{e}}mi Munos},
    title     = {Implicit Quantile Networks for Distributional Reinforcement Learning},
    journal   = {CoRR},
    volume    = {abs/1806.06923},
    year      = {2018},
    url       = {http://arxiv.org/abs/1806.06923},
    archivePrefix = {arXiv},
    eprint    = {1806.06923},
    timestamp = {Mon, 13 Aug 2018 16:48:24 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1806-06923},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + iqn_entries
)
entries = [{**entry, **source} for entry in entries]
