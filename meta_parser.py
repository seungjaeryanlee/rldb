#!/usr/bin/env python3
"""Parse metdata from ArXiv.org."""
import os
import requests
from string import Template

from bs4 import BeautifulSoup


def parse_arxiv(arxiv_tag):
    arxiv_link = "https://arxiv.org/abs/{}".format(arxiv_tag)
    result = requests.get(arxiv_link)
    soup = BeautifulSoup(result.content, "lxml")

    # TITLE
    title = soup.select("#abs > .title")[0].text[6:]
    print(title)

    # NICKNAME
    nickname = input('What should the nickname of this paper be?: ')
    paper_folder_name = input('What should the folder name of this paper be? (except paper__ prefix): ')

    # AUTHORS
    authors = soup.select('.authors > a')
    authors = [author.text for author in authors]
    print(authors)

    authors_str = "[\n"
    for author in authors:
        authors_str += "        \"{}\",\n".format(author)
    authors_str += "    ],"

    # LINKS
    pdf_link = "https://arxiv.org/pdf/{}.pdf".format(arxiv_tag)

    # ARXIV VERSION
    version = soup.select('#abs > .dateline')[0].text[-3:-2]
    print(version)

    # BIBTEX
    bibliography = """@misc{{{tag},
    author = {{{authors}}},
    title = {{{title}}},
    year = {{{year}}},
    eprint = {{arXiv:{tag}}},
}}""".format(tag=arxiv_tag, authors=' and '.join(authors), title=title, year='20' + arxiv_tag[:2])
    print(bibliography)

    feed_dict = {
        "title": title,
        "nickname": nickname,
        "authors_str": authors_str,
        "arxiv_link": arxiv_link,
        "pdf_link": pdf_link,
        "arxiv_tag": arxiv_tag,
        "version": version,
        "bibliography": bibliography,
    }

    ## Generate __init__.py
    with open('meta_template.txt') as f:
        template = Template(f.read())

    result = template.substitute(feed_dict)

    os.mkdir('rldb/db/paper__{}'.format(paper_folder_name))
    with open('rldb/db/paper__{}/__init__.py'.format(paper_folder_name), 'w') as f:
        f.write(result)


def main():
    arxiv_tag = input('Please input the arxiv tag (ex. 1509.06461): ')
    parse_arxiv(arxiv_tag)


if __name__ == '__main__':
    main()
