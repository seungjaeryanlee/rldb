import matplotlib.pyplot as plt

import rldb


def env_barplot(env_title, plot_title):
    # Get relevant entries
    entries = rldb.get_all_entries()
    entries = [e for e in entries if e['env-title'] == env_title]

    # Dedupe and sort entries by score, increasing
    sorted_entries = sorted(
        entries,
        key=lambda entry: entry['score'],
        reverse=True
    )
    deduped_entries = remove_duplicates(sorted_entries)

    # Draw bar plot
    labels = ['{} ({})'.format(entry['algo-nickname'], entry['env-variant']) if 'env-variant' in entry else entry['algo-nickname'] for entry in deduped_entries]
    scores = [entry['score'] for entry in deduped_entries]
    plt.barh(labels, scores)
    plt.title(plot_title)
    plt.tight_layout()
    plt.savefig('docs/{}.png'.format(env_title))
    plt.show()


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
    env_barplot('atari-breakout', 'Atari Breakout Scores')
    env_barplot('atari-montezuma-revenge', 'Atari Montezuma\'s Revenge Scores')


if __name__ == '__main__':
    main()
