"""Test metrics written in rldb README."""
import rldb


def test_envs_count():
    """Verify number of environments in rldb. This number should match README."""
    all_entries = rldb.find_all({})
    all_envs = set([e['env-title'] for e in all_entries])

    assert len(all_envs) == 84


def test_source_count():
    """Verify number of sources in rldb. This number should match README."""
    all_entries = rldb.find_all({})
    all_sources = set([e['source-title'] for e in all_entries])

    assert len(all_sources) == 22


def test_algo_count():
    """Verify number of algorithms in rldb. This number should match README."""
    all_entries = rldb.find_all({})
    all_algos = set([e['algo-title'] for e in all_entries])

    assert len(all_algos) == 77


def test_entries_count():
    """Verify number of entries in rldb. This number should match README."""
    all_entries = rldb.find_all({})

    assert len(all_entries) == 2918
    assert len(all_entries) == (
        0
        + 171  # A3C
        + 80   # ACKTR
        + 171  # C51
        + 179  # DDQN
        + 245  # DQN
        + 56   # DQN2013
        + 38   # DRQN
        + 301  # DuDQN
        + 245  # Gorila DQN
        + 57   # IQN
        + 456  # NoisyNet
        + 147  # PPO
        + 171  # Prioritized DQN
        + 114  # QR-DQN
        + 232  # Rainbow
        + 18   # RND
        + 49   # TD3
        + 21   # TRPO
        + 15   # Trust-PCL

        + 49   # OpenAI Baselines cbd21ef
        + 14   # OpenAI Baselines ea68f3b
        + 89   # RL Baselines Zoo b76641e
    )
