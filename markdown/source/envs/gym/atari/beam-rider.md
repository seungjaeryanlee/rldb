---
layout: page
title: Atari Beam Rider Environment
permalink: /envs/gym/atari/beam-rider/

redirect_from:
 - /envs/gym/atari-2600/beam-rider/
 - /env/gym/atari/beam-rider/
 - /env/gym/atari-2600/beam-rider/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/beam-rider.mp4' | absolute_url }}" type="video/mp4">
</video>

Beamrider takes place above Earth's atmosphere, where a large alien shield called the Restrictor Shield surrounds the Earth. The player's objective is to clear the Shield's 99 sectors of alien craft while piloting the Beamrider ship. The Beamrider is equipped with a short-range laser lariat and a limited supply of torpedoes. The player is given three at the start of each sector.

To clear a sector, fifteen enemy ships must be destroyed. A "Sentinel ship" will then appear, which can be destroyed using a torpedo (if any remain) for bonus points. Some enemy ships can only be destroyed with torpedoes, and some must simply be dodged. Occasionally during a sector, "Yellow Rejuvenators" (extra lives) appear. They can be picked up for an extra ship, but if they are shot they will transform into ship-damaging debris.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Beamrider)*


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
