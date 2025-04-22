# Crypto 2: Symmetric Cryptography

by Arnav Vora

We will discuss one type of modern cipher that is actually practical to use: symmetric cryptography. Symmetric cryptography uses the same keys for both encryption and decryption. These are many benefits and drawbacks to this form of cryptography. We will discuss the two main forms of symmetric cryptography: block ciphers and stream ciphers. Block ciphers divide plaintext into fixed-size blocks, and encrypt each block separately. These blocks are then combined with a certain _mode of operation_, which can open up more attacks. Stream ciphers are similar to the XOR operation, but instead they use a key to generate a _keystream_ to XOR the plaintext with.

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQmkoZa8puNRzIfz46t8T49igzFn5prmZoA_YEFTTnh8e3Otu1DWVdSe5cy19NI1X3_8o_77oRjEoDF/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges

The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.

These challenges are chosen for this week: (tags on the platform: crypto, cyber academy, week 4)

- Challenge 1 - `crypto/practice-run`
- Challenge 2 - `crypto/extremely-convenient-breaker`
- Challenge 3 - `crypto/convenient-cbc`
- Challenge 4 - `crypto/bigram`
- Challenge 5 - `crypto/admin-login`

## Resources

The following resources are great to practice/learn about the concepts covered in the slides.

- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
- [cryptohack](https://cryptohack.org/): A website with many challenges related to cryptography
- [Modes of Operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) A good article about the different modes of operation of block ciphers.
