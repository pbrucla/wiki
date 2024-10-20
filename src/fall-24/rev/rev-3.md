# Reverse Engineering 3: Assembly Part 2
by Jason An

We'll be continuing our dive into x86 assembly this week. We'll finish the slides we didn't cover last week, and then move onto learning about how memory works.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTrUOCPa0aKuX-wixfgmlrxUiZRQJWknUT2exA2TlLOG1G78ZMz_kS39G7AvOEbeXvi2olci9cIVVKv/embed?start=false&loop=false&delayms=3000" frameborder="0" width="1440" height="839" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
A set of challenges with increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. You can filter for them on the platform by checking "rev" under "Categories", and "week 3" under "week". They are:
- `rev/bomb2`
- `rev/bobomb`
- `rev/jabeglnz`
- `rev/galfrekcehc`

## Resources
The follow resources are great tools for some of the reversing challenges:
- [objdump command](https://man7.org/linux/man-pages/man1/objdump.1.html): A command that lets you disassemble an executable to extract the assembly
- [x86 reference](https://www.felixcloutier.com/x86/): An HTML rendering of the Intel handbook containing details on every x86 instruction
