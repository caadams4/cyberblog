# UDCTF 2023

I created 9 challenges for the CTF. Here are the problems and intended solutions for 2. I may get to the remaining 7 later. Enjoy :)

## 1 of 2: SIMP
This challenge takes a newbie through their first directory brute force, ssh private key theft, and privesc through exploiting a root cronjob (or Pwnkit), and a reverse shell.

![Alt text](image-11.png)

### Recon

(![Alt text](image.png)

Notice two TCP ports, 22 and 8000. 8000 is an alternate http service so lets check it out. 

![Alt text](image-1.png)
Its a webpage... but a placeholder webpage in development. Lets run dirbuster to se eif there's anything interesting in the serving directory.

![Alt text](image-2.png)
Big uh-oh on the devs part, see the `.ssh` directory is accessible (maybe)

### Initial Exploitaiton

Lets use that stolen private ssh key to log in to the web server. 

![Alt text](image-3.png)
On the web page, the email `dave@corpo.com` was present. This may be the account for which the stolen key belongs to. 

![Alt text](image-4.png)
Bingo. There's our initial access.

## SIMP II (continuation of SIMP I)

![image](https://github.com/caadams4/cyberblog/assets/79220528/2a274c57-4821-4ea3-a89e-ae6358eb86c8)


### Privilege Escalation


Now we need to find a way to root.

![Alt text](image-5.png)
On the target machine in dave's home directory, we see a few files. One of which is `send_logs.py`

Notice the file computes the md5 file hash of `/etc/shadow`

ROOT is required to do so. THAT is interesting. AND...

![Alt text](image-6.png)

We're able to edit the `send_logs.py` file. So I want to add a line to the end to create a file called `'cronjob?'` with `whoami` echoed to the contents.

![Alt text](image-7.png)

Add a reverse shell payload to the `send_logs.py` file:

![Alt text](image-8.png)

And we wait... 

![Alt text](image-9.png)

And there it is 

![Alt text](image-10.png)


## 2 of 2: SQL 4 Dummies

An easy SQL injection. The challenge: break into rickjames account.  

![Alt text](image-12.png)

The authentication page:

![Alt text](image-13.png)

Enter some creds to see what happens.

![Alt text](image-14.png)

The username is read back to us. 

![Alt text](image-15.png)

Try to end the sql variable with ' and negate the remaining query with a comment char -- 

![Alt text](image-16.png)

The input was filtered

![Alt text](image-17.png)

Try the same combo of chars inside the same combo of chars

![Alt text](image-18.png)

bingo!

![Alt text](image-19.png)
