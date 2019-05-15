

from .algo__random import entries as random_entries
from .algo__bll import entries as bll_entries
from .algo__contingency import entries as contingency_entries
from .algo__human import entries as human_entries
from .algo__dqn import entries as dqn_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Human-level control through deep reinforcement learning",
    "source-nickname": "DQN",
    "source-authors": [
        "Volodymyr Mnih",
        "Koray Kavukcuoglu",
        "David Silver",
        "Andrei A. Rusu",
        "Joel Veness",
        "Marc G. Bellemare",
        "Alex Graves",
        "Martin Riedmiller",
        "Andreas K. Fidjeland",
        "Georg Ostrovski",
        "Stig Petersen",
        "Charles Beattie",
        "Amir Sadik",
        "Ioannis Antonoglou"
        "Helen King",
        "Dharshan Kumaran",
        "Daan Wierstra",
        "Shane Legg",
        "Demis Hassabis",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "PDF",
            "url": "https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf",
        },
    ],
}

# Populate entries
entries = (
    []
    + random_entries
    + bll_entries
    + contingency_entries
    + human_entries
    + dqn_entries
)
entries = [{**entry, **source} for entry in entries]
