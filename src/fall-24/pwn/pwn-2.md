# Binary Exploitation 1: Return-Oriented Programming
by Alexander Zhang

Modern systems have exploit mitigations such as the NX bit that prevent writable memory from being executed.
This prevents shellcode injection attacks, where a vulnerability causes the program to execute malicious code that is injected into the program's memory.
Return-oriented programming is a powerful technique that bypasses these mitigations by taking advantage of the x86 `ret` instruction to chain together bits of existing code in the target program instead of injecting new code.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRClvyaaPBEAN_3Wk-wuTdN7TUqEv_ak3ZWLWWCZWkJfFx7web200vqJIYsn8-3uc4BNlcPFa3Qi_Ty/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
A set of challenges with increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. You can filter for them on the platform by checking "rev" under "Categories", and "week 9" under "week". They are:
- `pwn/ret2libc`
- `pwn/ret2libc2`
- `pwn/sus`

## Resources
The following resources are great tools for some of the pwn challenges:
- [xgadget](https://github.com/entropic-security/xgadget): A tool for finding ROP gadgets.
- [GEF](https://hugsy.github.io/gef/): A GDB extension with lots of useful features for pwn.
- [pwntools](https://github.com/Gallopsled/pwntools): A Python library useful for writing solve scripts.
- [pwninit](https://github.com/io12/pwninit): A tool for setting up pwn challenges locally.
