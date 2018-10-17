Run with command
```
python rsa.py
```

Run with option `-d` for debug mode (displaying generated public key, secret key, etc.) 
```
python rsa.py -d
```

### NOTE:
*Limitation*:

    - Currently the program only work for small N (20 bits). 
    - Small size of input (3 characters) since N is small.

To do the exponentiation in encryption mode, the input text message to be encrypt will be transformed into numerical representation then this numeric value will be used as inputencryption. 
After decryption, the same numerical representation will be recovered

*Example input*
```
Enter prime p = 1009
Enter prime q = 1017
-------Generating key------------------
Public key (e, N) =  65537 1026153
-------Enter your message = HEY
726989
Numerical representation of your message =  726989
-------Encrypting------------------ Cipher text =  443468
-------Decrypting------------------
De-Cipher text =  726989
```
