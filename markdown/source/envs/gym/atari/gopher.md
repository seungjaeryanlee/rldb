---
layout: page
title: Atari Gopher Environment
permalink: /envs/gym/atari/gopher/

redirect_from:
 - /envs/gym/atari-2600/gopher/
 - /env/gym/atari/gopher/
 - /env/gym/atari-2600/gopher/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/gopher.mp4' | absolute_url }}" type="video/mp4">
</video>

The gopher tunnels left and right and up to the surface. When he makes a hole to the surface he will attempt to steal a carrot. The farmer must hit the gopher to send him back underground or fill in the holes to prevent him from reaching the surface. If gopher has taken any of the three carrots, a pelican will occasionally fly overhead and drop a seed which, if the farmer catches it, he can plant it in the place of the missing carrot. The longer the game, the faster the gopher gets. The game ends when the gopher successfully removes all three carrots. There are two skill levels and is for one or two players, giving a total of four game variations.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Gopher_%28video_game%29)*


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
