import re

import rldb


def test_readme_env_count():
    """
    Test if environment count in README is correct.
    """
    all_entries = rldb.find_all({})
    all_envs = set([e['env-title'] for e in all_entries])

    with open('README.md', 'r') as f:
        lines = f.readlines()
        text = '\n'.join(lines)
        nb_envs = re.search('environments-(.*)-blue.svg', text).group(1)

    assert int(nb_envs) == len(all_envs)


def test_readme_source_count():
    """
    Test if source count in README is correct.
    """
    all_entries = rldb.find_all({})
    all_sources = set([e['source-title'] for e in all_entries])

    with open('README.md', 'r') as f:
        lines = f.readlines()
        text = '\n'.join(lines)
        nb_sources = re.search('papers-(.*)-blue.svg', text).group(1)

    assert int(nb_sources) == len(all_sources)


def test_readme_algo_count():
    """
    Test if algorithm count in README is correct.
    """
    all_entries = rldb.find_all({})
    all_algos = set([e['algo-title'] for e in all_entries])

    with open('README.md', 'r') as f:
        lines = f.readlines()
        text = '\n'.join(lines)
        nb_algos = re.search('algorithms-(.*)-blue.svg', text).group(1)

    assert int(nb_algos) == len(all_algos)


def test_readme_entry_count():
    """
    Test if entry count in README is correct.
    """
    all_entries = rldb.find_all({})

    with open('README.md', 'r') as f:
        lines = f.readlines()
        text = '\n'.join(lines)
        nb_entries = re.search('entries-(.*)-blue.svg', text).group(1)

    assert int(nb_entries) == len(all_entries)
