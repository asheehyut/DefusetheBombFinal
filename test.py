##########################################################################################
# Test file
##########################################################################################
# converts binary to decimal
# int("1111", 2)

##########################################################################################

# serial number
# self._lserial = Label(self, background="black", fg="white", font=("Courier New", 24), text="Serial Number: {serial_number}")
# self._lserial.grid(row=0, column=0, columnspan=2, sticky=W)

##########################################################################################
# generates random serial number
import random

# serial_format = "xx00xxx0"
# serial_number = ""

# for i in serial_format:
#     if i == "x":
#         serial_number += chr(random.randint(97, 122))
#     elif i == "0":
#         serial_number += str(random.randint(1, 9))

# ##########################################################################################
# # list with encrypted words
# # caeser cipher
# encrypted = []
# decrypted = [
#     "horizon",
#     "velvet",
#     "lantern",
#     "orbit",
#     "whisper",
#     "glacier",
#     "compass",
#     "meadow",
#     "ember",
#     "quartz",
#     "harbor",
#     "summit",
#     "echo",
#     "ripple",
#     "mosaic"
# ]

# # encryption algorithm
# for i in range(0, len(decrypted)):
#     word = ""
#     for j in decrypted[i]:
#         ascii_code = (ord(j) + int(serial_number[7])) % 26 + 97
#         word += chr(ascii_code)
#     encrypted.append(word)


##########################################################################################
# wires


##########################################################################################
# keypad

dictionary = {
            "1" : "a",
            "11" : "b",
            "111" : "c"
        }
a = "11"

print(dictionary[a])