"""Test filter find functions of rldb."""
import rldb


def test_find_one_rtype_dict():
    """Verify that find_one() returns an entry (dict), not a list of entries."""
    entry = rldb.find_one({})

    assert type(entry) == dict


def test_find_all_rtype_list():
    """Verify that find_one() returns an entry (dict), not a list of entries."""
    all_entries = rldb.find_all({})

    assert type(all_entries) == list


def test_find_one_return_none():
    """Verify that find_one() returns None if nothing is found."""
    entry = rldb.find_one({ 'env-title': 'There is no env with this title.' })

    assert entry is None


def test_find_all_return_empty_list():
    """Verify that find_all() returns an empty list if nothing is found."""
    all_entries = rldb.find_all({ 'env-title': 'There is no env with this title.' })

    assert all_entries == []


def test_find_one_return_match_all_filter():
    """Make sure that entry returned by find_one() matches all filters."""
    entry = rldb.find_one({
        'algo-nickname': 'DQN',
        'env-title': 'atari-pong',
    })

    assert entry['algo-nickname'] == 'DQN'
    assert entry['env-title'] == 'atari-pong'


def test_find_all_return_match_all_filter():
    """Make sure that all entries returned by find_all() matches all filters."""
    all_entries = rldb.find_all({
        'algo-nickname': 'DQN',
        'env-title': 'atari-pong',
    })

    for entry in all_entries:
        assert entry['algo-nickname'] == 'DQN'
        assert entry['env-title'] == 'atari-pong'
