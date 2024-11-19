# Web 6: XSS Revisited
by Stewart Kwok

Cross-Site Scripting (XSS) is a web vulnerability that allows attackers to inject malicious scripts into websites, which are then executed in a victim's browser. This type of attack can lead to the theft of **sensitive data** such as **cookies** or **session tokens**, and is a significant threat to web security.

Today, we explored various methods of injecting JavaScript, including the use of `<script>` tags and **event attributes**. We also covered how attackers simulate victim interactions with **admin bots** to steal sensitive data like **cookies** or **flags**. We discussed advanced exploitation techniques, such as the **double-fetch trick**, to bypass **HTTPOnly cookie protections**. Finally, we examined defenses like **input sanitization** and the challenges of bypassing these security measures.


## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSX46Wtn2ptm1VMnHwigF6pgzvsHs_Q9lhuQZbJgGeyXk3I48_Ri903U61fS5dsw4hExYNeIQ1ThxL2/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

https://docs.google.com/presentation/d/1FO3Nu12UK33MRSysP8kWndCW7t_98JaCJj-VbiHq55s/edit#slide=id.g2f8929da001_0_0

## Challenges
The following XSS challenges are deployed to [platform.acmcyber.com](https://platform.acmcyber.com)
- Challenge 1 - `web/homework`
- Challenge 2 - `web/among-us`
- Challenge 3 - `web/among-us-extra-sus`
- Challenge 4 - `web/hello-my-name-is`
- Challenge 5 - `web/acm-picks`
- Challenge 6 - `web/xtra-salty-sardines`
- Challenge 7 - `web/brainrot-xss`
- Challenge 8 - `web/hptla`

## Resources
The following are resources for different kinds of XSS attacks.
- [Portswigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet): PortSwigger's list of common XSS payloads
- [PayloadsAllTheThings XSS Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection): PayloadsAllTheThings' list of common XSS payloads
- [OWASP Filter Evasion Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html): OWASP's list of payloads for XSS filter evasion
