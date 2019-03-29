from .algo__human import entries as human_entries
from .algo__random import entries as random_entries
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

    #  ARXIV
    "source-arxiv-id": "1706.10295",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """""",
}

# Populate entries
entries = (
    []
    + human_entries
    + random_entries
    + dqn_entries
    + noisynet_dqn_entries
    + a3c_entries
    + noisynet_a3c_entries
    + dudqn_entries
    + noisynet_dudqn_entries
)
entries = [{**entry, **source} for entry in entries]
