# Web 5: XSS
by Stewart Kwok

XSS stands for **Cross Site Scripting** and it's a web attack where the attacker injects code to be run on the website. It requires the victim to visit the webpage with the malicious code. There are many techniques for injecting JavaScript code into a webpage. We'll go through **stored**, **reflected**, and **DOM-based XSS** and their common payloads. URLs, form fields, cookies, and HTTP headers are all common injection points. Input sanitization can be used to mitigate these attacks, but there are also ways to **bypass these mitigations**!

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRrAAOBLXED4dRhTRJMcyY30YA603hnSpjNXMoj_s0Sia0oh5hOafiB3iH4f4xGWIDtl3tKINKBI4hy/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following XSS challenges are deployed to [platform.acmcyber.com](https://platform.acmcyber.com)
- Challenge 1 - `web/acm-picks` 
- Challenge 2 - `web/hello-my-name-is`
- Challenge 3 - `web/brainrot-xss`
- Challenge 4 - `web/bananas` 
- Challenge 5 - `web/hptla`
- Challenge 6 - `web/xtra-salty-sardines`

## Resources
The following are resources for different kinds of XSS attacks.
- [List of XSS Payloads](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet): PortSwigger's list of common XSS payloads
- [DOM-based XSS](https://www.invicti.com/learn/dom-based-cross-site-scripting-dom-xss/): Includes common sources and sinks for DOM-based XSS