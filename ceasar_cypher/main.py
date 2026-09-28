alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

def decode(alphabet, message, offset):
    decoded_message = ""

    for char in message:
        if char in alphabet:
            #find current index
            current_index = alphabet.index(char)
            #move n offset with modulo operator
            new_index = (current_index + offset) % len(alphabet)
            # add the decodified letter
            decoded_message += alphabet[new_index]
        else:
            decoded_message += char
    return decoded_message

encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
decoded = decode(alphabet, encoded_message, 10)
print(decoded)

def encode(alphabet, message, offset):
    encoded_message = ""

    for char in message:
        if char in alphabet:
            current_index = alphabet.index(char)
            new_index = (current_index - offset) % len(alphabet)
            encoded_message += alphabet[new_index]
        else:
            encoded_message += char
    return encoded_message


my_reply = "hello! yes i decoded it, that was super cool!"

encoded_reply = encode(alphabet, my_reply, 10)
print(encoded_reply)


def vigenere_decode(message, keyword):
    decoded_message = ""
    keyword_index = 0

    for char in message:
        if char in alphabet:

            message_idx = alphabet.index(char)


            key_char = keyword[keyword_index % len(keyword)]
            key_idx = alphabet.index(key_char)


            new_idx = (message_idx + key_idx) % len(alphabet)
            decoded_message += alphabet[new_idx]


            keyword_index += 1
        else:

            decoded_message += char

    return decoded_message



encoded_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"

decoded_text = vigenere_decode(encoded_message, keyword)
print(decoded_text)