# Reverse Engineering 1: Intro to Reverse Engineering
by Jason An

Reverse engineering is a field of cybersecurity that involves figuring out what a program, often compiled, does, in order to achieve some kind of goal, like bypassing a license check or finding a vulnerability in the software. From professional positions like vulnerability research and malware analysis, to hobbyist activities like game modding or DRM cracking, reverse engineering has a wide variety of interesting applications in cybersecurity. We'll start off by learning basic reverse engineering principles on programs with full to nearly-full source code access, and then move towards learning how to reverse engineer *compiled* executables later on.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR8bjTTxOSkbfIB5fNkM6WJs2ZlWACVmUhmwgGQWKuEBsMKpu-pdUQMGBOxy4Ew5cV8S1xtSeWADM7b/embed?start=false&loop=false&delayms=3000" frameborder="0" width="1440" height="839" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
A set of challenges with increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. You can filter for them on the platform by checking "rev" under "Categories", and "week 2" under "week". They are:
- `rev/Character Numbers`
- `rev/just-dance`
- `rev/brick-maze`

## Resources
The follow resources are great tools for some of the reversing challenges:
- [Online Java Decompiler](https://www.decompiler.com): An entirely online tool that can decompile Java jar/class files back to decent-quality source code.
- [repl.it](https://replit.com): A website that lets you run many different programming languages online, which you can use to play around with programs if you don't want to install them locally.
- [CyberChef](https://gchq.github.io/CyberChef/): An online tool that has a variety of different encoding and encryption schemes, which may be useful.
