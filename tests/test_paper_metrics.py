"""Test metrics for each paper."""
import rldb


def test_a3c_paper_count():
    """Verify number of entries in A3C paper."""
    a3c_entries = rldb.find_all({
        'source-title': 'Asynchronous Methods for Deep Reinforcement Learning',
    })

    assert len(a3c_entries) == (
        0
        + 57  # A3C FF 1 day
        + 57  # A3C FF
        + 57  # A3C LSTM
    )


def test_a3c_paper_count():
    """Verify number of entries in Ape-X DQN paper."""
    ape_x_dqn_entries = rldb.find_all({
        'source-title': 'Distributed Prioritized Experience Replay',
    })

    assert len(ape_x_dqn_entries) == (
        0
        + 114
    )


def test_c51_paper_count():
    """Verify number of entries in C51 paper."""
    c51_entries = rldb.find_all({
        'source-title': 'A Distributional Perspective on Reinforcement Learning',
    })

    assert len(c51_entries) == (
        0
        + 57  # DQN
        + 57  # DDQN
        + 57  # C51
    )


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
        'source-title': 'Human-level control through deep reinforcement learning',
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
    dudqn_entries = rldb.find_all({
        'source-title': 'Dueling Network Architectures for Deep Reinforcement Learning',
    })

    assert len(dudqn_entries) == (
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


def test_impala_paper_count():
    """Verify number of entries in IMPALA paper."""
    impala_entries = rldb.find_all({
        'source-title': 'IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures',
    })

    assert len(impala_entries) == (
        0
        + 57  # Atari-57 IMPALA (deep)
        + 57  # Atari-57 IMPALA (deep, multitask)
        + 57  # Atari-57 IMPALA (shallow)
        + 30  # DMLab-30 Experts
        + 30  # DMLab-30 Human
        + 30  # DMLab-30 IMPALA
        + 30  # DMLab-30 Random
    )


def test_noisynet_paper_count():
    """Verify number of entries in NoisyNet paper."""
    noisynet_entries = rldb.find_all({
        'source-title': 'Noisy Networks for Exploration',
    })

    assert len(noisynet_entries) == (
        0
        + 57  # A3C
        + 57  # DQN
        + 57  # DuDQN
        + 57  # NoisyNet A3C
        + 57  # NoisyNet DQN
        + 57  # NoisyNet DuDQN
    )


def test_ppo_paper_count():
    """Verify number of entries in PPO paper."""
    ppo_entries = rldb.find_all({
        'source-title': 'Proximal Policy Optimization Algorithm',
    })

    assert len(ppo_entries) == (
        0
        + 49  # A2C
        + 49  # ACER
        + 49  # PPO
    )


def test_prioritized_dqn_paper_count():
    """Verify number of entries in Prioritized DQN paper."""
    prioritized_dqn_entries = rldb.find_all({
        'source-title': 'Prioritized Experience Replay',
    })

    assert len(prioritized_dqn_entries) == (
        0
        + 57  # Proportional Prioritized DDQN
        + 57  # Rank Prioritized DQN
        + 57  # Rank Prioritized DDQN
    )


def test_rainbow_paper_count():
    """Verify number of entries in Rainbow paper."""
    rainbow_entries = rldb.find_all({
        'source-title': 'Rainbow: Combining Improvements in Deep Reinforcement Learning',
    })

    assert len(rainbow_entries) == (
        0
        + 16   # DQN
        + 108  # Distributional DQN
        + 108  # Rainbow
    )


def test_rnd_paper_count():
    """Verify number of entries in RND paper."""
    rnd_entries = rldb.find_all({
        'source-title': 'Exploration by Random Network Distillation',
    })

    assert len(rnd_entries) == (
        0
        + 6  # Dynamics
        + 6  # PPO
        + 6  # RND
    )


def test_td3_paper_count():
    """Verify number of entries in TD3 paper."""
    td3_entries = rldb.find_all({
        'source-title': 'Addressing Function Approximation Error in Actor-Critic Methods',
    })

    assert len(td3_entries) == (
        0
        + 7  # ACKTR
        + 7  # DDPG
        + 7  # Our DDPG
        + 7  # PPO
        + 7  # SAC
        + 7  # TD3
        + 7  # TRPO
    )


def test_trpo_paper_count():
    """Verify number of entries in TRPO paper."""
    trpo_entries = rldb.find_all({
        'source-title': 'Trust Region Policy Optimization',
    })

    assert len(trpo_entries) == (
        0
        + 7  # TRPO (single path)
        + 7  # TRPO (vine)
        + 7  # UCC-I
    )


def test_trust_pcl_paper_count():
    """Verify number of entries in Trust-PCL paper."""
    trust_pcl_entries = rldb.find_all({
        'source-title': 'Trust-PCL: An Off-Policy Trust Region Method for Continuous Control',
    })

    assert len(trust_pcl_entries) == (
        0
        + 5  # TRPO+GAE
        + 5  # TRPO (from Trust-PCL)
        + 5  # Trust-PCL
    )
