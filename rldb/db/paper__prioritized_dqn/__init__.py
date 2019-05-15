from .algo__prop_prioritized_ddqn_tuned import entries as prop_pddqn_tuned_entries
from .algo__rank_prioritized import entries as rank_prioritized_entries
from .algo__rank_prioritized_ddqn_tuned import entries as rank_pddqn_tuned_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Prioritized Experience Replay",
    "source-nickname": "Prioritized DQN",
    "source-authors": [
        "Tom Schaul",
        "John Quan",
        "Ioannis Antonoglou",
        "David Silver",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "ArXiv",
            "url": "https://arxiv.org/abs/1511.05952",
        },
        {
            "type": "PDF",
            "url": "https://arxiv.org/pdf/1511.05952.pdf",
        },
    ],

    #  ARXIV
    "source-arxiv-id": "1511.05952",
    "source-arxiv-version": 4,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/SchaulQAS15,
  author    = {Tom Schaul and
               John Quan and
               Ioannis Antonoglou and
               David Silver},
  title     = {Prioritized Experience Replay},
  journal   = {CoRR},
  volume    = {abs/1511.05952},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.05952},
  archivePrefix = {arXiv},
  eprint    = {1511.05952},
  timestamp = {Mon, 13 Aug 2018 16:46:28 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SchaulQAS15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + prop_pddqn_tuned_entries
    + rank_prioritized_entries
    + rank_pddqn_tuned_entries
)
entries = [{**entry, **source} for entry in entries]
