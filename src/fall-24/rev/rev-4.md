# Reverse Engineering 4: GDB
by Alexander Zhang

This week's topic is GDB, a tool that allows us to control the execution of processes and inspect their state.
This is useful for debugging, reverse engineering, and exploit development.
We will also learn about GEF, a GDB extension with lots of useful features for CTFs.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQmj2dNYYoUR41U2RdCynZUSHgIFRsa4uswnlm-I13fekNJiUAR7jZAE1uxw67YHl7wliUyAQqMJxKD/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
A set of challenges with increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. You can filter for them on the platform by checking "rev" under "Categories", and "week 5" under "week". They are:
You can practice using GDB on the challenges from previous weeks:
- `rev/bomb`
- `rev/bomb2`
- `rev/bomb3`
- `rev/bobomb`
- `rev/flow`
- `rev/galfrekcehc`
- `rev/salsa69`
- `rev/jabeglnz`
- `rev/nested`

We've also added some new challenges that are designed to be much easier to solve with GDB than with static analysis alone:
- `rev/dancing`
- `rev/boxing`

## Resources
The following resources are great tools for some of the reversing challenges:
- [GDB documentation](https://sourceware.org/gdb/documentation/): Information on using GDB
- [GDB reference card](https://www.sourceware.org/gdb/download/onlinedocs/refcard.pdf): Cheat sheet with common GDB commands
- [GEF documentation](https://hugsy.github.io/gef/): Information on how to install and use GEF
