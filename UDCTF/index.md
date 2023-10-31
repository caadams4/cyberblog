# UDCTF 2023

I created 3 challenges for the CTF. Here are the problems and intended solutions. Enjoy :)

## 1 of 3: SIMP
This challenge takes a newbie through their first directory brute force, ssh private key theft, and privesc through exploiting a root cronjob (or Pwnkit), and a reverse shell.

### 1. Recon

(![Alt text](image.png)

Notice two TCP ports, 22 and 8000. 8000 is an alternate http service so lets check it out. 

![Alt text](image-1.png)
Its a webpage... but a placeholder webpage in development. Lets run dirbuster to se eif there's anything interesting in the serving directory.

![Alt text](image-2.png)
Big uh-oh on the devs part, see the .ssh directory is accessible (maybe)

### Initial Exploitaiton

Lets use that stolen private ssh key to log in to the web server. 

![Alt text](image-3.png)
On the web page, the email dave@corpo.com was present. This may be the account for which the stolen key belongs to. 

![Alt text](image-4.png)
Bingo. There's our initial access.

### Priviledge Escalation

Now we need to find a way to root.

![Alt text](image-5.png)
On the target machine in dave's home directory, we see a few files. One of which is `send_logs.py`

Notice the file computes the md5 file hash of `/etc/shadow`

ROOT is required to do so. THAT is interesting. AND...

![Alt text](image-6.png)

We're able to edit the send_logs.py file. So I want to add a line to the end to create a file called 'cronjob?' with whoami echoed to the contents.

![Alt text](image-7.png)

Add a reverse shell payload to the send_logs.py file:

![Alt text](image-8.png)

And we wait... 

![Alt text](image-9.png)

And there it is 

![Alt text](image-10.png)


## 2 of 4: SQL 4 Dummies





