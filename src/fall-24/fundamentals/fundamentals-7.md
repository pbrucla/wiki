# Fundamentals 6: Model Cryptography Basics
by Rathul Anand

Cryptography is the process of hiding information or communicating securely in an environment where everyone is trying to read the communication. Most cryptography examples involve Alice and Bob trying to communicate while Eve listens in. Today, we explore **modern cryptography**, heavily rooted in modular arithmetic. Modular arihmetic the language underlying modern cryptosystems. Many cryptographic alogirhtms rely on this arithmetic, where numbers "wrap around" after reaching a certain modulus. For example, the Diffie-Hellman Key Exchange (DHKE), which we covered today, leverages modular exponentiation to enable two parties to share a secret over an insecure channel. By applying modular arithmetic, both parties can compute the same shared secret without revealing or sharing their private keys. This principle forms the basis for secure communication in many asymmetric encryption schemes. We also cover the RSA cryptosystem, what it is, what calculations are needed, and a short proof on why it works.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQpiJdlth-5JiFFPiHwu3GF6jzwhqtmFITBsPKou0CcNRqw8UpKm0Q8zH-7Pz8eYeHKVSJlTb_xv22Y/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides. We recommend working in the order below, as the challenges build upon themselves.
- Challenge 1 - `fundamentals/Modular Practice`
- Challenge 2 - `fundamentals/rubiks-cube`
- Challenge 3 - `fundamentals/prime-factory`
- Challenge 4 - `fundamentals/RSA Practice`
- Challenge 5 - `fundamentals/lunchly-exchange`

## Resources
The following resources are great to practice/learn about the ciphers covered in the slides.
- [dcode.fr](https://www.dcode.fr/): This website hosts many classical ciphers, and provides tools for encryption, decryption, and automatic cracking of ciphers. This is a staple for classical cryptography challenges.
- [Alpertron](https://www.alpertron.com.ar/ECM.HTM): A fast online integer factorization calculator for large numbers
- [FactorDB](https://factordb.com/): A large online database of integers and their factors.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
- [cryptohack](https://cryptohack.org/): A website with many challenges related to cryptography.
- [Cyberchef](https://gchq.github.io/CyberChef/): This website also hosts many ciphers, and provides tools for encryption, decryption, and automatic cracking. It is very powerful at detecting the cipher used in encryption if is unknown, and is also a staple for classical cryptography challenges.