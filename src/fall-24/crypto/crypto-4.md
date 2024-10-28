# Crypto 4: Math for Crypto, DHKE
by Rathul Anand

Modular arihmetic is an important language underlying modern cryptosystems. Many cryptographic alogirhtms rely on this arithmetic, where numbers "wrap around" after reaching a certain modulus. For example, the Diffie-Hellman Key Exchange (DHKE), which we cover in these slides, leverages modular exponentiation to enable tow parties to share a secret over an insecure channel. By applying modular arithmetic, both parties can compute the same shared secret without revealing or sharing their private keys. This principle forms the basis for secure communication in many asymmetric encryption schemes.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRnxf9JzdfPeg2SLs_UWlM_Xyhn2yMN-8iciuRShvggYsWa1eQlR0YiLcGCmyJLaP4PYT6YsE40tsb6/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.
- Challenge 1 - `crypto/chinese-lazy-theorem-1`
- Challenge 2 - `crypto/modular-practice`
- Challenge 3 - `crypto/lunchly-exchange`
- Challenge 4 - `crypto/chinese-lazy-theorem-2`
- Challenge 5 - `crypto/golden-ticket`
- Challenge 6 - `crypto/lazy-lagrange`

## Resources
The follow resources are great to practice/learn about the ciphers covered in the slides.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
- [alperton](https://www.alpertron.com.ar/DILOG.HTM): Has a discrete logarithm solver that works fast for small `n`.
- [SageMath](https://www.sagemath.org/): An open-source mathematical software tool. Works with Python and has many constructs that are very useful in modular arithmetic/cryptography.