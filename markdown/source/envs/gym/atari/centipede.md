---
layout: page
title: Atari Centipede Environment
permalink: /envs/gym/atari/centipede/

redirect_from:
 - /envs/gym/atari-2600/centipede/
 - /env/gym/atari/centipede/
 - /env/gym/atari-2600/centipede/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/centipede.mp4' | absolute_url }}" type="video/mp4">
</video>

The player is represented by a small, "somewhat humanoid head" at the bottom of the screen, later depicted as a caped, elf-like character on the Atari 2600, Atari 5200 and Atari 7800 cartridge graphics (though described as being a garden gnome in the trivia section of the cell phone interpretation). The player moves the character about the bottom area of the screen with a trackball and fires laser shots at a centipede advancing from the top of the screen down through a field of mushrooms. Shooting any section of the centipede creates a mushroom; shooting one of the middle segments splits the centipede into two pieces at that point. Each piece then continues independently on its way down the board, with the first section of the rear piece becoming a new head. If the head is destroyed, the section behind it becomes the next head.

The centipede starts at the top of the screen, traveling either left or right. When it hits a mushroom or the edge of the screen, it drops one level and switches direction. Thus, more mushrooms on the screen cause the centipede to descend more rapidly. The player can destroy mushrooms by shooting them, but each takes four hits to destroy.

If the centipede reaches the bottom of the screen, it moves back and forth within the player area and one-segment "head" centipedes are periodically added. This continues until the player has eliminated both the original centipede and all heads. When all the centipede's segments are destroyed, a new centipede forms at the top of the screen. Every time a centipede is eliminated, however, the next one is one segment shorter and is accompanied by one additional, fast-moving "head" centipede.

The player is also menaced by other creatures besides the centipedes. Fleas drop vertically, leaving additional mushrooms in their path; they appear when fewer than five mushrooms are in the player movement area, though the number required increases with level of difficulty. Spiders move across the player area in a zig-zag fashion and occasionally eat some of the mushrooms. Scorpions move horizontally across the screen and poison every mushroom they touch, but these never appear in the player movement region. A centipede touching a poisoned mushroom hurtles straight down toward the player area, then returns to normal behavior upon reaching it.

A player loses a life when hit by a centipede or another enemy, such as a spider or a flea, after which any poisoned or partially damaged mushrooms revert to normal. Points are awarded for each regenerated mushroom. A game ends if all lives are gone.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Centipede_%28video_game%29)*


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
