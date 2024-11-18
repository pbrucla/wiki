# Fundamentals 6: Introduction to Cryptography
by Arnav Vora

Cryptography is the process of hiding information or communicating securely in an environment where everyone is trying to read the communication. Most cryptography examples involve Alice and Bob trying to communicate while Eve listens in. Today, we explored the basics of cryptography, starting with the most fundamental **classical ciphers** used before we had powerful computers. However, these ciphers are completely inadequate to hide data in today's age. We learn of ways that computers can break these ciphers, and then move to discussing more modern forms of encryption. A fundamental operation in modern cryptography is **XOR**. This can be used to create the **One-time Pad**, a mathematically *perfectly secure* cipher that reveals no information about the information being sent. However, this cipher isn't practical in most scenarios, and it has many conditions for it to actually achieve perfect security. We then discuss two main classes of *symmetric* ciphers that are widely used: **block ciphers** and **stream ciphers**.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQpdAzBVLMExOGsP8jT2pF3pFxP3hVdx-lWEnawtOpIOcKQQlwb-WiVgell2vz2rZnw8gmJ6isY-fZF/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.
- Challenge 1 - `fundamentals/Caesar turns 47` 
- Challenge 2 - `fundamentals/vigenere is kill`
- Challenge 3 - `fundamentals/XOR practice`
- Challenge 4 - `fundamentals/Practice Run` 
- Challenge 5 - `fundamentals/Practice Run 2`
- Challenge 6 - `fundamentals/bigram`

## Resources
The following resources are great to practice/learn about the ciphers covered in the slides.
- [dcode.fr](https://www.dcode.fr/): This website hosts many classical ciphers, and provides tools for encryption, decryption, and automatic cracking of ciphers. This is a staple for classical cryptography challenges.
- [guballa Substitution Solver](https://www.guballa.de/substitution-solver): My personal favorite website to crack monoalphabetic substitution ciphers.
- [Cyberchef](https://gchq.github.io/CyberChef/): This website also hosts many ciphers, and provides tools for encryption, decryption, and automatic cracking. It is very powerful at detecting the cipher used in encryption if is unknown, and is also a staple for classical cryptography challenges.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.