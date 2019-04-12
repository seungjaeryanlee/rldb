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
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(labels, scores, color=colors)

    # Add title
    plt.title(plot_title)

    # Add score labels
    switch_label_align = False # If true, put score label outside of barplot
    for i, (bar, entry, score) in enumerate(zip(bars, sorted_entries, scores)):

        text = ax.text(
            x=bar.get_x() + bar.get_width() - 50,
            y=bar.get_y() + bar.get_height() / 2,
            s=str(score),
            color='white',
            fontweight='bold',
            ha='right',
            va='center',
        )

        # Check if putting score label outside of barplot would make it too long
        bar_x1 = bar.get_window_extent(renderer=fig.canvas.get_renderer()).x1
        ax_x1 = ax.get_window_extent(renderer=fig.canvas.get_renderer()).x1
        text_width = text.get_window_extent(renderer=fig.canvas.get_renderer()).width
        if switch_label_align or bar_x1 + text_width < ax_x1:
            switch_label_align = True
            text.set_x(bar.get_x() + bar.get_width() + 50)
            text.set_ha('left')

            if entry['algo-title'] == 'Human':
                color = 'red'
            elif entry['algo-title'] == 'Random':
                color = 'black'
            else:
                color = 'darkblue'
            text.set_color(color)

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
