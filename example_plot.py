import matplotlib.pyplot as plt

import rldb


ENV_TITLE = 'atari-montezuma-revenge'

# Get relevant entries
entries = rldb.get_all_entries()
breakout_entries = [e for e in entries if e['env-title'] == ENV_TITLE]

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
plt.title('Atari Montezuma\'s Revenge Scores')
plt.tight_layout()
plt.savefig('atari-montezuma-revenge.png')
plt.show()