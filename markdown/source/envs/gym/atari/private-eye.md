---
layout: page
title: Atari Private Eye Environment
permalink: /envs/gym/atari/private-eye/

redirect_from:
 - /envs/gym/atari-2600/private-eye/
 - /env/gym/atari/private-eye/
 - /env/gym/atari-2600/private-eye/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/private-eye.mp4' | absolute_url }}" type="video/mp4">
</video>

n Private Eye, players assume the role of Pierre Touché, a private investigator who has been assigned the task of capturing the criminal mastermind, Henri Le Fiend. Le Fiend is implicated in a number of crimes across the city, and the player must find the clues and the stolen property in order to successfully arrest Le Fiend.

The game consists of four separate cases. Using a specially-built Model A that can jump over obstacles, players must search the city for a specific clue to the crime and for the object stolen in the crime. Each item must then be returned to its point of origin; the clue is taken to a business to verify it came from there, and the stolen object is returned to its rightful owner. These items may be discovered in any order, but players may carry only one item at a time. When both items have been located and returned, then the player must locate and capture Le Fiend, and finally take him to jail, successfully closing the case.

However, the city is full of street thugs who will attack the player. If the player is hit while carrying an item (either the clue or the stolen property), the item is lost and must be re-located. Further, each case has a statute of limitations, which serves as the game's time limit. To win the game, the player must locate and verify the clue, locate and return the stolen property, and lastly locate Le Fiend and take him to jail within the time allotted.

The player starts with 1000 "merit points". Points are lost whenever the player hits an obstacle or is attacked by a thug, and are awarded whenever an item is located, subsequently returned, and when a thug (or Le Fiend himself) is nabbed. Each case represents a separate game variation; when the case is solved or time runs out, the game ends. A fifth variation requires the player to solve all four crimes at the same time.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Q*bert)*


## Performances of RL Agents {#performances}

We list various reinforcement learning algorithms that were tested in this environment. These results are from [RL Database](https://github.com/seungjaeryanlee/rldb). If this page was helpful, please consider giving a star!

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/seungjaeryanlee/rldb" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star seungjaeryanlee/rldb on GitHub">Star</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
