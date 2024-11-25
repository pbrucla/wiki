# Crypto 7: Digital Signatures and Writeups
by Arnav Vora

Aside from just encrypting data, we also need a cryptographic mechanism to verify the identity of users. This is done through digital signatures. First, we discuss cryptograhic hashing functions, which act as one-way functions with the added benefit of collision resistance. Then, we discuss how we can construct a digital signature scheme using the same RSA primitives. Finally, we will have time to write writeups for challenges we have solved this quarter in cyber academy or elsewhere.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQvAkLsA2-z_STMMbMDSHbIGVtGWdBv7Le67-lTDHlHuRhTSiFcy4zY8NMa35HX9GCFUpXJKxfNqp2b/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.
- Challenge 1 - `crypto/rubiks-cube`
- Challenge 2 - `crypto/prime-factory`
- Challenge 3 - `crypto/rubiks-cube-2`
- Challenge 4 - `crypto/mitm`

## Resources
The following resources are great to practice/learn about the ciphers covered in the slides.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
- [cryptohack](https://cryptohack.org/): A website with many challenges related to cryptography
- [Alpertron](https://www.alpertron.com.ar/ECM.HTM): A fast online integer factorization calculator for large numbers
- [FactorDB](https://factordb.com/): A large online database of integers and their factors
- [DanBoneh](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf): A paper by a Stanford professor on RSA attacks
- [hackMD](https://hackmd.io/): A very useful markdown editor/publisher
- [Twin Prime](https://freedthelamb.com/blog/2023/twinprime/): Gary's writeup for Twin Primes from Buckeye CTF 2023, a good example of a writeup for an easier challenge.
- [SHA256-CTR](https://github.com/AVDestroyer/CTF-Writeups/blob/main/sdctf2023/sha256-ctr.md): Arnav's writeup for SHA256-CTR from SDCTF 2023, a good example of a writeup for a harder challenge.