---
layout: page
title: Atari H.E.R.O. Environment
permalink: /envs/gym/atari/hero/

redirect_from:
 - /envs/gym/atari-2600/hero/
 - /env/gym/atari/hero/
 - /env/gym/atari-2600/hero/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/hero.mp4' | absolute_url }}" type="video/mp4">
</video>

The player assumes control of Roderick Hero (sometimes styled as "R. Hero"), a one-man rescue team. Miners working in Mount Leone are trapped, and it's up to Roderick to reach them.

The player is equipped with a backpack-mounted helicopter unit, which allows him to hover and fly, along with a helmet-mounted laser and a limited supply of dynamite. Each level consists of a maze of mine shafts that Roderick must safely navigate in order to reach the miner trapped at the bottom. The backpack has a limited amount of power, so the player must reach the miner before the power supply is exhausted.

Mine shafts may be blocked by cave-ins or magma, which require dynamite to clear. The helmet laser can also destroy cave-ins, but more slowly than dynamite. Unlike a cave-in, magma is lethal when touched. Later levels include walls of magma with openings that alternate between open and closed requiring skillful navigation. The mine shafts are populated by spiders, bats and other unknown creatures that are deadly to the touch; these creatures can be destroyed using the laser or dynamite.

Some deep mines are flooded, forcing players to hover safely above the water. In later levels, monsters strike out from below the water. Some mine sections are illuminated by lanterns. If the lantern is somehow destroyed, the layout of that section becomes invisible. Exploding dynamite lights up the mine for a brief time.

Points are scored for each cave-in cleared and each creature destroyed. When the player reaches the miner, points are awarded for the rescue, along with the amount of power remaining in the backpack and for each remaining stick of dynamite. Extra lives are awarded for every 20,000 points scored.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/H.E.R.O.)*


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
