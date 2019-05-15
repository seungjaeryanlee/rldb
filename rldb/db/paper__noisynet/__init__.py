from .algo__dqn import entries as dqn_entries
from .algo__noisynet_dqn import entries as noisynet_dqn_entries
from .algo__a3c import entries as a3c_entries
from .algo__noisynet_a3c import entries as noisynet_a3c_entries
from .algo__dudqn import entries as dudqn_entries
from .algo__noisynet_dudqn import entries as noisynet_dudqn_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Noisy Networks for Exploration",
    "source-nickname": "NoisyNet",
    "source-authors": [
        "Meire Fortunato",
        "Mohammad Gheshlaghi Azar",
        "Bilal Piot",
        "Jacob Menick",
        "Ian Osband",
        "Alex Graves",
        "Vlad Mnih",
        "Remi Munos",
        "Demis Hassabis",
        "Olivier Pietquin",
        "Charles Blundell",
        "Shane Legg",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1706.10295",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1706.10295.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1706.10295",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """
@article{DBLP:journals/corr/FortunatoAPMOGM17,
    author    = {Meire Fortunato and
                 Mohammad Gheshlaghi Azar and
                 Bilal Piot and
                 Jacob Menick and
                 Ian Osband and
                 Alex Graves and
                 Vlad Mnih and
                 R{\'{e}}mi Munos and
                 Demis Hassabis and
                 Olivier Pietquin and
                 Charles Blundell and
                 Shane Legg},
    title     = {Noisy Networks for Exploration},
    journal   = {CoRR},
    volume    = {abs/1706.10295},
    year      = {2017},
    url       = {http://arxiv.org/abs/1706.10295},
    archivePrefix = {arXiv},
    eprint    = {1706.10295},
    timestamp = {Mon, 13 Aug 2018 16:46:11 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/FortunatoAPMOGM17},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + dqn_entries
    + noisynet_dqn_entries
    + a3c_entries
    + noisynet_a3c_entries
    + dudqn_entries
    + noisynet_dudqn_entries
)
entries = [{**entry, **source} for entry in entries]
