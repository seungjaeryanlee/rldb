---
layout: page
title: Atari Berzerk Environment
permalink: /envs/gym/atari/berzerk/

redirect_from:
 - /envs/gym/atari-2600/berzerk/
 - /env/gym/atari/berzerk/
 - /env/gym/atari-2600/berzerk/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/berzerk.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls a green stick man. Using a joystick and a firing button that activates a laser-like weapon, the player navigates a simple maze filled with many robots, who fire lasers back at the player character. A player can be killed by being shot, by running into a robot or an exploding robot, coming into contact with the electrified walls of the maze itself, or by being touched by the player's nemesis, Evil Otto.

The function of Evil Otto, represented by a bouncing smiley face, is to quicken the pace of the game. Otto is unusual, with regard to games of the period, in that there is no way to kill him. Otto can go through walls with impunity and is attracted to the player character. If robots remain in the maze Otto moves slowly, about half as fast as the humanoid, but he speeds up to match the humanoid's speed once all the robots are killed. Evil Otto moves exactly the same speed as the player going left and right but he can move faster than the player going up and down; thus, no matter how close Otto is, the player can escape as long as they can avoid moving straight up or down.

The player advances by escaping from the maze through an opening in the far wall. Each robot destroyed is worth 50 points. Ideally, all the robots in the current maze have been destroyed before the player escapes, thus gaining the player a per-maze bonus (ten points per robot). The game has 65,536 rooms (256x256 grid), but due to limitations of the random number generation there are fewer than 1024 maze layouts (876 unique). It has only one controller, but two-player games can be accomplished by alternating at the joystick. The game is most difficult when the player enters a new maze, as there is only a short interval between entering the maze and all the robots in range firing at the player. For the beginner, this often means several deaths in rapid succession, as each death means starting a new maze layout.

As a player's score increases, the colors of the enemy robots change, and the robots can have more bullets on the screen at the same time. Once they reach the limit of simultaneous onscreen bullets, they cannot fire again until one or more of their bullets detonates; the limit applies to the robots as a group, not as individuals.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Berzerk_%28video_game%29)*


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
