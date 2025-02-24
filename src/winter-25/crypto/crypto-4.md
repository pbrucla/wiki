# Crypto 4: Signatures, Symmetric Cryptography

by Arnav Vora

We will cover signature schemes based on RSA. These use the same underlying cryptosystem, but serve a very different purpose: instead of hiding data, they are used to prove that you are the one sending the message, and nobody is impersonating you. This is crucial in modern web communication, forming the foundation of the TLS (transport layer security) protocol. Then, we will discuss symmetric cryptography. Instead of asymmetric cryptography, where different keys are used for encryption and decryption, symmetric cryptography uses the same keys for both. These are many benefits and drawbacks to this form of cryptography. We will discuss the two main forms of symmetric cryptography: block ciphers and stream ciphers.

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSJ7WI7rHPi1TIX6IfGdS3vESMGbbQEvG4YsJMayW1dZY1CjVFiO_PmSC83QfUOTx81iR5ZSXA3jNNr/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges

The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.

- Challenge 1 - `crypto/extremely-convenient-breaker`
- Challenge 2 - `crypto/practice-run-2`
- Challenge 3 - `crypto/forgeme`
- Challenge 4 - `crypto/bigram`

## Resources

The following resources are great to practice/learn about the concepts covered in the slides.

- [SageMath](https://www.sagemath.org/): An open-source mathematics system that integrates with Python and is incredibly useful in many cryptography challenges.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
- [cryptohack](https://cryptohack.org/): A website with many challenges related to cryptography
- [Modes of Operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) A good article about the different modes of operation of block ciphers.
