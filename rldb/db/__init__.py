from .paper__proximal_policy_optimization_algorithms import entries as ppo_entries
from .paper__trust_region_policy_optimization import entries as trpo_entries

entries = (
      ppo_entries
    + trpo_entries
)

assert len(entries) == (
      147  # PPO
    + 42   # TRPO
)
