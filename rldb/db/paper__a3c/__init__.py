from .algo__a3c_ff_1_day import entries as a3c_ff_1_day_entries
from .algo__a3c_ff import entries as a3c_ff_entries
from .algo__a3c_lstm import entries as a3c_lstm_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Asynchronous Methods for Deep Reinforcement Learning",
    "source-nickname": "A3C",
    "source-authors": [
        "Volodymyr Mnih",
        "Adrià Puigdomènech Badia",
        "Mehdi Mirza",
        "Alex Graves",
        "Timothy P. Lillicrap",
        "Tim Harley",
        "David Silver",
        "Koray Kavukcuoglu",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1602.01783",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1602.01783.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1602.01783",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/MnihBMGLHSK16,
    author    = {Volodymyr Mnih and
                 Adri{\`{a}} Puigdom{\`{e}}nech Badia and
                 Mehdi Mirza and
                 Alex Graves and
                 Timothy P. Lillicrap and
                 Tim Harley and
                   David Silver and
                 Koray Kavukcuoglu},
    title     = {Asynchronous Methods for Deep Reinforcement Learning},
    journal   = {CoRR},
    volume    = {abs/1602.01783},
    year      = {2016},
    url       = {http://arxiv.org/abs/1602.01783},
    archivePrefix = {arXiv},
    eprint    = {1602.01783},
    timestamp = {Mon, 13 Aug 2018 16:47:40 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/MnihBMGLHSK16},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + a3c_ff_1_day_entries
    + a3c_ff_entries
    + a3c_lstm_entries
)
entries = [{**entry, **source} for entry in entries]
