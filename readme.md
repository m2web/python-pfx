# Chat Session Building Certificate Files

This chat session was created Saturday morning, 2023-6-24, in about a half hour time span. Since I have been working with security certs and extracting \*.crt and \*.key files from a *.pfx cert, in bashshell scripts on a Linux system, I thought I will try this in python. 😊

## Create a Script to Make a \*.CRT and \*.KEY Files

Before we can create an \*.pfx file, we need the \*.crt and \*.key files.  The \*.crt file is the public key and the \*.key file is the private key.  The \*.crt file is the file that is shared with the other party.  The \*.key file is the file that is kept secret.

See the makeCRTandKEY.py file for the script to create the \*.crt and \*.key files.

## Create a Script to Make a \*.PFX File

See the createPFX.py file for the script to create the \*.pfx file.

## Create a Script to Extract the \*.CRT and \*.KEY Files

See the makeCRTandKEYfiles.py file for the script to extract the \*.crt and \*.key files from the \*.pfx file.
