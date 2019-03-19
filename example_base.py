"""
Example usage of rldb package.
TODO Adjust accordingly after rldb is implemented.
"""
import rldb


nicknames = ['dqn2015', 'doubledqn', 'per', 'duelingdqn', 'noisydqn', 'c51', 'rainbowdqn']
papers = rldb.get_papers_from_nicknames(nicknames)
primary_algos = rldb.get_primary_algos_from_papers(papers)
scores = [algo['breakout']['score'] for algo in primary_algos]

for nickname, score in zip(nickname, score):
    print('{:10s} | {:5.2f}'.format(nickname, score))
