from Crypto.Cipher import AES
import base64, os

SECRET_KEY = key = b'\xc0\x14\x91\xd8v4\x92\x06\xf2\x0e %\xd7,\x8b\xba'
token = "5nb6IfB+I5PKUdotVh8MJ5kdbryYjB0AI0YSoSIK/Og="
content = "textoparacifrar"

# AES 'pad' byte array to multiple of BLOCK_SIZE bytes
def pad(byte_array):
    BLOCK_SIZE = 16
    pad_len = BLOCK_SIZE - len(byte_array) % BLOCK_SIZE
    return byte_array + (bytes([pad_len]) * pad_len)

# Remove padding at end of byte array
def unpad(byte_array):
    last_byte = byte_array[-1]
    return byte_array[0:-last_byte]

def encryptCBC(message):
    """
    Input String, return base64 encoded encrypted String
    """

    byte_array = message.encode("UTF-8")

    padded = pad(byte_array)

    # generate a random iv and prepend that to the encrypted result.
    # The recipient then needs to unpack the iv and use it.
    iv = os.urandom(AES.block_size)
    cipher = AES.new( SECRET_KEY, AES.MODE_CBC, iv )
    encrypted = cipher.encrypt(padded)
    # Note we PREPEND the unencrypted iv to the encrypted message
    return base64.b64encode(iv+encrypted).decode("UTF-8")

def decryptCBC(message):
    """
    Input encrypted bytes, return decrypted bytes, using iv and key
    """

    byte_array = base64.b64decode(message)

    iv = byte_array[0:16] # extract the 16-byte initialization vector

    messagebytes = byte_array[16:] # encrypted message is the bit after the iv

    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv )

    decrypted_padded = cipher.decrypt(messagebytes)

    decrypted = unpad(decrypted_padded)

    message_content = decrypted.decode("UTF-8")

    return content == message_content

if __name__ == '__main__':
    encryptCBC(message)
    decryptCBC(message)