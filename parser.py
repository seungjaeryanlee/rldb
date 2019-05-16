"""
Generate entries.py from raw table in papers.
"""
atari57_envs = [
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
dmlab30_envs = [
    "rooms_collect_good_objects_test",
    "rooms_exploit_deferred_effects_test",
    "rooms_select_nonmatching_object",
    "rooms_watermaze",
    "rooms_keys_doors_puzzle",
    "language_select_described_object",
    "language_select_located_object",
    "language_execute_random_task",
    "language_answer_quantitative_question",
    "lasertag_one_opponent_large",
    "lasertag_three_oponents_large",
    "lasertag_one_opponent_small",
    "lasertag_three_opponents_small",
    "natlab_fixed_large_map",
    "natlab_varying_map_regrowth",
    "natlab_varying_map_randomized",
    "skymaze_irreversible_path_hard",
    "skymaze_irreversible_path_varied",
    "pyschlab_arbitrary_visuomotor_mapping",
    "pyschlab_continuous_recognition",
    "pyschlab_sequential_comparison",
    "pyschlab_visual_search",
    "explore_object_locations_small",
    "explore_object_locations_large",
    "explore_obstructed_goals_small",
    "explore_obstructed_goals_large",
    "explore_goal_locations_small",
    "explore_goal_locations_large",
    "explore_object_rewards_few",
    "explore_object_rewards_many",
]


def parse_scores(get_score_from_line):
    with open('input.txt', 'r') as f:
        lines = f.readlines()[1:]
        scores = [get_score_from_line(line.strip()) for line in lines]

    return scores


def generate_entries(envs: list, scores: list, env_variant: str = ''):
    if len(envs) != len(scores):
        raise AssertionError('Number of environments does not match number of scores. Check which environments are used in the paper!')

    with open('output.txt', 'w') as f:
        f.write("entries = [\n")
        for env, score in zip(envs, scores):
            f.write("    {\n")
            f.write("        \"env-title\": \"{}\",\n".format(env))
            if env_variant:
                f.write("        \"env-variant\": \"{}\",\n".format(env_variant))
            f.write("        \"score\": {},\n".format(score))
            f.write("    },\n")
        f.write("]\n")


if __name__ == '__main__':
    # Prefer using backward-indices (-1, -2) since environment names can contain spaces
    scores = parse_scores(lambda line: line.split(' ')[-1].replace(',', ''))

    # env_variant should be '', 'Human start' or 'No-op start'
    generate_entries(atari57_envs, scores, env_variant='Human start')
