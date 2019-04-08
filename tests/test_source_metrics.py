"""Test metrics for each source."""
import rldb


def test_openai_baselines_cbd21ef_count():
    """Verify number of entries in OpenAI Baselines."""
    a3c_entries = rldb.find_all({
        'source-title': 'OpenAI Baselines cbd21ef',
    })

    assert len(a3c_entries) == (
        0
        + 7  # A2C
        + 7  # ACER
        + 7  # ACKTR
        + 7  # DQN
        + 7  # PPO2
        + 7  # PPO2 (MPI)
        + 7  # TRPO (MPI)
    )


def test_openai_baselines_ea68f3b_count():
    """Verify number of entries in OpenAI Baselines."""
    a3c_entries = rldb.find_all({
        'source-title': 'OpenAI Baselines ea68f3b',
    })

    assert len(a3c_entries) == (
        0
        + 7  # TRPO (MPI)
        + 7  # PPO2
    )


def test_rl_baselines_zoo_count():
    """Verify number of entries in RL Baselines Zoo."""
    rl_baselines_zoo_entries = rldb.find_all({
        'source-title': 'RL Baselines Zoo b76641e',
    })

    assert len(rl_baselines_zoo_entries) == (
        0
        + 12  # A2C
        + 11  # ACER
        + 12  # ACKTR
        + 3  # DDPG
        + 12  # DQN
        + 27  # PPO2
        + 12  # SAC
    )
