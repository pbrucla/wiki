# frognebulasolver

This is code we used for the Frog Nebula challenge in the BuckeyeCTF 2022 competition. The challenge involved lots of back and forth communication between the user and their server, so we made use of pwntools to help facilitate this in our Python script.

Let's look at a few relevant lines:

```
(2) from pwn import *
```

This is generally how you will be importing pwntools.

```
(42) self.conn = remote('pwn.chall.pwnoh.io', 13380)
```

This establishes the connection to the challenge address at port 13380. The connection is a "remote" object, which we store in a class variable, since we'll be using it a lot.

```
(43) self.flag = tuple([int(i) for i in self.conn.recvline().decode().strip().split(' ')])
```

The server would send us the coordinates of the flag location, so we would want to store those numbers in a variable. self.conn is our remote connection. The .recvline() command receives one line of input from the connection in binary. The .decode() command turns that received line into standard format. The rest is just string manipulation to get what we want.
