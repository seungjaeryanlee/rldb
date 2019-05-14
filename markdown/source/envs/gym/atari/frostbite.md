---
layout: page
title: Atari Frostbite Environment
permalink: /envs/gym/atari/frostbite/

redirect_from:
 - /envs/gym/atari-2600/frostbite/
 - /env/gym/atari/frostbite/
 - /env/gym/atari-2600/frostbite/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/frostbite.mp4' | absolute_url }}" type="video/mp4">
</video>

The bottom two thirds of the screen are covered by a mass of water with four rows of ice blocks floating horizontally. The player moves by jumping from one row to another while trying to avoid various kinds of foes including crabs and birds. There are also fish which grant extra points.

On the top of the screen is the shore where the player must build the Igloo. From the fourth level onwards there is also a polar bear walking around on the shore which must be avoided.

The game levels alternate between large ice blocks and little ice pieces. The levels with the little pieces are actually easier, since one can walk left or right over them without falling in the water.

Each time the player jumps on a piece of ice in a row its color changes from white to blue and the player gets an ice block in the Igloo on the shore. The player has the ability to change the direction in which the ice is flowing by pressing the fire button, but that costs a piece of the Igloo.

After the player has jumped on all the pieces on the screen, they all turn back to white and one can jump on them again. When all the 15 ice blocks required for building the Igloo are gathered, the player has to get back to the shore and get inside it, thus proceeding to the next level. On every level the enemies and the ice blocks move slightly faster than in the previous level making the game more difficult.

Each level must be completed in 45 seconds, (represented as the declining temperature,) else the eskimo dies frozen. The faster the level is completed the more bonus points are awarded to the player. If player makes it past level 20, a "magic" fish will appear between the temperature gage and the number of lives remaining, this serves no real purpose other than as an Easter egg to the game.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Frostbite_%28video_game%29)*


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
