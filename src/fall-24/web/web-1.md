# Web 1: Intro to Web & Client-Side Security
by Benson Liu

The internet is one of the most powerful tools that we used today and is deeply integrated into our daily lives. As the history of the web envolved, the security of the internet has changed as well. As we begin our journey into web security, we will start by understanding the basics of the web and how to secure the client-side of web applications. Every page on the internet is composed of **HTML**, **CSS**, and **JavaScript** which is used to display content, add styling, and make the page interactive respectively. Most web apps take on the **client-server model** when desigining their systems and communicate with each other using the **HTTP protocol**. Web clients or frontends are targets for a variety of security vulnerabilities (we will cover these in later weeks) but for now, we will focus on getting familiar with interacting with the client-side of web applications using the **Chrome Developer Tools**, **Document Object Model (DOM) APIs** and more!

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSFHXEvzXqLQJ-uJdJje9UZ0-THwvSkw1RU7xAnPmRjJyUCTi65G9cp49v5F5NXAQOiAZXVP3D2hNRG/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
The following challenges in increasing difficulty are deployed to [platform.acmcyber.com](https://platform.acmcyber.com) to practice the concepts covered in the slides.
- Challenge 1 - `web/control-you` (from angstromctf 2019)
- Challenge 2 - `web/sourcery`
- Challenge 3 - `web/cooking`
- Challenge 4 - `web/acm-netsec`
- Challenge 5 - `web/terms-and-conditions` (from lactf 2024)

## Resources
The follow resources are great to learn more about the topics covered in the slides.
- [Chrome DevTools Documentation](https://developer.chrome.com/docs/devtools): The comprehensive resource for various features of Chrome DevTools. Frequently, the Chrome DevTools Developer Advocacy team will put together blog posts and videos to help show off new features and how to use them.
- [MDN Web Docs: Document Object Model (DOM)](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model): The DOM API has a lot of features that are well documented by MDN. This is a great resource to figure out how to use different features of the DOM API when working on client-side web challenges.
- [How to hack the Chrome Dinosaur game](https://www.tomsguide.com/how-to/how-to-hack-the-chrome-dinosaur-game): A great exercise in understanding why attempting to secure code on the client-side is a losing battle. This article goes through various tricks for how to hack the Chrome Dinosaur game!
