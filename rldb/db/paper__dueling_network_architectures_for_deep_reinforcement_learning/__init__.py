from .algo__ddqn_tuned import entries as ddqn_tuned_entries
from .algo__dqn2015 import entries as dqn2015_entries
from .algo__dueling import entries as dueling_entries
from .algo__human import entries as human_entries
from .algo__pdd import entries as pdd_entries
from .algo__prioritized_ddqn_tuned import entries as prioritized_ddqn_tuned_entries
from .algo__random import entries as random_entries



# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Dueling Network Architectures for Deep Reinforcement Learning",
    "source-nickname": "Dueling DQN",
    "source-authors": [
        "Ziyu Wang",
        "Tom Schaul",
        "Matteo Hessel",
        "Hado van Hasselt",
        "Marc Lanctot",
        "Nando de Freitas",
    ],

    #  ARXIV
    "source-arxiv-id": "1511.06581",
    "source-arxiv-version": 3,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/WangFL15,
    author    = {Ziyu Wang and
                 Nando de Freitas and
                 Marc Lanctot},
    title     = {Dueling Network Architectures for Deep Reinforcement Learning},
    journal   = {CoRR},
    volume    = {abs/1511.06581},
    year      = {2015},
    url       = {http://arxiv.org/abs/1511.06581},
    archivePrefix = {arXiv},
    eprint    = {1511.06581},
    timestamp = {Mon, 13 Aug 2018 16:48:17 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/WangFL15},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + ddqn_tuned_entries
    + dqn2015_entries
    + dueling_entries
    + human_entries
    + pdd_entries
    + prioritized_ddqn_tuned_entries
    + random_entries
)
entries = [{**entry, **source} for entry in entries]

assert len(entries) == 57 * 2 * 7  # 57 games, 2 variants, 7 algorithms

