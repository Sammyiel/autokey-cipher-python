# autokey-cipher-python

Name: 
Email: 

To execute my program, please run the following command:

python auto.py <inputfile> <outputfile> <key> <1/0>

Example encryption: auto.py 1.txt 2.txt 2 1

Example decryption: auto.py 1.txt 2.txt 2 0

1: encryption
0: decryption

My algorithm:

I first check if the input file exists or not. If not, I direct the user. Otherwise, I proceed with encryption/decryption. I allocate indices of the input file, output file, key and action. I first check if the action is 1 or 0. If not, I direct the user. Otherwise, I proceed with the encryption/decryption. I use the ord() and chr() functions to encrypt/decrypt the file. For autokey cipher, I use a for loop to iterate through the input file and add the key and the input file into the output file. After all iterations, I close the input file and the output file.
