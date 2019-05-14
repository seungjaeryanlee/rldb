---
layout: page
title: Atari Venture Environment
permalink: /envs/gym/atari/venture/

redirect_from:
 - /envs/gym/atari-2600/venture/
 - /env/gym/atari/venture/
 - /env/gym/atari-2600/venture/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/venture.mp4' | absolute_url }}" type="video/mp4">
</video>

The goal of Venture is to collect treasure from a dungeon. Winky is equipped with a bow and arrow and explores a dungeon with rooms and hallways. The hallways are patrolled by large, tentacled monsters named Hallmonsters, which cannot be killed, injured, or stopped in any way. Once in a room, Winky may kill monsters, avoid traps and gather treasures. If they stay in any room too long, a Hallmonster will enter the room, chase and kill them. In this way, the Hallmonsters serve the same role as "Evil Otto" in the arcade game Berzerk. The more quickly the player finishes each level, the higher their score.

The goal of each room is only to steal the room's treasure. In most rooms, it is possible (though difficult) to steal the treasure without defeating the monsters within. Some rooms have traps that are only sprung when the player picks up the treasure. For instance, in "The Two-Headed Room", two 2-headed ettins appear the moment the player picks up the prize.

Winky dies if he touches a monster or Hallmonster. Dead monsters decay over time and their corpses may block room exits, delaying Winky and possibly allowing the Hallmonster to enter. Shooting a corpse causes it to regress back to its initial death phase. The monsters themselves move in specific patterns but may deviate to chase the player, and the game's AI allows them to dodge the player's shots with varying degrees of "intelligence" (for example, the snakes of "The Serpent Room" are relatively slow to dodge arrows, the trolls of "The Troll Room" are quite adept at evasion).

The game consists of three different dungeon levels with different rooms. After clearing all the rooms in a level the player advances to the next. After three levels the room pattern and monsters repeat, but at a higher speed and with a different set of treasures.

The different dungeons in each level are as follows:

 * Level 1 - The Wall Room, The Serpent Room, The Skeleton Room, The Goblin Room
 * Level 2 - The Two-Headed Room, The Dragon Room, The Spider Room, The Troll Room
 * Level 3 - The Genie Room, The Demon Room, The Cyclops Room, The Bat Room


*Description from [Wikipedia](https://en.wikipedia.org/wiki/Venture_(video_game))*


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
