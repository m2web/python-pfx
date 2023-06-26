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