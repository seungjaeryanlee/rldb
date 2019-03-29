"""Test metrics for each paper."""
import rldb


def test_ddqn_paper_count():
    """Verify number of entries in DDQN paper."""
    ddqn_entries = rldb.find_all({
        'source-title': 'Deep Reinforcement Learning with Double Q-learning',
    })

    assert len(ddqn_entries) == 57 * 4 + 49 * 2


def test_dqn2013_paper_count():
    """Verify number of entries in DQN2013 paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Playing Atari with Deep Reinforcement Learning',
    })

    assert len(dqn2013_entries) == 8 * 7


def test_dqn2015_paper_count():
    """Verify number of entries in DQN2015 paper."""
    dqn2015_entries = rldb.find_all({
        'source-title': 'Human-level Control through Deep Reinforcement Learning',
    })

    assert len(dqn2015_entries) == 49 * 5


def test_drqn_paper_count():
    """Verify number of entries in DRQN paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Deep Recurrent Q-Learning for Partially Observable MDPs',
    })

    assert len(dqn2013_entries) == 9 * 2


def test_dueling_dqn_paper_count():
    """Verify number of entries in Dueling DQN paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Dueling Network Architectures for Deep Reinforcement Learning',
    })

    assert len(dqn2013_entries) == 57 * 2 * 4 - 49


def test_ppo_paper_count():
    """Verify number of entries in PPO paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Proximal Policy Optimization Algorithm',
    })

    assert len(dqn2013_entries) == 49 * 3


def test_prioritized_dqn_paper_count():
    """Verify number of entries in Prioritized DQN paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Prioritized Experience Replay',
    })

    assert len(dqn2013_entries) == 57 * 5 + 49 * 1


def test_rnd_paper_count():
    """Verify number of entries in RND paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Exploration by Random Network Distillation',
    })

    assert len(dqn2013_entries) == 6 * 3


def test_trpo_paper_count():
    """Verify number of entries in TRPO paper."""
    dqn2013_entries = rldb.find_all({
        'source-title': 'Trust Region Policy Optimization',
    })

    assert len(dqn2013_entries) == 7 * 5
