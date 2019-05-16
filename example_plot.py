from decimal import Decimal

import matplotlib.pyplot as plt

import rldb


def set_label(fig, ax, bar, entry, BBOX_TO_BAR_UNIT):
    algo_text = ax.text(
        x=bar.get_x()-100,
        y=bar.get_y()+0.4,
        s=str(entry['algo-nickname']),
        color='black',
        fontweight='bold',
        ha='right',
        va='bottom'
    )
    source_text = ax.text(
        x=bar.get_x()-100,
        y=bar.get_y()+bar.get_height()-0.4,
        s=str(entry['source-nickname']),
        color='red',
        ha='right',
        va='top'
    )
    source_text_x = source_text.get_position()[0]
    source_text_width = source_text.get_window_extent(renderer=fig.canvas.get_renderer()).width

    if 'algo-frames' in entry:
        # TODO This is currently stub
        frames_text = ax.text(
            x=source_text_x - source_text_width * BBOX_TO_BAR_UNIT - 50,
            y=bar.get_y()+bar.get_height()-0.4,
            s='{:.2E}'.format(Decimal(entry['algo-frames'])),
            color='green',
            ha='right',
            va='top'
        )


def set_score_text(fig, ax, bar, entry):
    score_text = ax.text(
        x=bar.get_x() + bar.get_width() - 30,
        y=bar.get_y() + bar.get_height() / 2,
        s=str(entry['score']),
        color='white',
        fontweight='bold',
        ha='right',
        va='center',
    )

    # Check if putting score label outside of barplot would make it too long
    bar_x1 = bar.get_window_extent(renderer=fig.canvas.get_renderer()).x1
    ax_x1 = ax.get_window_extent(renderer=fig.canvas.get_renderer()).x1
    score_text_width = score_text.get_window_extent(renderer=fig.canvas.get_renderer()).width

    if bar_x1 + score_text_width < ax_x1:
        score_text.set_x(bar.get_x() + bar.get_width() + 50)
        score_text.set_ha('left')

        if entry['algo-title'] == 'Human':
            color = 'red'
        elif entry['algo-title'] == 'Random':
            color = 'black'
        else:
            color = 'darkblue'
        score_text.set_color(color)


def set_label_legends(fig, ax, bars, BBOX_TO_BAR_UNIT):
    origin_x = bars[-1].get_x()
    origin_y = bars[-1].get_y() + bars[-1].get_height()

    algo_text = ax.text(
        x=origin_x - 100,
        y=origin_y + 0.4,
        s='Algorithm',
        color='black',
        fontweight='bold',
        ha='right',
        va='bottom'
    )
    source_text = ax.text(
        x=origin_x - 100,
        y=origin_y + bars[-1].get_height() - 0.4,
        s='Source',
        color='red',
        ha='right',
        va='top'
    )
    source_text_x = source_text.get_position()[0]
    source_text_width = source_text.get_window_extent(renderer=fig.canvas.get_renderer()).width

    frames_text = ax.text(
        x=source_text_x - source_text_width * BBOX_TO_BAR_UNIT - 50,
        y=origin_y + bars[-1].get_height() - 0.4,
        s='Frames',
        color='green',
        ha='right',
        va='top'
    )


def env_barplot(filter, plot_title, filepath):
    entries = rldb.find_all(filter)

    # Dedupe and sort entries by score, increasing
    sorted_entries = sorted(
        entries,
        key=lambda entry: entry['score'],
        reverse=True,
    )
    labels, scores, colors = entries_to_labels_scores(sorted_entries)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, int(len(sorted_entries)/2)))
    bars = ax.barh(labels, scores, color=colors)
    plt.yticks(range(len(scores)), [''] * len(scores))

    # Add title
    plt.title(plot_title)

    # Add score labels
    bar_x0 = bars[0].get_window_extent(renderer=fig.canvas.get_renderer()).x0
    bar_x1 = bars[0].get_window_extent(renderer=fig.canvas.get_renderer()).x1
    BBOX_TO_BAR_UNIT = bars[0].get_width() / (bar_x1 - bar_x0)
    switch_label_align = False # If true, put score label outside of barplot
    for i, (bar, entry) in enumerate(zip(bars, sorted_entries)):
        set_label(fig, ax, bar, entry, BBOX_TO_BAR_UNIT)
        set_score_text(fig, ax, bar, entry)

    # Add label legends
    set_label_legends(fig, ax, bars, BBOX_TO_BAR_UNIT)


    plt.tight_layout()
    plt.savefig(filepath)
    # plt.show()
    plt.clf()


def entries_to_labels_scores(entries):
    """
    Convert entries to labels and scores for barplot.

    NOTE The labels only exist to discern entries: the actual labels are
    set in set_label_legends.
    """
    nicknames = [entry['algo-nickname'] for entry in entries]

    scores = []
    colors = []
    for entry in entries:
        # Special color for 'Human' and 'Random'
        if entry['algo-title'] == 'Human':
            color = 'red'
        elif entry['algo-title'] == 'Random':
            color = 'black'
        else:
            color = 'darkblue'
        scores.append(entry['score'])

        colors.append(color)

    return list(range(len(scores))), scores, colors


def main():
    env_barplot(
        filter={
            'env-title': 'atari-space-invaders',
            'env-variant': 'No-op start',
        },
        plot_title='Atari Space Invaders Scores (No-op start)',
        filepath='docs/atari-space-invaders.png',
    )
    env_barplot(
        filter={'env-title': 'mujoco-walker2d'},
        plot_title='MuJoCo Walker2D Scores',
        filepath='docs/mujoco-walker2d.png',
    )


if __name__ == '__main__':
    main()
