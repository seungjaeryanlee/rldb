#!/usr/bin/env python3
"""
Generate Atari environment Markdown files for endtoend.ai.
"""
import rldb
from generate_md_helper import get_template, populate_template, save_file, get_best_source_link, entries_to_table


def _split_entries_by_variants(entries):
    """Split entries by their variants."""
    human_entries = []
    noop_entries = []
    unspecified_entries = []
    for entry in entries:
        if 'env-variant' not in entry:
            unspecified_entries.append(entry)
        elif entry['env-variant'] == 'Human start':
            human_entries.append(entry)
        elif entry['env-variant'] == 'No-op start':
            noop_entries.append(entry)
        else:
            unspecified_entries.append(entry)

    return human_entries, noop_entries, unspecified_entries

def _generate_md_atari_single_env(filepath, env_title):
    """Generate a Markdown file for a single Atari environment."""
    # Get template
    template = get_template('markdown/source/{}'.format(filepath))

    # Parse rldb
    entries = rldb.find_all({
        'env-title': env_title,
    })
    entries.sort(key=lambda entry: entry['score'], reverse=True)
    human_entries, noop_entries, unspecified_entries = _split_entries_by_variants(entries)
    feed_dict = {
        'human_table': entries_to_table(human_entries),
        'noop_table': entries_to_table(noop_entries),
        'unspecified_table': entries_to_table(unspecified_entries),
    }

    result = populate_template(template, feed_dict)
    save_file('markdown/docs/{}'.format(filepath), result)

def _generate_md_atari_main(atari_envs):
    """Generate a markdown file summarizing Atari environments."""
    # TODO Implement Human normalized score in rldb
    pass

def _generate_md_atari_batch(atari_envs):
    """Generate all markdown files for Atari environments."""
    for name in atari_envs:
        subname = name[6:] # "atari-alien" -> "alien"
        _generate_md_atari_single_env(
            filepath='envs/gym/atari/{}.md'.format(subname),
            env_title='atari-{}'.format(subname)
        )

def generate_md_atari():
    entries = rldb.find_all({})
    envs = set([entry['env-title'] for entry in entries])
    atari_envs = [env for env in envs if 'atari-' in env]
    _generate_md_atari_main(atari_envs)
    _generate_md_atari_batch(atari_envs)

if __name__ == "__main__":
    generate_md_atari()
