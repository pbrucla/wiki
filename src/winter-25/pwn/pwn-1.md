# Pwn 1: Pwn review, Ret2Win

by Jason An

This quarter, we'll be focusing on binary exploitation, also known as "pwn" in the CTF community. We'll study how memory corruption from vulnerabilities like buffer overflows and improper usage of format strings can lead to arbitrary code execution, as well as ways to bypass modern mitigations for said vulnerabilities.

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSuWJBnzscaJT3GAzuGT8f21xUaLqawfuUHSIMhhDQVVRKOwj8l1Gx8UplqmmW5WqxmhU-v1ekn3-tW/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;"  allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRClvyaaPBEAN_3Wk-wuTdN7TUqEv_ak3ZWLWWCZWkJfFx7web200vqJIYsn8-3uc4BNlcPFa3Qi_Ty/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges

The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.

Intro to Pwn:

- Challenge 1 - `pwn/pwn0`
- Challenge 2 - `pwn/ret2win`
- Challenge 3 - `pwn/bot`
- Challenge 4 - `pwn/aplet123`

ROP:

- Challenge 1: `pwn/ret2libc`
- Challenge 2: `pwn/ret2libc2`
- Challenge 3: `pwn/sus`

## Resources

The following resources are great tools for some of the pwn challenges:

- [GEF](https://hugsy.github.io/gef/): A GDB extension with lots of useful features for pwn.
- [pwntools](https://github.com/Gallopsled/pwntools): A Python library useful for writing solve scripts.
- [pwninit](https://github.com/io12/pwninit): A tool for setting up pwn challenges locally.
- [xgadget](https://github.com/entropic-security/xgadget): A tool for finding ROP gadgets.
