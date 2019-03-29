"""Test metrics written in rldb README."""
import rldb


def test_envs_count():
    """Verify number of environments in rldb. This number should match README."""
    all_entries = rldb.find_all({})
    all_envs = set([e['env-title'] for e in all_entries])

    assert len(all_envs) == 57


def test_paper_count():
    """Verify number of papers in rldb. This number should match README."""
    all_entries = rldb.find_all({})
    all_papers = set([e['source-title'] for e in all_entries])

    assert len(all_papers) == 10


def test_algo_count():
    """Verify number of algorithms in rldb. This number should match README."""
    all_entries = rldb.find_all({})
    all_algos = set([e['algo-title'] for e in all_entries])

    assert len(all_algos) == 33


def test_entries_count():
    """Verify number of entries in rldb. This number should match README."""
    all_entries = rldb.find_all({})

    assert len(all_entries) == 1929
