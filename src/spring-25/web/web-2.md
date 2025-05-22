# Web 2: JWT

## What is a JWT?
Jason Web Tokens (JWT) are method of user authentication. The server sends a signed JWT to the user's browser, which contains information like user privileges.

There are 3 parts of a JWT token, separated by periods (.), with the format as header.payload.signature
- Header - tells you the algorithm used to sign the token
- Payload -  information connected to the user, such as permissions
- Signature - Proof that the token hasn't been messed with, determined by Algorithm(header.payload, secret)

The components are base64 encoded and not encrypted, so anyone can decipher them

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered.

- `mcqueen-login`
- `dwayne-the-rock-johnson`
- `kidding-around`
- `imagehost`

## Resources
- [jwt.io](https://jwt.io/)
- [Hacktricks JWT](https://hacktricks.boitatech.com.br/pentesting-web/hacking-jwt-json-web-tokens)

## Tips
- Pay attention to the algorithm type, maybe even look up what it does
- If you want to brute force crack the secret, look into hashcat
