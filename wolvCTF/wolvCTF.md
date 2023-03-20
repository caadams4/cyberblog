# UTCTF 2023

UNDER CONSTRUCTION

## Summary
A great set of challenges. I didn't have much time this weekend, so I tried my hand at one reverse engineer problem and successfully solved the problem.

## 1. Homework Help

* PICTURE HERE

The challenge includes one binary file. Lets download it and open it up with Ghidra. 

* If you're not familiar with Ghidra, it's a sick NSA tool used to decompile binaries

GHIDRA LINK GITHUB

GHIDRA REVERSE



Now that we have a picture of what is happening within the file, let's run it through the radare2 (r2) debugger and watch it in execution. 

RADARE2 LINK GITHUB

Let's start the binary using r2 and set a breakpoint at the flag xor loop in __stack_chk_fail. 

PICTURE BREAKPOINT

Ok, when it asks for input, we're going to send the line, 'wctf{}'. Why? Well this is WolvCTF and the flag format begins with 'wctf{', thus we can safely assume the decryptor will successfully process the first 5 characters and fail on the 6th. We can watch the first 5 characters run through the flag verification loop to verify our what we know. 

Continue the program, enter 'wctf{}'

Each screenshot is taken when the instruction pointer is on the character verification XOR

SCREENSHOTS HERE

DESCRIPTION HERE

Take a look at this line:


* Note XOR bit operation is denoted by '^', so XORing 1 and 1 would look like: 1 ^ 1  

Note this portion of memory, these are what the program suspects will be the result of continued chain of XORs against the flag characters. Lets make a list of them so we can build a script to perform the XOR chain. 

'''python3
here here
'''

We must write a script to compute the first XOR, 0x41 ^ 0x36, which resolves to 'w', then XOR the result with the first element of our list above ^^ , then XOR that result with the next element, ... and so on....

* 0x41 ^ 0x36 == 0x57 == 'w'
                  /
      ------------
    /
* 0x57 ^ 0x14 == 0x63 == 'c'
                  /
      ------------
    /
* result ^ next arr[i] == next char
                  /
      ------------
    /
* and so on...

We can write a python3 script to solve:

'''python3
here here
'''

Beautiful,

OUTPUT HERE







