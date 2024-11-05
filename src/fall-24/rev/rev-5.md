# Reverse Engineering 5: Decompilers
by Enzo Saracen

This week's topic is decompilers: tools that lift machine code from executables into higher-level source-like representations.
This is useful for static analysis of binaries when source code is not provided.
We will be demonstrating the features of decompilers using [Binary Ninja](https://binary.ninja/), a proprietary decompiler that provides both a local and cloud-based free version.

## Slides
<iframe src="https://docs.google.com/presentation/d/1q_uhRxN64ujR9i7FC0gXPe_fEXcIh_GDcx1RT2Ka-wU/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
A set of challenges with increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. You can filter for them on the platform by checking "rev" under "Categories", and "week 5" under "week". They are:

You can also practice using decompilers on some of the challenges from previous weeks that involve a binary:
- `rev/flow`
- `rev/galfrekcehc`
- `rev/jabeglnz`
- `rev/nested`
- `rev/dancing`
- `rev/boxing`

## Resources
The following resources are great tools for some of the reversing challenges:
- [Binary Ninja documentation](https://docs.binary.ninja/guide/index.html)
