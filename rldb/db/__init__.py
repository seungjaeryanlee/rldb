from .paper__drqn import entries as drqn_entries
from .paper__ddqn import entries as ddqn_entries
from .paper__dueling_dqn import entries as dueling_entries
from .paper__rnd import entries as rnd_entries
from .paper__dqn2013 import entries as dqn2013_entries
from .paper__prioritized_dqn import entries as per_entries
from .paper__ppo import entries as ppo_entries
from .paper__trpo import entries as trpo_entries

entries = (
    []
    + drqn_entries
    + ddqn_entries
    + dueling_entries
    + rnd_entries
    + dqn2013_entries
    + per_entries
    + ppo_entries
    + trpo_entries
)

assert len(entries) == (
    0
    + 18   # DRQN
    + 375  # DDQN
    + 456  # Dueling DQN
    + 18   # RND
    + 56   # DQN2013
    + 334  # PER
    + 147  # PPO
    + 35   # TRPO
)
