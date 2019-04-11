import matplotlib.pyplot as plt

import rldb


def env_barplot(filter, plot_title, plot_name):
    entries = rldb.find_all(filter)

    # Dedupe and sort entries by score, increasing
    sorted_entries = sorted(
        entries,
        key=lambda entry: entry['score'],
        reverse=True,
    )
    labels, scores, colors = entries_to_labels_scores(sorted_entries)

    # Draw bar plot
    plt.figure(figsize=(12, 8))
    bars = plt.barh(labels, scores, color=colors)
    # Color 'Human' and 'Random' entries

    # Add text
    plt.title(plot_title)
    plt.tight_layout()
    plt.savefig('docs/{}.png'.format(plot_name))
    # plt.show()
    plt.clf()


def entries_to_labels_scores(entries):
    """
    Convert entries to labels and scores for barplot.
    """
    nicknames = [entry['algo-nickname'] for entry in entries]

    labels = []
    scores = []
    colors = []
    for entry in entries:
        label = entry['algo-nickname']

        # Add source info if needed
        if nicknames.count(entry['algo-nickname']) > 1:
            label += ' (From {})'.format(entry['source-nickname'])

        # Special color for 'Human' and 'Random'
        
        if entry['algo-title'] == 'Human':
            color = 'red'
        elif entry['algo-title'] == 'Random':
            color = 'black'
        else:
            color = 'darkblue'

        labels.append(label)
        scores.append(entry['score'])

        colors.append(color)

    return labels, scores, colors


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
