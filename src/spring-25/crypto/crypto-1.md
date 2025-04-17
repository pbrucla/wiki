# Crypto 1: Intro to Cryptography / Math

by Arnav Vora, Joshua Zhu (revamped for Spring 2025)

Cryptography is the process of hiding information or communicating securely in an environment where everyone is trying to read the communication. Most cryptography examples involve Alice and Bob trying to communicate while Eve listens in. Today, we explored the basics of modern cryptography, including fundamental math used in modern cryptosystems. Specifically, we covered data encoding, the XOR operation, and one-time-pads, used as the most fundamental way to provide information theoretic security. However, this cipher isn't practical in most scenarios, and it has many conditions for it to actually achieve perfect security. We also learned about modular arithmetic that underlies most modern public key cryptosystems.

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ2LxI6MkXZprWbkjSQtdcuPnD1GxHuWDy4Wr4eBu1NjtWq0TmpJZLWeRRzlPIT0-pVMTkeVQfjwV6g/embed?start=false&loop=false&delayms=3000" frameborder="0"width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges

The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.

These challenges are beginner friendly: (tags on the platform: crypto, cyber academy, week 3)

- Challenge 1 - `crypto/XOR Practice`
- Challenge 2 - `crypto/Modular Practice`
- Challenge 3 - `crypto/vigexor`
- Challenge 4 - `crypto/Practice Run`
- Challenge 5 - `crypto/bigram`

These challenges are a bit harder: (can be found under the `upsolving` category under the week tab)

- Challenge 6 - `crypto/chinese-lazy-theorem-1`
- Challenge 7 - `crypto/prime-factory`
- Challenge 8 - `crypto/lunchly-exchange`
- Challenge 9 - `crypto/chinese-lazy-theorem-2`
- Challenge 10 - `crypto/Golden Ticket`
- Challenge 11 - `crypto/mitm`
- Challenge 12 - `crypto/Lazy Lagrange`

## Resources

The following resources are great to practice/learn about the ciphers covered in the slides.

- [dcode.fr](https://www.dcode.fr/): This website hosts many classical ciphers, and provides tools for encryption, decryption, and automatic cracking of ciphers. This is a staple for classical cryptography challenges.
- [Cyberchef](https://gchq.github.io/CyberChef/): This website also hosts many ciphers, and provides tools for encryption, decryption, and automatic cracking. It is very powerful at detecting the cipher used in encryption if is unknown, and is also a staple for classical cryptography challenges.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
- [SageMath](https://www.sagemath.org/): An open-source mathematics system that integrates with Python and is incredibly useful in many cryptography challenges.
