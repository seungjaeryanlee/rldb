from .algo__ape_x_dqn import entries as ape_x_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Distributed Prioritized Experience Replay",
    "source-nickname": "Ape-X DQN",
    "source-authors": [
        "Dan Horgan",
        "John Quan",
        "David Budden",
        "Gabriel Barth-Maron",
        "Matteo Hessel",
        "Hado van Hasselt",
        "David Silver",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1803.00933",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1803.00933.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1708.05144",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1803-00933,
  author    = {Dan Horgan and
               John Quan and
               David Budden and
               Gabriel Barth{-}Maron and
               Matteo Hessel and
               Hado van Hasselt and
               David Silver},
  title     = {Distributed Prioritized Experience Replay},
  journal   = {CoRR},
  volume    = {abs/1803.00933},
  year      = {2018},
  url       = {http://arxiv.org/abs/1803.00933},
  archivePrefix = {arXiv},
  eprint    = {1803.00933},
  timestamp = {Mon, 13 Aug 2018 16:46:02 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1803-00933},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + ape_x_entries
)
entries = [{**entry, **source} for entry in entries]
