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
    })
    random_entries = find_all({
        'env-title': entry['env-title'],
        'algo-title': 'Random',
    })

    # Use the higher scores if multiple scores exist
    if len(human_entries) > 1:
        print("[WARNING] More than one human entries were found for environment '{}'.".format(entry['env-title']))
        human_entries.sort(key=lambda entry: entry['score'], reverse=True)
    if len(random_entries) > 1:
        print("[WARNING] More than one random entries were found for environment '{}'.".format(entry['env-title']))
        random_entries.sort(key=lambda entry: entry['score'], reverse=True)

    return (entry['score'] - random_entries[0]['score']) / (human_entries[0]['score'] - random_entries[0]['score'])
