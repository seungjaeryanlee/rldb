---
layout: page
title: Atari Kangaroo Environment
permalink: /envs/gym/atari/kangaroo/

redirect_from:
 - /envs/gym/atari-2600/kangaroo/
 - /env/gym/atari/kangaroo/
 - /env/gym/atari-2600/kangaroo/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/kangaroo.mp4' | absolute_url }}" type="video/mp4">
</video>

There are four different levels. Each of them consist of the mother kangaroo on the bottom floor trying to reach the top floor where her joey is being held captive by some monkeys. On each of the levels, there are monkeys who are throwing apples at the mother kangaroo. Sometimes the apples are thrown so that she must jump over them and sometimes they are thrown so that she must duck. If she gets face to face with one of the monkeys, she can punch the monkey with a boxing glove. She can also punch and destroy apples if they're thrown in level with her gloves. Also, there are pieces of fruit that she can jump up and get for points. Additionally, there is at least one bell on each level that she can hit so that more fruits will appear. She must be wary of the big Ape, who will occasionally appear and try to take her gloves away from her. The level must be completed before the time runs out, otherwise the player will lose a life.

Levels 1, 2 and 4 consist of different platforms that the mother kangaroo must jump onto or climb onto via a ladder. On the third level, the cage in which the kid kangaroo is imprisoned is held up by an entire troop of monkeys and there is a horde of apples that the monkey will unleash if five of them climb up there. On this level, the mother kangaroo must punch each monkey in the stack several times until the cage is lowered and when the cage has been lowered enough, the mother kangaroo must climb to the next floor to get to the kid kangaroo before the cage is raised again or before the monkeys have an avalanche of apple cores unleashed.

Kangaroo has a number of clearly visible glitches in the graphics, such as sprites briefly flickering.[

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Kangaroo_%28video_game%29)*


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
