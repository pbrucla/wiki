# Crypto 6: RSA Attacks
by Gary Song

Over the many years since RSA was presented to the world, an enormous amount of research has been put into find different vulnerabilities. While nothing has been found for standard padded RSA, there are several cases of misuse that lead to vulnerabilties being present. These can range from poor parameter generation causing easy factoring to information leakage through auxillary means.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR4GbYsYQYM2YEUwV3by1aDm-p_rrnnzJE-ld61ugX3dgsMXdPoj-p466wDGlZtrZgMiMH-aJ9H7FbE/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.
- Challenge 1 - `crypto/rsa-practice`
- Challenge 2 - `crypto/rubiks-cube`
- Challenge 3 - `crypto/prime-factory`
- Challenge 4 - `crypto/rubiks-cube-2`
- Challenge 4 - `crypto/mitm`

## Resources
The following resources are great to practice/learn about the ciphers covered in the slides.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
- [cryptohack](https://cryptohack.org/): A website with many challenges related to cryptography
- [Alpertron](https://www.alpertron.com.ar/ECM.HTM): A fast online integer factorization calculator for large numbers
- [FactorDB](https://factordb.com/): A large online database of integers and their factors
- [DanBoneh](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf): A paper by a Stanford professor on RSA attacks