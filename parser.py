"""
Generate entries.py from raw table in papers.
"""
envs = [
    'atari-alien',
    'atari-amidar',
    'atari-assault',
    'atari-asterix',
    'atari-asteroids',
    'atari-atlantis',
    'atari-bank-heist',
    'atari-battle-zone',
    'atari-beam-rider',
    'atari-berzerk',
    'atari-bowling',
    'atari-boxing',
    'atari-breakout',
    'atari-centipede',
    'atari-chopper-command',
    'atari-crazy-climber',
    'atari-defender',
    'atari-demon-attack',
    'atari-double-dunk',
    'atari-enduro',
    'atari-fishing-derby',
    'atari-freeway',
    'atari-frostbite',
    'atari-gopher',
    'atari-gravitar',
    'atari-hero',
    'atari-ice-hockey',
    'atari-jamesbond',
    'atari-kangaroo',
    'atari-krull',
    'atari-kung-fu-master',
    'atari-montezuma-revenge',
    'atari-ms-pacman',
    'atari-name-this-game',
    'atari-phoenix',
    'atari-pitfall',
    'atari-pong',
    'atari-private-eye',
    'atari-qbert',
    'atari-riverraid',
    'atari-road-runner',
    'atari-robotank',
    'atari-seaquest',
    'atari-skiing',
    'atari-solaris',
    'atari-space-invaders',
    'atari-star-gunner',
    'atari-surround',
    'atari-tennis',
    'atari-time-pilot',
    'atari-tutankham',
    'atari-up-n-down',
    'atari-venture',
    'atari-video-pinball',
    'atari-wizard-of-wor',
    'atari-yars-revenge',
    'atari-zaxxon',
]


def parse_scores():
    with open('input.txt', 'r') as f:
        lines = f.readlines()[1:]
        scores = [line.strip().split(' ')[-1] for line in lines]

    return scores


def generate_entries(envs: list, scores: list, env_variant: str = ''):
    if len(envs) != len(scores):
        raise AssertionError('Number of environments does not match number of scores. Check which environments are used in the paper!')

    with open('output.txt', 'w') as f:
        f.write("[\n")
        for env, score in zip(envs, scores):
            f.write("    {\n")
            f.write("        \"env-title\": \"{}\",\n".format(env))
            if env_variant:
                f.write("        \"env-variant\": \"{}\",\n".format(env_variant))
            f.write("        \"score\": {},\n".format(score))
            f.write("    },\n")
        f.write("]\n")


if __name__ == '__main__':
    scores = parse_scores()

    # env_variant should be '', 'Human start' or 'No-op start'
    generate_entries(envs, scores, env_variant='Human start')
