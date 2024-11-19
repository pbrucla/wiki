# Binary Exploitation 1: Intro to Pwn
by Alexander Zhang

Binary exploitation, also known as pwn, is a category of challenges where we gain control over vulnerable programs by exploiting memory safety vulnerabilities.
We will learn about basic pwn concepts today and exploit buffer overflow vulnerabilities, where a program can be tricked into writing data past the end of a buffer in memory.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSuWJBnzscaJT3GAzuGT8f21xUaLqawfuUHSIMhhDQVVRKOwj8l1Gx8UplqmmW5WqxmhU-v1ekn3-tW/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
A set of challenges with increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. You can filter for them on the platform by checking "rev" under "Categories", and "week 2" under "week". They are:
- `pwn/pwn0`
- `pwn/ret2win`
- `pwn/bot`
- `pwn/aplet123`

## Resources
The following resources are great tools for some of the pwn challenges:
- [GEF](https://hugsy.github.io/gef/): A GDB extension with lots of useful features for pwn.
- [pwntools](https://github.com/Gallopsled/pwntools): A Python library useful for writing solve scripts.
- [pwninit](https://github.com/io12/pwninit): A tool for setting up pwn challenges locally.
