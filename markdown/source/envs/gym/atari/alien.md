---
layout: page
title: Atari Alien Environment
permalink: /envs/gym/atari/alien/

redirect_from:
 - /envs/gym/atari-2600/alien/
 - /env/gym/atari/alien/
 - /env/gym/atari-2600/alien/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/alien.mp4' | absolute_url }}" type="video/mp4">
</video>

In this game based, loosely, on the movie of the same name, you have to move through a maze (the halls of your ship in the manual), ala Pac-Man, collecting dots (destroying alien eggs).

If you collect the power dot (pulsar), you can kill any of the three aliens, for a short time. There are only three enemies in the maze at a time, there is a bonus item at times and only one power dot (pulsar) at a time. When you grab the pulsar, it will next appear in one of two other spots.

After you clear one level, you get a bonus game. You have to move up the screen to the prize at the top past several aliens, reminiscent of Freeway. You do not lose a man if you fail but you only have eight seconds to do it then you are off the the next, harder level.

*Description from [RetroGames](https://www.retrogames.cz/play_251-Atari2600.php)*


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
