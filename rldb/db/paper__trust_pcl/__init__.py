from .algo__trpo_gae import entries as trpo_gae_entries
from .algo__trpo_ours import entries as trpo_ours_entries
from .algo__trust_pcl import entries as trust_pcl_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Trust-PCL: An Off-Policy Trust Region Method for Continuous Control",
    "source-nickname": "Trust-PCL",
    "source-authors": [
        "Ofir Nachum",
        "Mohammad Norouzi",
        "Kelvin Xu",
        "Dale Schuurmans",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1707.01891",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1707.01891.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1707.01891",
    "source-arxiv-version": 3,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/NachumNXS17aa,
    author    = {Ofir Nachum and
                 Mohammad Norouzi and
                 Kelvin Xu and
                 Dale Schuurmans},
    title     = {Trust-PCL: An Off-Policy Trust Region Method for Continuous Control},
    journal   = {CoRR},
    volume    = {abs/1707.01891},
    year      = {2017},
    url       = {http://arxiv.org/abs/1707.01891},
    archivePrefix = {arXiv},
    eprint    = {1707.01891},
    timestamp = {Mon, 13 Aug 2018 16:47:10 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/NachumNXS17aa},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + trpo_gae_entries
    + trpo_ours_entries
    + trust_pcl_entries
)
entries = [{**entry, **source} for entry in entries]
