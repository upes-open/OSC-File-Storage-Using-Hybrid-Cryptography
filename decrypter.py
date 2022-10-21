from cryptography.fernet import Fernet, MultiFernet
from cryptography.hazmat.primitives.ciphers.aead import (AESCCM, AESGCM,
                                                         ChaCha20Poly1305)

import tools


def readEncryptedKeys():
    target_file = open("raw_data/store_in_me.enc", "rb")
    encryptedKeys = b""
    for line in target_file:
        encryptedKeys = encryptedKeys + line
    target_file.close()
    return encryptedKeys


def readEncryptedText(filename):
    source_filename = 'encrypted/' + filename
    file = open(source_filename, 'rb')
    encryptedText = b""
    for line in file:
        encryptedText = encryptedText + line
    file.close()
    return encryptedText


def writePlainText(filename, plainText):
    target_filename = 'files/' + filename
    target_file = open(target_filename, 'wb')
    target_file.write(plainText)
    target_file.close()


def AESAlgo(key):
    f = Fernet(key)
    encryptedKeys = readEncryptedKeys()
    secret_data = f.decrypt(encryptedKeys)
    return secret_data


def AESAlgoRotated(filename, key1, key2):
    f = MultiFernet([Fernet(key1), Fernet(key2)])
    encryptedText = readEncryptedText(filename)
    plainText = f.decrypt(encryptedText)
    writePlainText(filename, plainText)


def ChaChaAlgo(filename, key, nonce):
    aad = b"authenticated but unencrypted data"
    chacha = ChaCha20Poly1305(key)
    encryptedText = readEncryptedText(filename)
    plainText = chacha.decrypt(nonce, encryptedText, aad)
    writePlainText(filename, plainText)


def AESGCMAlgo(filename, key, nonce):
    aad = b"authenticated but unencrypted data"
    aesgcm = AESGCM(key)
    encryptedText = readEncryptedText(filename)
    plainText = aesgcm.decrypt(nonce, encryptedText, aad)
    writePlainText(filename, plainText)


def AESCCMAlgo(filename, key, nonce):
    aad = b"authenticated but unencrypted data"
    aesccm = AESCCM(key)
    encryptedText = readEncryptedText(filename)
    plainText = aesccm.decrypt(nonce, encryptedText, aad)
    writePlainText(filename, plainText)


def decrypter():
    tools.empty_folder('files')
    key_1 = b""
    list_directory = tools.list_dir('key')
    filename = './key/' + list_directory[0]
    public_key = open(filename, "rb")
    for line in public_key:
        key_1 = key_1 + line
    public_key.close()
    secret_information = AESAlgo(key_1)
    list_information = secret_information.split(b':::::')
    key_1_1 = list_information[0]
    key_1_2 = list_information[1]
    key_2 = list_information[2]
    key_3 = list_information[3]
    key_4 = list_information[4]
    nonce12 = list_information[5]
    nonce13 = list_information[6]
    files = sorted(tools.list_dir('encrypted'))
    for index in range(0, len(files)):
        if index % 4 == 0:
            AESAlgoRotated(files[index], key_1_1, key_1_2)
        elif index % 4 == 1:
            ChaChaAlgo(files[index], key_2, nonce12)
        elif index % 4 == 2:
            AESGCMAlgo(files[index], key_3, nonce12)
        else:
            AESCCMAlgo(files[index], key_4, nonce13)
