"""
Helper functions for `generate_md_atari.py` and `generate_md_mujoco.py`.
"""
from string import Template


def get_template(filename):
    """Load template file."""
    with open(filename, 'r') as f:
        template = Template(f.read())

    return template

def populate_template(template, feed_dict):
    """Populate template."""
    result = template.substitute(feed_dict)

    return result

def save_file(filename, result):
    """Save text into file."""
    with open(filename, 'w') as f:
        f.write(result)

def get_best_source_link(entry):
    """Return best source link from given entry."""
    source_link = { 'type': '', 'url': '' }
    for link in entry['source-links']:
        if link['type'] == 'ArXiv': # Best link
            source_link = link
        elif link['type'] == 'PDF': # Second-best link
            if not source_link or source_link['type'] != 'ArXiv':
                source_link = link
        elif link['type'] == 'GitHub':
            if not source_link or source_link['type'] not in ['ArXiv', 'PDF']:
                source_link = link
        else:
            if not source_link or source_link['type'] not in ['ArXiv', 'PDF', 'GitHub']:
                source_link = link

    return source_link

def entries_to_table(entries):
    """Generate Markdown table from rldb entries."""
    table = ''
    table += '| Result | Algorithm | Source |\n'
    table += '|--------|-----------|--------|\n'
    for entry in entries:
        source_link = get_best_source_link(entry)

        # Boldface if Human or Random
        if entry['algo-nickname'] in ['Human', 'Random']:
            table += '| {} | **{}** | [{}]({}) |\n'.format(
                entry['score'], entry['algo-nickname'], entry['source-title'], source_link['url'],
            )
        else:
            table += '| {} | {} | [{}]({}) |\n'.format(
                entry['score'], entry['algo-nickname'], entry['source-title'], source_link['url'],
            )

    return table