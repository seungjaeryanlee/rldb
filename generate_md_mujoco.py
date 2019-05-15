#!/usr/bin/env python3
"""
Generate Atari environment Markdown files for endtoend.ai.
"""
import rldb
from generate_md_helper import get_template, populate_template, save_file, get_best_source_link, entries_to_table


def _generate_md_mujoco_main(filepath, mujoco_envs):
    # Get template
    template = get_template('markdown/source/{}'.format(filepath))

    table = ''
    table += '| Environment | Result | Algorithm | Source |\n'
    table += '|-------------|--------|-----------|--------|\n'

    for env_title in mujoco_envs:
        entries = rldb.find_all({
            'env-title': env_title,
        })
        entries.sort(key=lambda entry: entry['score'], reverse=True)
        entry = entries[0] # Best Performing algorithm
        source_link = get_best_source_link(entry) # Choose best link
        table += '| [{}](/envs/gym/mujoco/{}) | {} | {} | [{}]({}) |\n'.format(
            entry['env-title'][7:],
            entry['env-title'][7:],
            entry['score'],
            entry['algo-nickname'],
            entry['source-title'],
            source_link['url'],
        )

    result = populate_template(template, { "table": table })
    save_file('markdown/docs/{}'.format(filepath), result)

def _generate_md_mujoco_single_env(filepath, env_title):
    """Generate a Markdown file for a single MuJoCo environment."""
    # Get template
    template = get_template('markdown/source/{}'.format(filepath))

    # Parse rldb
    entries = rldb.find_all({
        'env-title': env_title,
    })
    entries.sort(key=lambda entry: entry['score'], reverse=True)
    feed_dict = {
        'table': entries_to_table(entries),
    }

    result = populate_template(template, feed_dict)
    save_file('markdown/docs/{}'.format(filepath), result)

def _generate_md_mujoco_all_env(mujoco_envs):
    """Generate all markdown files for MuJoCo environments."""
    for name in mujoco_envs:
        subname = name[7:] # "mujoco-walker2d" -> "walker2d"
        _generate_md_mujoco_single_env(
            filepath='envs/gym/mujoco/{}.md'.format(subname),
            env_title='mujoco-{}'.format(subname)
        )

def generate_md_mujoco():
    entries = rldb.find_all({})
    envs = set([entry['env-title'] for entry in entries])
    mujoco_envs = [env for env in envs if 'mujoco-' in env]

    _generate_md_mujoco_main('envs/gym/mujoco/mujoco.md', mujoco_envs)
    _generate_md_mujoco_all_env(mujoco_envs)


if __name__ == "__main__":
    generate_md_mujoco()
