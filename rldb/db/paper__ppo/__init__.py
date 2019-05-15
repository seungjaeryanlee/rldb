from .algo__a2c import entries as a2c_entries
from .algo__acer import entries as acer_entries
from .algo__ppo import entries as ppo_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Proximal Policy Optimization Algorithm",
    "source-nickname": "PPO",
    "source-authors": [
        "John Schulman",
        "Filip Wolski",
        "Prafulla Dhariwal",
        "Alec Radford",
        "Oleg Klimov",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1707.06347",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1707.06347.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1707.06347",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/SchulmanWDRK17,
    author    = {John Schulman and
                Filip Wolski and
                Prafulla Dhariwal and
                Alec Radford and
                Oleg Klimov},
    title     = {Proximal Policy Optimization Algorithms},
    journal   = {CoRR},
    volume    = {abs/1707.06347},
    year      = {2017},
    url       = {http://arxiv.org/abs/1707.06347},
    archivePrefix = {arXiv},
    eprint    = {1707.06347},
    timestamp = {Mon, 13 Aug 2018 16:47:34 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/SchulmanWDRK17},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = a2c_entries + acer_entries + ppo_entries
entries = [{**entry, **source} for entry in entries]
