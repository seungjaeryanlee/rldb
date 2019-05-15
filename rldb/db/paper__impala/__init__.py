from .algo__dmlab_30_human import entries as dmlab_30_human_entries
from .algo__dmlab_30_random import entries as dmlab_30_random_entries
from .algo__dmlab_30_experts import entries as dmlab_30_experts_entries
from .algo__dmlab_30_impala import entries as dmlab_30_impala_entries
from .algo__atari_impala_deep_multitask import entries as atari_impala_deep_multitask_entries
from .algo__atari_impala_shallow import entries as atari_impala_shallow_entries
from .algo__atari_impala_deep import entries as atari_impala_deep_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures",
    "source-nickname": "IMPALA",
    "source-authors": [
        "Lasse Espeholt",
        "Hubert Soyer",
        "Remi Munos",
        "Karen Simonyan",
        "Volodymir Mnih",
        "Tom Ward",
        "Yotam Doron",
        "Vlad Firoiu",
        "Tim Harley",
        "Iain Dunning",
        "Shane Legg",
        "Koray Kavukcuoglu",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1802.01561",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1802.01561.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1802.01561",
    "source-arxiv-version": 3,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/abs-1802-01561,
    author    = {Lasse Espeholt and
                 Hubert Soyer and
                 R{\'{e}}mi Munos and
                 Karen Simonyan and
                 Volodymyr Mnih and
                 Tom Ward and
                 Yotam Doron and
                 Vlad Firoiu and
                 Tim Harley and
                 Iain Dunning and
                 Shane Legg and
                 Koray Kavukcuoglu},
    title     = {{IMPALA:} Scalable Distributed Deep-RL with Importance Weighted Actor-Learner
                 Architectures},
    journal   = {CoRR},
    volume    = {abs/1802.01561},
    year      = {2018},
    url       = {http://arxiv.org/abs/1802.01561},
    archivePrefix = {arXiv},
    eprint    = {1802.01561},
    timestamp = {Mon, 13 Aug 2018 16:46:52 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1802-01561},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + dmlab_30_human_entries
    + dmlab_30_random_entries
    + dmlab_30_experts_entries
    + dmlab_30_impala_entries
    + atari_impala_deep_multitask_entries
    + atari_impala_shallow_entries
    + atari_impala_deep_entries
)
entries = [{**entry, **source} for entry in entries]
