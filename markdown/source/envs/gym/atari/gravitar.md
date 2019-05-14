---
layout: page
title: Atari Gravitar Environment
permalink: /envs/gym/atari/gravitar/

redirect_from:
 - /envs/gym/atari-2600/gravitar/
 - /env/gym/atari/gravitar/
 - /env/gym/atari-2600/gravitar/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/gravitar.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls a small blue spacecraft. The game starts in a fictional solar system with several planets to explore. If the player moves his ship into a planet, he will be taken to a side-view landscape. Unlike many other shooting games, gravity plays a fair part in Gravitar: the ship will be pulled slowly to the deadly star in the overworld, and downward in the side-view levels.

The player has five buttons: two to rotate the ship left or right, one to shoot, one to activate the thruster, and one for both a tractor beam and force field. Gravitar, Asteroids, Asteroids Deluxe and Space Duel all used similar 5-button controlling system.

In the side-view levels, the player has to destroy red bunkers that shoot constantly, and can also use the tractor beam to pick up blue fuel tanks. Once all of the bunkers are destroyed, the planet will blow up, and the player will earn a bonus. Once all planets are destroyed, the player will move onto another solar system.

The player will lose a life if he crashes into the terrain or gets hit by an enemy's shot, and the game will end immediately if fuel runs out.

Gravitar has 12 different planets. Red Planet is available in all 3 phases in the universe; it contains a reactor. Shooting the reactor core activates a link. Escaping the reactor successfully moves the player to the next phase of planets, awards bonus points and 7500 units of fuel. Reactor escape time reduces after each phase and eventually becomes virtually impossible to complete.

After completing all 11 planets (or alternatively completing the reactor three times) the player enters the second universe and the gravity will reverse. Instead of dragging the ship towards the planet surface, the gravity pushes it away. In the third universe the landscape becomes invisible and the gravity is positive again. The final, fourth universe, has invisible landscape and reverse gravity. After completing the fourth universe the game starts over. However, the reactor escape time will never reset back to high levels again

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Gravitar)*


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
