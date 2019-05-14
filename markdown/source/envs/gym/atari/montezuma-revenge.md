---
layout: page
title: Atari Montezuma's Revenge Environment
permalink: /envs/gym/atari/montezuma-revenge/

redirect_from:
 - /envs/gym/atari-2600/montezumas-revenge/
 - /env/gym/atari/montezumas-revenge/
 - /env/gym/atari-2600/montezumas-revenge/
 - /envs/gym/atari/montezumas-revenge/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/montezuma-revenge.mp4' | absolute_url }}" type="video/mp4">
</video>

Montezuma's Revenge is an early example of the Metroidvania genre. The player controls a character called Panama Joe (a.k.a. Pedro), moving him from room to room in the labyrinthine underground pyramid of the 16th century Aztec temple of emperor Montezuma II, filled with enemies, obstacles, traps, and dangers. The objective is to score points by gathering jewels and killing enemies along the way. Panama Joe must find keys to open doors, collect and use equipment such as torches, swords, amulets, etc., and avoid or defeat the challenges in his path. Obstacles are laser gates, conveyor belts, disappearing floors and fire pits.

Movement is achieved by jumping, running, sliding down poles, and climbing chains and ladders. Enemies are skulls, snakes, and spiders. A further complication arises in the bottom-most floors of each pyramid, which must be played in total darkness unless a torch is found.

The pyramid is nine floors deep, not counting the topmost entry room that the player drops into at the start of each level, and has 99 rooms to explore. The goal is to reach the Treasure Chamber, whose entrance is in the center room of the lowest level. After jumping in here, the player has a short time to jump from one chain to another and pick up as many jewels as possible. However, jumping onto a fireman's pole will immediately take the player to the next level; when time runs out, the player is automatically thrown onto the pole.

There are nine difficulty levels in all. Though the basic layout of the pyramid remains the same from one level to the next, small changes in details force the player to rethink strategy. These changes include:

 * Blocking or opening up certain paths (by adding/removing walls or ladders)
 * Adding enemies and obstacles
 * Rearrangement of items
 * More dark rooms and fewer torches (in level 9, the entire pyramid is dark)
 * Enemies that do not disappear after they kill Panama Joe (starting with level 5)
 * The player can reach only the left half of the pyramid in level 1, and only the right half in level 2. Starting with level 3, the entire pyramid is open for exploration.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Montezuma%27s_Revenge_%28video_game%29)*


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
