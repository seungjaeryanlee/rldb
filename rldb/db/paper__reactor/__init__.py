from .algo__reactor_nd import entries as reactor_nd_entries
from .algo__reactor import entries as reactor_entries
from .algo__reactor_500m import entries as reactor_500m_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "The Reactor: A fast and sample-efficient Actor-Critic agent for Reinforcement Learning",
    "source-nickname": "Reactor",
    "source-authors": [
        "Audrunas Gruslys",
        "Will Dabney",
        "Mohammad Gheshlaghi Azar",
        "Bilal Piot",
        "Marc Bellemare",
        "Remi Munos",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1704.04651",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1704.04651.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1704.04651",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/GruslysABM17,
  author    = {Audrunas Gruslys and
               Mohammad Gheshlaghi Azar and
               Marc G. Bellemare and
               R{\'{e}}mi Munos},
  title     = {The Reactor: {A} Sample-Efficient Actor-Critic Architecture},
  journal   = {CoRR},
  volume    = {abs/1704.04651},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.04651},
  archivePrefix = {arXiv},
  eprint    = {1704.04651},
  timestamp = {Mon, 13 Aug 2018 16:47:55 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/GruslysABM17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + reactor_nd_entries
    + reactor_entries
    + reactor_500m_entries
)

entries = [{**entry, **source} for entry in entries]
