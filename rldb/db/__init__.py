from .paper__deep_recurrent_q_learning_for_partially_observable_mdps import entries as drqn_entries
from .paper__exploration_by_random_network_distillation import entries as rnd_entries
from .paper__playing_atari_with_deep_reinforcement_learning import entries as dqn2013_entries
from .paper__proximal_policy_optimization_algorithms import entries as ppo_entries
from .paper__trust_region_policy_optimization import entries as trpo_entries

entries = (
    []
    + drqn_entries
    + rnd_entries
    + dqn2013_entries
    + ppo_entries
    + trpo_entries
)

assert len(entries) == (
    0
    + 27   # DRQN
    + 18   # RND
    + 56   # DQN2013
    + 147  # PPO
    + 42   # TRPO
)
