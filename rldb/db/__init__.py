from .paper__drqn import entries as drqn_entries
from .paper__ddqn import entries as ddqn_entries
from .paper__dueling_dqn import entries as dueling_entries
from .paper__rnd import entries as rnd_entries
from .paper__dqn2013 import entries as dqn2013_entries
from .paper__dqn2015 import entries as dqn2015_entries
from .paper__prioritized_dqn import entries as per_entries
from .paper__gorila_dqn import entries as gorila_dqn_entries
from .paper__ppo import entries as ppo_entries
from .paper__trpo import entries as trpo_entries

entries = (
    []
    + drqn_entries
    + ddqn_entries
    + dueling_entries
    + rnd_entries
    + dqn2013_entries
    + dqn2015_entries
    + per_entries
    + gorila_dqn_entries
    + ppo_entries
    + trpo_entries
)
