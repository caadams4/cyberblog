# UTCTF

## Summary
An overall good set of challenges; I tried my hand at four but only solved two. I had much success at the network security problems. Even though I didn't finish the forensics, I learned alot. So that's good, I guess.

## CTF Solves 
The second solve is dependent to the first, so I will combine them into one writeup. 

### SMB Infiltration

![listing](smb/smb_problem_listing.png)

* Some background on 445:
Port 445 commonly operates Microsoft's Server Message Block (SMB) protocol. SMB gained infamy after it was exploited with EternalBlue in the devastating ransomeware attack, WannaCry. Read about WannaCry [CVE-2017-0144](https://nvd.nist.gov/vuln/detail/CVE-2017-0144)

After some infomation gathering on SMB, I found there is a smbclient package for Ubuntu. I installed the software with:
```shell
sudo apt-get install smbclient
```

### Recon

For SMB, we need to know the IP address. We run the nslookup to find the IP address that matches the given hostname. 

![nslookup](smb/nslookup.png)

So we know the IP of our target is 44.201.8.3. Now lets run a scan of open ports, just to see what ports the server is listening.

![nmap](smb/nmap%20server.png)

Note the 445, that's SMB! 

After reviewing the smbclient manual, I notice the -L option can be used to scan for shares on a host. So:

![scan](smb/smb%20list%20shares.png)

Now lets connect to a share using smbclient again.

![connect](smb/smb%20connecting.png)

We're in. We can poke around and see what we find. 

![note](smb/download%20note.png)

Check out this note to IT. We cant open and view it here, but we can download it to our machine with 'mget'

Cool. 

![flag](smb/smb%20note%20flag.png)

Here's our first flag...Along with some interesting info in the note. 

Turns out Crystal Ball, Wade Coldwater Jay Walker, Holly Wood, and possibly Arty F all use "abracadabra" as their passwords. Arty F instructs them to append a special char to make it more secure. 

Sounds great Arty. 

This may come in hand in our next challenge.

### SSH Brute Force

![listing_ssh](ssh/utctf_solve.png)

Many servers are administered remotely using ssh, witch listens on port 22. ssh encrypts with a passphrase and, unless you know the passphrase, its totally secure. 

Looking at our nmap scan, we can see ssh is open on our target. 

![nmap2](smb/nmap%20server.png)

Note the information gathered infiltrating the server via SMB. A few users have used the password "abracadabra" and have been instructed to append it with a special character for security.

Crystal Ball, Wade Coldwater, Jay Walker, Holly Wood, and Arty F. are our target users. 

* A buddy in the Bluehens Discord passed some valuable info he found from some OSINT: Usernames are first initial + last name. 

Usernames:              Possible Passwords:
* cball                 * abacadabra! 
* wcoldwater            * abawcadabra@ 
* jwalker               * abacadabra# 
* hwood                 * abacadabra$ 
* artyf                ....and so on... 

We need generate an ssh key for each possible passphrase, for each user, and try to ssh into the target. After each attempt, we'll log the output.

Sounds like a job for a brute force bash script.

![bash](ssh/exploit_script.png)

Initiate the script. 

And here's the output. 

![flagssh](ssh/script_output.png)