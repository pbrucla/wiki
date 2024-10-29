# Crypto 2: Stream Ciphers
by Arnav Vora

For perfect security, OTP has very restrictive conditions. Instead, we want to design ciphers that need a smaller key and are easy to work with. Symmetric encryption is when the same key is used for encryption and decryption, and there are two types of commonly-used ciphers. Stream ciphers generate a "keystream" similar to OTP's key, but instead from a single fixed-size key. On the other hand, block ciphers divide up the ciphertext into "blocks" and apply an encryption function to each block using the key. There are many standard commonly-used stream and block ciphers.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRTZaUXtOsoMrXfY19j7Ka3PBpFXJ5DUciWa5I9kxugYSU7qUq19fuk15qIm2Oi2p3Ik21yntyezu7-/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.
- Challenge 1 - `crypto/practice-run-2`
- Challenge 2 - `crypto/count-the-counter`

## Resources
The follow resources are great to practice/learn about the ciphers covered in the slides.
- [pycryptodome](https://pypi.org/project/pycryptodome/): A library that implements many modern-day cryptographic algorithms.
