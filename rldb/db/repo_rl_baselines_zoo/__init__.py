from .algo__a2c import entries as a2c_entries
from .algo__acer import entries as acer_entries
from .algo__acktr import entries as acktr_entries
from .algo__ddpg import entries as ddpg_entries
from .algo__dqn import entries as dqb_entries
from .algo__ppo2 import entries as ppo2_entries
from .algo__sac import entries as sac_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "RL Baselines Zoo b76641e",
    "source-nickname": "RL Baselines Zoo b76641e",
    "source-authors": [
        "Antonin Raffin",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "GitHub",
            "url": "https://github.com/araffin/rl-baselines-zoo",
        },
    ],

    #  MISC.
    "source-bibtex": """\
@misc{rlbaselines,
  author = {Raffin, Antonin},
  title = {RL Baselines Zoo},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\\url{https://github.com/araffin/rl-baselines-zoo}},
}""",
}

# Populate entries
entries = (
    []
    + a2c_entries
    + acer_entries
    + acktr_entries
    + ddpg_entries
    + dqb_entries
    + ppo2_entries
    + sac_entries
)
entries = [{**entry, **source} for entry in entries]
