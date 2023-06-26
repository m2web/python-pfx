# Chat Session Building Certificate Files

This chat session was created Saturday morning, 2023-6-24, in about a half hour time span. Since I have been working with security certs and extracting \*.crt and \*.key files from a *.pfx cert, in bashshell scripts on a Linux system, I thought I will try this in python. 😊

To see the Copilot Chat's session and see the steps, import the chat-session.json file into Copilot Chat via `Ctrl+Shift+P | Chat: Import Session...` or by choosing `View > Command Palette | Chat: Import Session...`

## Create a Script to Make a \*.CRT and \*.KEY Files

Before we can create an \*.pfx file, we need the \*.crt and \*.key files. I typically am handed a \*.pfx file from which I need to extract the \*.crt and \*.key files so this step is not normally necessary. However, to create a test \*.pfx file, I will need to generate them here.

The \*.crt file is the public key and the \*.key file is the private key.  The \*.crt file is the file that is shared with the other party.  The \*.key file is the file that is kept secret.

With Copilot Chat's help, here is the makeCRTandKEYfiles.py file:

```python
import OpenSSL.crypto as crypto
import os

def create_certificate_and_key(cert_file_path, key_file_path):
    # Generate a new private key
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Create a new certificate
    cert = crypto.X509()
    cert.get_subject().CN = 'm2.fyi'
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(315360000)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    # Write the certificate and private key to files
    cert_data = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
    key_data = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)
    with open(cert_file_path, 'wb') as f:
        f.write(cert_data)
    with open(key_file_path, 'wb') as f:
        f.write(key_data)

    print(f'Certificate and private key files created: {cert_file_path}, {key_file_path}')

# Save the certificate and private key to the current directory
create_certificate_and_key('./cert.crt', './cert.key')
```

## Create a Script to Make a \*.PFX File

Now that we have our \*.crt and \*.key files, with Copilot Chat's help, here is the createPFX.py script to create a \*.pfx file.

```python
import OpenSSL.crypto as crypto
import os

def create_pfx_certificate(cert_file_path, key_file_path, password):
    # Load the certificate and private key
    with open(cert_file_path, 'rb') as f:
        cert_data = f.read()
    with open(key_file_path, 'rb') as f:
        key_data = f.read()
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)
    key = crypto.load_privatekey(crypto.FILETYPE_PEM, key_data)

    # Create a PKCS12 container
    pfx = crypto.PKCS12()
    # include the certificate
    pfx.set_certificate(cert)
    # include the private key
    pfx.set_privatekey(key)
    # encode as bytes
    pswdBytes = password.encode('utf-8')
    # export as PKCS12
    pfx_data = pfx.export(pswdBytes)

    # Write the PKCS12 container to a file
    pfx_file_path = os.path.splitext(cert_file_path)[0] + '.pfx'
    with open(pfx_file_path, 'wb') as f:
        f.write(pfx_data)

    print(f'PKCS12 container file created: {pfx_file_path}')

# Use the certificate and private key files in the current directory
create_pfx_certificate('./cert.crt', './cert.key', 'password123')
```

## Create a Script to Extract the \*.CRT and \*.KEY Files

Here is the getCRTandKEYfromPFX.py file for the script to extract the \*.crt and \*.key files from the \*.pfx file.

```python
import OpenSSL.crypto as crypto
import os

def get_crt_and_key(pfx_file_path, password):
    # Load the PFX file
    with open(pfx_file_path, 'rb') as f:
        pfx_data = f.read()
    pfx = crypto.load_pkcs12(pfx_data, password)

    # Extract the certificate and private key
    cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pfx.get_certificate())
    key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pfx.get_privatekey())

    # Write the certificate and private key to files
    cert_file_path = os.path.splitext(pfx_file_path)[0] + '.crt'
    key_file_path = os.path.splitext(pfx_file_path)[0] + '.key'
    with open(cert_file_path, 'wb') as f:
        f.write(cert)
    with open(key_file_path, 'wb') as f:
        f.write(key)

    print(f'Certificate and private key files created: {cert_file_path}, {key_file_path}')

# Example usage
get_crt_and_key('./cert.pfx', 'password123')
```

Again, to see the Copilot Chat's session content, import the chat-session.json file into Copilot Chat via `Ctrl+Shift+P | Chat: Import Session...` or by choosing `View > Command Palette | Chat: Import Session...`
