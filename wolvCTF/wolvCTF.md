# UTCTF 2023

## Summary
A great set of challenges. I didn't have much time this weekend, so I tried my hand at one reverse engineer problem and successfully solved the problem.

## 1. Homework Help

* PICTURE HERE

The challenge includes one binary file and is reminiscent of an old linscence key crack. Lets download and examine with Ghidra. 

* If you're not familiar with Ghidra, it's a sick NSA tool used to decompile binaries. [Check it out on Github](https://github.com/NationalSecurityAgency/ghidra)

### Examine the code


Now that we have a picture of what is happening within the file, let's run it through the [radare2 (r2)](https://github.com/radareorg/radare2) debugger and watch it in execution. 

Let's start the binary using r2 and set a breakpoint at the flag xor loop in __stack_chk_fail. 

Ok, when it asks for input, we're going to send the line, 'wctf{}'. Why? Well this is WolvCTF and the flag format begins with 'wctf{', thus we can safely assume the decryptor will successfully process the first 5 characters and fail on the 6th. We can watch the first 5 characters run through the flag verification loop to verify our what we know. 

Continue the program, enter 'wctf{}'

Each screenshot is taken when the instruction pointer is on the character verification XOR

SCREENSHOTS HERE

DESCRIPTION HERE










Note this portion of memory; these values are what the program suspects will be the result of continued chain of XORs against the flag characters. Lets make a list of them so we can build a script to perform the XOR chain. 

'''python3
bytes_of_interest = [0x14,0x17,0x12,0x1d,0x50,0x46,0x5d,0x42,0x41,0x6c,0x33,0x5d,0x5a,0x0e,0x3a,0x6a,0x41,0x40,0x57,0x08,0x34,0x3c,0x0b,0x03,0x34,0x28,0x46,0x5f,0x53,0x10,0x50]
'''

We must write a script to compute the first XOR, 0x41 ^ 0x36, which resolves to 'w', then XOR the result with the first element of our list above ^^ , then XOR that result with the second element, ... and so on....

Which will look like:
* 0x41 ^ 0x36  == result1
* result1 ^ next arr[i] == result2
* result2 ^ next arr[i+1] == result3
* result3 ^ next arr[i+2] == result4
* and so on...

* 0x41 ^ 0x36 == 0x57 == 'w'
* 0x57 ^ 0x14 == 0x63 == 'c'
* 0x63 ^ 0x17 == 0x74 == 't'
* 0x74 ^ 0x12 == 0x66 == 'f'
* and so on...

We can write a python3 script to solve:

'''python
bytes_of_interest = [0x14,0x17,0x12,0x1d,0x50,0x46,0x5d,0x42,0x41,0x6c,0x33,0x5d,0x5a,0x0e,0x3a,0x6a,0x41,0x40,0x57,0x08,0x34,0x3c,0x0b,0x03,0x34,0x28,0x46,0x5f,0x53,0x10,0x50]
print(bytes_of_interest)

result = 0x36^0x41
flag = ""
flag += chr(result)

for i in range(0,len(bytes_of_interest)):
    result = result ^ bytes_of_interest[i]
    flag+=chr(result)
    
print(flag)
'''

Beautiful,

![flag](./solve_output.png)






