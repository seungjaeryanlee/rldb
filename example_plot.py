import matplotlib.pyplot as plt

import rldb


def env_barplot(env_title, plot_title):
    # Get relevant entries
    entries = rldb.get_all_entries()
    breakout_entries = [e for e in entries if e['env-title'] == env_title]

    # Sort entries by score, increasing
    breakout_entries = sorted(
        breakout_entries,
        key=lambda entry: entry['score'],
        reverse=True
    )

    # Draw bar plot
    labels = [entry['algo-nickname'] for entry in breakout_entries]
    scores = [entry['score'] for entry in breakout_entries]
    plt.barh(labels, scores)
    plt.title(plot_title)
    plt.tight_layout()
    plt.savefig('docs/{}.png'.format(env_title))
    plt.show()


def main():
    env_barplot('atari-breakout', 'Atari Breakout Scores')
    env_barplot('atari-montezuma-revenge', 'Atari Montezuma\'s Revenge Scores')


if __name__ == '__main__':
    main()
