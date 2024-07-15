# try block to handle exception
try:
    # taking path of image as a input
    file1 = input(r'Enter path of Image : ')

    # taking Decryption key as input
    key = int(input('Enter Key for Decryption of Image : '))

    print('The path of file : ', file1)
    print('Key for Decryption : ', key)

    # open file for reading purpose
    fi = open(file1, 'rb')

    # storing image data in variable "image"
    image = fi.read()
    fi.close()

    # converting image into byte array to perform Decryption easily on numeric data
    image = bytearray(image)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key

    # opening file for writing purpose
    fi = open(file1, 'wb')

    # writing Decrypted data in image
    fi.write(image)
    fi.close()
    print('Decryption Done...')


except Exception:
    print('Error caught : ', Exception.__name__)
