# Crypto 4: Lattices

by Arnav Vora

We will cover a more advanced topic in cryptography: lattices. These are essential in many cryptographic attacks. Lattices can be used to describe linear systems of integers, and are very powerful when solving for inequalities/small solutions of linear integer equations. When using lattice-based attacks, we often rely on _lattice reduction_, which transforms a lattice basis into a nearly orthonormal one, allowing one to find small integer solutions to systems. We will see some applications of lattice attacks in LCGs (linear congruential generators) and other instances where small integer solutions are needed.

## Slides

Slides that I presented for PBR last year, relevant for today's lesson!

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTpv_O8qZaOODbzTtEQxz6ixgdPkwkoID5rHR6lKunc0vgUwCeVjKKAVjPJacj__A2LaYmAZ4nwYgEu/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges

The following challenges have been found in various CTF competitions, and are good examples of lattice-based attacks

- LACTF 2024: `crypto/any-percent-ssg`
- LACTF 2025: `crypto/shuffle-revenge`
- glacierCTF 2024: `crypto/signmeup`

## Resources

The following resources are great to practice/learn about the concepts covered today:

- [Matthew Bolan: Minecraft seedcracking](https://www.youtube.com/watch?v=8CKh4x4iK38&list=PLke4P_1UHlmB8sB1oGdcea4SeBH0yZy5B): A nice video series that described how lattices can be used to crack Minecraft's LCG and find seeds that satisfy some constraints.
- [Lattice tutorial](https://eprint.iacr.org/2023/032.pdf): A good tutorial for using lattices in cryptography.
- [Another lattice tutorial](https://ur4ndom.dev/static/files/latticetraining/practical_lattice_reductions.pdf): Another good tutorial for lattices in cryptography, applied to common CTF challenges.
- [SageMath](https://www.sagemath.org/): An open-source mathematics system that integrates with Python and is incredibly useful in many cryptography challenges.
