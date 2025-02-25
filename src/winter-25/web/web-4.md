# Web 4: XSS, CSP

XSS (Cross-Site Scripting) is a classic web exploit where attackers can inject malicious code into a website. The attacker sends a link to the webpage with the malicious code to the victim. Once the victim visits the link, the attacker's code is executed. XSS is a serious attack, as it can result in stealing the victim's sensitive data like cookies.

CSP (Content Security Policy) is a security measure that prevents attacks like XSS. It does this by restricting the use of scripts, styles, images, etc from different sources.

by Savannah Alanis

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vS8gA-ESgoh4LIDTLx8RM3KVkxxs5UUCRZN-UVJYH4_4npNAFxItjLQFBj6S8IqyP-brWYRt2POk9xb/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges

The following challenges in increasing difficulty are deployed to [platform.lac.ctf](https://platform.lac.tf) to practice the concepts covered in the slides.

- Challenge 1 - `web/mavs-fan`
- Challenge 2 - `web/purell`
- Challenge 3 - `web/california-state-police` (LACTF 2023)

## Resources

The following resources are great tools for sql challenges:

- [CSP Evaluator](https://csp-evaluator.withgoogle.com/): Check the strength of a CSP
- [CSP Bypass Search](https://cspbypass.com/): A tool designed to help ethical hackers bypass restrictive Content Security Policies.
