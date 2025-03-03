# Crypto 5: PRNGs, Writeups

by Arnav Vora

We will first briefly cover various PRNG (pseudo-random number generator) algorithms, and explain their importance in security. A very simply PRNG algorithm is called an LCG (linear congruential generator), using linear congruences to generate numbers. We will explore why it isn't secure and how to exploit it. Finally, we will have time to write writeups for challenges we have solved this quarter in cyber academy or elsewhere.

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSYl_0C2MdsoH_MgHkAccNQlqwBKafactSC3nUrRgdodNi0ezqXbXMG6J_ZokNQoP2Jwl3p-9hSPo2L/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges

The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.

- Challenge 1 - `crypto/letsgogambling`
- Challenge 2 - `crypto/letsgogamblingagain`

## Resources

The following resources are great to practice/learn about the concepts covered in the slides.

- [Cracking LCGs with unknown coefficients](https://security.stackexchange.com/questions/4268/cracking-a-linear-congruential-generator): A thread on how to crack LCGs with unknown coefficents. This can be used to solve `crypto/letsgogamblingagain`.
- [Matthew Bolan](https://www.youtube.com/channel/UCB4XuRBJZBOpnoJSWekMohw): A youtuber who covers Minecraft math for speedrunners. Has some videos on LCGs and exploiting the Minecraft randomness engine that are very interesting.
- [hackMD](https://hackmd.io/): A very useful markdown editor/publisher
- [Twin Prime](https://freedthelamb.com/blog/2023/twinprime/): Gary's writeup for Twin Primes from Buckeye CTF 2023, a good example of a writeup for an easier challenge.
- [SHA256-CTR](https://github.com/AVDestroyer/CTF-Writeups/blob/main/sdctf2023/sha256-ctr.md): Arnav's writeup for SHA256-CTR from SDCTF 2023, a good example of a writeup for a harder challenge.
