from .paper__a3c import entries as a3c_entries
from .paper__acktr import entries as acktr_entries
from .paper__c51 import entries as c51_entries
from .paper__drqn import entries as drqn_entries
from .paper__ddqn import entries as ddqn_entries
from .paper__dudqn import entries as dudqn_entries
from .paper__rnd import entries as rnd_entries
from .paper__dqn2013 import entries as dqn2013_entries
from .paper__dqn import entries as dqn_entries
from .paper__noisynet import entries as noisynet_entries
from .paper__prioritized_dqn import entries as per_entries
from .paper__qr_dqn import entries as qr_dqn_entries
from .paper__rainbow import entries as rainbow_entries
from .paper__reactor import entries as reactor_entries
from .paper__gorila_dqn import entries as gorila_dqn_entries
from .paper__impala import entries as impala_entries
from .paper__iqn import entries as iqn_entries
from .paper__ppo import entries as ppo_entries
from .paper__td3 import entries as td3_entries
from .paper__trpo import entries as trpo_entries
from .paper__trust_pcl import entries as trust_pcl_entries
from .repo__openai_baselines_cbd21ef import entries as openai_baselines_cbd21ef_entries
from .repo__openai_baselines_ea68f3b import entries as openai_baselines_ea68f3b_entries
from .repo_rl_baselines_zoo import entries as rl_baselines_zoo_entries

entries = (
    []
    + a3c_entries
    + acktr_entries
    + c51_entries
    + drqn_entries
    + ddqn_entries
    + dudqn_entries
    + rnd_entries
    + dqn2013_entries
    + dqn_entries
    + noisynet_entries
    + per_entries
    + qr_dqn_entries
    + rainbow_entries
    + reactor_entries
    + gorila_dqn_entries
    + impala_entries
    + iqn_entries
    + ppo_entries
    + td3_entries
    + trpo_entries
    + trust_pcl_entries

    + openai_baselines_cbd21ef_entries
    + openai_baselines_ea68f3b_entries
    + rl_baselines_zoo_entries
)
