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