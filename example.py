"""
Example usage of sotarl package.
TODO Adjust accordingly after sotarl is implemented.
"""
import sotarl


nicknames = ['dqn2015', 'doubledqn', 'per', 'duelingdqn', 'noisydqn', 'c51', 'rainbowdqn']
papers = sotarl.get_papers_from_nicknames(nicknames)
primary_algos = sotarl.get_primary_algos_from_papers(papers)
scores = [algo['breakout']['score'] for algo in primary_algos]

for nickname, score in zip(nickname, score):
    print('{:10s} | {:5.2f}'.format(nickname, score))
