from .algo__dynamics import entries as dynamics_entries
from .algo__ppo import entries as ppo_entries
from .algo__rnd import entries as rnd_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Exploration by Random Network Distillation",
    "source-nickname": "RND",
    "source-authors": [
        "Yuri Burda",
        "Harrison Edwards",
        "Amos Storkey",
        "Oleg Klimov",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1810.12894",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1810.12894.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1810.12894",
    "source-arxiv-version": 1,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1810-12894,
    author    = {Yuri Burda and
                 Harrison Edwards and
                 Amos J. Storkey and
                 Oleg Klimov},
    title     = {Exploration by Random Network Distillation},
    journal   = {CoRR},
    volume    = {abs/1810.12894},
    year      = {2018},
    url       = {http://arxiv.org/abs/1810.12894},
    archivePrefix = {arXiv},
    eprint    = {1810.12894},
    timestamp = {Thu, 08 Nov 2018 10:57:46 +0100},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1810-12894},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + dynamics_entries
    + ppo_entries
    + rnd_entries
)

entries = [{**entry, **source} for entry in entries]
