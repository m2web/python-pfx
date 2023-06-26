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