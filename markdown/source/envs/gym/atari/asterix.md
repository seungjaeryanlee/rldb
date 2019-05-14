---
layout: page
title: Atari Asterix Environment
permalink: /envs/gym/atari/asterix/

redirect_from:
 - /envs/gym/atari-2600/asterix/
 - /env/gym/atari/asterix/
 - /env/gym/atari-2600/asterix/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/asterix.mp4' | absolute_url }}" type="video/mp4">
</video>

Asterix (Taz) was released by Atari in 1983 for the Atari 2600 and features the Looney Tunes character the Tasmanian Devil in a food frenzy. Within the game, Taz only appears as a tornado. The same game was released outside the United States featuring Asterix instead of Taz.

The gameplay is rather simple. The player guides Taz between the stage lines in order to eat hamburgers and avoid the dynamites. The game does not use any buttons and the difficulty increases by increasing the speed of the objects on screen. As the game progresses, the burgers may change into other edible or drinkable objects such as beer kegs, hot dogs, etc. There are not many sound effects in the game except a blipping sound when the player hits an edible object and another sound that resembles of explosion when the player hits dynamite.

*Description from [RetroGames](https://www.retrogames.cz/play_386-Atari2600.php)*


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
