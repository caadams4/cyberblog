bytes_of_interest = [0x14,0x17,0x12,0x1d,0x50,0x46,0x5d,0x42,0x41,0x6c,0x33,0x5d,0x5a,0x0e,0x3a,0x6a,0x41,0x40,0x57,0x08,0x34,0x3c,0x0b,0x03,0x34,0x28,0x46,0x5f,0x53,0x10,0x50]
print(bytes_of_interest)

result = 0x36^0x41
flag = ""
flag += chr(result)

for i in range(0,len(bytes_of_interest)):
    result = result ^ bytes_of_interest[i]
    flag+=chr(result)
    
print(flag)