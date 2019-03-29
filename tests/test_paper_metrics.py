"""Test metrics for each paper."""
import rldb


def test_ddqn_paper_count():
    """Verify number of entries in DDQN paper."""
    ddqn_entries = rldb.find_all({
        'source-title': 'Deep Reinforcement Learning with Double Q-learning',
    })

    assert len(ddqn_entries) == (
        0
        + 57 + 49  # DDQN 
        + 57       # DDQN (tuned)
        + 8        # Human
        + 8        # Random
    )


def test_dqn2013_paper_count():
    """Verify number of entries in DQN2013 paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Playing Atari with Deep Reinforcement Learning',
    })

    assert len(dqn2013_entries) == (
        0
        + 7  # Contingency
        + 7  # DQN2013
        + 7  # DQN2013 Best
        + 7  # HNeat Best
        + 7  # HNeat Pixel
        + 7  # Human
        + 7  # Random
        + 7  # SARSA
    )


def test_dqn_paper_count():
    """Verify number of entries in DQN paper."""
    dqn_entries = rldb.find_all({
        'source-title': 'Human-level Control through Deep Reinforcement Learning',
    })

    assert len(dqn_entries) == (
        0
        + 49  # Best Linear Learner
        + 49  # Contingency
        + 49  # DQN
        + 49  # Human
        + 49  # Random
    )


def test_drqn_paper_count():
    """Verify number of entries in DRQN paper."""
    drqn_entries = rldb.find_all({
        'source-title': 'Deep Recurrent Q-Learning for Partially Observable MDPs',
    })

    assert len(drqn_entries) == (
        0
        + 19  # DQN (Ours)
        + 19  # DRQN
    )


def test_dueling_dqn_paper_count():
    """Verify number of entries in Dueling DQN paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Dueling Network Architectures for Deep Reinforcement Learning',
    })

    assert len(dqn2013_entries) == (
        0
        + 114  # Dueling DQN
        + 65   # Human
        + 114  # PDD DQN
        + 8    # Random
    )


def test_gorila_dqn_paper_count():
    """Verify number of entries in Gorila DQN paper."""
    gorila_dqn_entries = rldb.find_all({
        'source-title': 'Massively Parallel Methods for Deep Reinforcement Learning',
    })

    assert len(gorila_dqn_entries) == (
        0
        + 49  # DQN
        + 98  # Gorila DQN
        + 49  # Human
        + 49  # Random
    )


def test_ppo_paper_count():
    """Verify number of entries in PPO paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Proximal Policy Optimization Algorithm',
    })

    assert len(dqn2013_entries) == (
        0
        + 49  # A2C
        + 49  # ACER
        + 49  # PPO
    )


def test_prioritized_dqn_paper_count():
    """Verify number of entries in Prioritized DQN paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Prioritized Experience Replay',
    })

    assert len(dqn2013_entries) == (
        0
        + 57  # Proportional Prioritized DDQN
        + 57  # Rank Prioritized DQN
        + 57  # Rank Prioritized DDQN
    )


def test_rnd_paper_count():
    """Verify number of entries in RND paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Exploration by Random Network Distillation',
    })

    assert len(dqn2013_entries) == (
        0
        + 6  # Dynamics
        + 6  # PPO
        + 6  # RND
    )


def test_trpo_paper_count():
    """Verify number of entries in TRPO paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Trust Region Policy Optimization',
    })

    assert len(dqn2013_entries) == (
        0
        + 7  # TRPO (single path)
        + 7  # TRPO (vine)
        + 7  # UCC-I
    )
