from statistics import median

from .find import find_all
from .db import entries


def get_human_normalized_score(entry):
    """
    Return human-normalized score of the entry.

    This normalization is well documented in the Rainbow paper.
    https://arxiv.org/abs/1710.02298
    """
    human_entries = find_all({
        'env-title': entry['env-title'],
        'algo-title': 'Human',
        'env-variant': entry['env-variant'],
    })
    random_entries = find_all({
        'env-title': entry['env-title'],
        'algo-title': 'Random',
        'env-variant': entry['env-variant'],
    })

    # Use the higher scores if multiple scores exist
    if len(human_entries) > 1:
        print("[WARNING] More than one human entries were found for environment '{}'.".format(entry['env-title']))
        human_entries.sort(key=lambda entry: entry['score'], reverse=True)
    if len(random_entries) > 1:
        print("[WARNING] More than one random entries were found for environment '{}'.".format(entry['env-title']))
        random_entries.sort(key=lambda entry: entry['score'], reverse=True)

    return (entry['score'] - random_entries[0]['score']) / (human_entries[0]['score'] - random_entries[0]['score'])


def get_atari_median_human_normalized_score(algo_title, env_variant):
    """
    Return median of human-normalized score of the algorithm for atari environments.

    This normalization is well documented in the Rainbow paper.
    https://arxiv.org/abs/1710.02298
    """
    normalized_scores = []
    algo_entries = find_all({ 'algo-title': algo_title, 'env-variant': env_variant })
    for algo_entry in algo_entries:
        if algo_entry['env-title'][:5] == 'atari':
            score = get_human_normalized_score(algo_entry)
            normalized_scores.append(score)
    
    return median(normalized_scores)
