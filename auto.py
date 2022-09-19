# Importing modules

import sys
import os

# Encrypting/decrypting function
def encrypt(inputfile,outputfile,key,en):
    if not os.path.exists(inputfile):
        print("Input file does not exist!!!")
    else:
        fin=open(inputfile,"r")
        fout=open(outputfile,"w")
        s=fin.readline()
        k=""
        # For encryption
        if en==1:
            for i in range(0,len(s)):
                k=k+chr(((ord(s[i])-97+ord(key[i%len(key)]))%26)+97)
        # For decryption
        else:
            for i in range(0,len(s)):
                k=k+chr(((ord(s[i])-97-ord(key[i%len(key)]))%26)+97)
        fout.write(k)
        fin.close()
        fout.close()

def main():
    # Checking command line arguments if not 5, direct user
    if len(sys.argv)!=5:
        print("Invalid number of arguments")
        print("Usage: auto.py <inputfile> <outputfile> <key> <1/0>")
        print("1: encryption")
        print("0: decryption")
    # If command line arguments are 5, proceed with 1/0
    else:
        inputfile=sys.argv[1]       # Allocating index of the input file
        outputfile=sys.argv[2]       # Allocating index of the output file
        key=sys.argv[3]              # Allocating index of the key
        en=int(sys.argv[4])         # Allocating index of the action (either 1 or 0)
        if en!=1 and en!=0:
            print("Invalid choice of 1/0")
        else:
            encrypt(inputfile,outputfile,key,en)

if __name__=="__main__":
    main()