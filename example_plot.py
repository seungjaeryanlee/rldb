import matplotlib.pyplot as plt

import rldb


def env_barplot(filter, plot_title, plot_name):
    entries = rldb.find_all(filter)

    # Dedupe and sort entries by score, increasing
    sorted_entries = sorted(
        entries,
        key=lambda entry: entry['score'],
        reverse=True
    )
    deduped_entries = remove_duplicates(sorted_entries)

    # Draw bar plot
    labels = ['{} ({})'.format(entry['algo-nickname'], entry['env-variant']) if 'env-variant' in entry and 'env-variant' not in filter else entry['algo-nickname'] for entry in deduped_entries]
    scores = [entry['score'] for entry in deduped_entries]
    plt.figure(figsize=(12, 8))
    plt.barh(labels, scores)
    plt.title(plot_title)
    plt.tight_layout()
    plt.savefig('docs/{}.png'.format(plot_name))
    # plt.show()
    plt.clf()


def remove_duplicates(entries):
    duplicate_indices = []
    for i, entry in enumerate(entries):
        if i == len(entries) - 1:
            break
        next_entry = entries[i + 1]

        if entry['algo-nickname'] == next_entry['algo-nickname'] and ('env-variant' in entry and 'env-variant' in next_entry and entry['env-variant'] == next_entry['env-variant']):
            if entry['score'] == next_entry['score']:
                duplicate_indices.append(i + 1)
            else:
                print('[WARN] Algorithm {} have different scores ({}, {}) from source ({}, {}) in env {}. Consider renaming them.'.format(
                    entry['algo-nickname'],
                    entry['score'], next_entry['score'],
                    entry['source-nickname'], next_entry['source-nickname'],
                    '{} ({})'.format(entry['env-title'], entry['env-variant']) if 'env-variant' in entry else entry['env-title'],
                ))

    deduped_entries = [entry for i, entry in enumerate(entries) if i not in duplicate_indices]
    return deduped_entries


def main():
    env_barplot(
        filter={
            'env-title': 'atari-space-invaders',
            'env-variant': 'No-op start',
        },
        plot_title='Atari Space Invaders Scores (No-op start)',
        plot_name='atari-space-invaders',
    )
    env_barplot(
        filter={'env-title': 'mujoco-walker2d'},
        plot_title='Atari Space Invaders Scores',
        plot_name='mujoco-walker2d',
    )


if __name__ == '__main__':
    main()
