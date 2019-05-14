---
layout: page
title: Atari Boxing Environment
permalink: /envs/gym/atari/boxing/

redirect_from:
 - /envs/gym/atari-2600/boxing/
 - /env/gym/atari/boxing/
 - /env/gym/atari-2600/boxing/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/boxing.mp4' | absolute_url }}" type="video/mp4">
</video>

Boxing is an Atari 2600 video game based on the sport of boxing. The game was designed by Activision programmer Bob Whitehead. Boxing shows a top-down view of two boxers, one white and one black. When close enough, a boxer can hit his opponent with a punch (executed by pressing the fire button on the Atari joystick). This causes his opponent to reel back slightly. Long punches score one point, while closer punches (power punches, from the manual) score two. There are no knockdowns or rounds. A match is completed either when one player lands 100 punches (a 'knockout') or two minutes have elapsed (a 'decision'). In the case of a decision, the player with the most landed punches is the winner. Ties are possible.

While the gameplay is simple, there are subtleties, such as getting an opponent on the 'ropes' and 'juggling' him back and forth between alternate punches. Boxing was made available on Microsoft's Game Room service for its Xbox 360 console and for Windows-based PCs on September 1, 2010.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Boxing_(1980_video_game))*


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
