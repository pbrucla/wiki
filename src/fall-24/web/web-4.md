# Web 4: Advanced Local File Inclusion
by Ronak Badhe

Last week, we covered why local file inclusion is possible and some basic LFI techniques. This week, we'll dive into more **advanced techniques** that can be used to bypass certain mitigations. Oftentimes, different languages have different quirks when handling file paths. Unintuitive behavior is the basis for security vulnerabilities. There are special linux files that contain more information for exploitation, like **/proc/self** and **/dev/fd**. When coming up with LFI exploits, you should research the app's language/framework (especially if the framework is not super common or "normal") and do a lot of experimenting! We'll work through some advanced LFI challenges today and learn about various strange behaviors in web apps.

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT6rd0lWABMRVvKHxioYUDnHHdUThuA6Goa4TieRlsLUO0uPqqq2KMZcSpWNQ695vnZRJgjh1j6-9fy/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" style="aspect-ratio: 16 / 10;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
We'll be continuting on challenges from last week along with two new challenges, all deployed on [platform.acmcyber.com](https://platform.acmcyber.com)
- Challenge 1 - `web/happy-halloween`
- Challenge 2 - `web/potluck`
- Challenge 3 - `web/book-store`
- Challenge 4 - `web/stealing-favorite-animal-flag`
- Challenge 5 - `web/the-modern-file-explorer-1`
- Challenge 6 - `web/the-modern-file-explorer-2`
- Challenge 7 - `web/the-modern-file-explorer-3`
- Challenge 8 - `web/the-modern-file-explorer-4`
- Challenge 9 - `web/the-modern-file-explorer-5`
- NEW Challenge 10 - `web/nginkoid`
- NEW Challenge 11 - `web/buns`

## Resources
The following resources cover various techniques for advanced local file inclusion.
- [Portswigger's Path Traversal Lesson](https://portswigger.net/web-security/file-path-traversal#what-is-path-traversal): Portwigger is a great resource for all kinds of web security. There are explanations and challenges for LFI at this link. 
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion): Contains lots of payloads for different LFI techniques and tricks. 
- [HackTricks File Inclusion/Path Traversal](https://book.hacktricks.xyz/pentesting-web/file-inclusion): Great post that explains common LFI techniques and how to bypass certain mitigations.
