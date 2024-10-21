# Web 3: Local File Inclusion
by Audrey Emis

The Linux File System has some built in directories that every directory (even seemingly empty ones) have! . represents the current directory and ../ represents the parent directory. Some web apps take file paths as inputs from users, which can lead to sensitive data being uncovered if the user puts in the right input. They can use "../" to get to parent directories, all the wayup to the root directory, where many more files are accessible. This vulnerability is caused by weak input sanitization or other interesting loopholes in the code. Today, we'll learn about LFI and work through some challenges that cover different LFI techniques!

## Slides
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRyZ-0qMoZTTIo1To4MEzs6Rj3PNNhWQyRKakHJfeZkUSiyF_sqz9m01iABEp3W768cxogKg3_ufK6E/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Challenges
We'll be working on the following challenges on [platform.acmcyber.com](https://platform.acmcyber.com)
- Challenge 1 - `web/happy-halloween`
- Challenge 2 - `web/potluck`
- Challenge 3 - `web/book-store`
- Challenge 4 - `web/stealing-favorite-animal-flag`
- Challenge 5 - `web/the-modern-file-explorer-1`
- Challenge 6 - `web/the-modern-file-explorer-2`
- Challenge 7 - `web/the-modern-file-explorer-3`
- Challenge 8 - `web/the-modern-file-explorer-4`
- Challenge 9 - `web/the-modern-file-explorer-5`

## Resources
The following are great resources for learning about LFI, mitigations, and bypasses.
- [Portswigger's Path Traversal Lesson](https://portswigger.net/web-security/file-path-traversal#what-is-path-traversal): Portwigger is a great resource for all kinds of web security. There are explanations and challenges for LFI at this link. 
- [HackTricks File Inclusion/Path Traversal](https://book.hacktricks.xyz/pentesting-web/file-inclusion): Great post that explains common LFI techniques and how to bypass certain mitigations.