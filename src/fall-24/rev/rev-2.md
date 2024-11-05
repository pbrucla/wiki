# Reverse Engineering 2: Assembly
by Jason An

We'll be diving into x86\_64/amd64 assembly this week. Being the dominant architecture in laptops, being able to reverse x86 executables is a crucial skill in reverse engineering, and still has many transferrable skills to reversing other architectures. For this week, we'll cover basic x86 instructions, and how to read and work with assembly.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT5IcZev_bBPwmnsDo_3L4s_7UIbqQC624t83jOkvFXlcLa9fRl4WM5B963OHaqBjXPF7_8Mpzne-ZW/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
A set of challenges with increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. You can filter for them on the platform by checking "rev" under "Categories", and "week 3" under "week". They are:
- `rev/bomb`
- `rev/bobomb`
- `rev/bomb2`
- `rev/jabeglnz`
- `rev/galfrekcehc`

## Resources
The following resources are great tools for some of the reversing challenges:
- [objdump command](https://man7.org/linux/man-pages/man1/objdump.1.html): A command that lets you disassemble an executable to extract the assembly
- [x86 reference](https://www.felixcloutier.com/x86/): An HTML rendering of the Intel handbook containing details on every x86 instruction
