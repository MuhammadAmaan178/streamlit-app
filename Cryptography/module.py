codes = {" ":0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
valid_characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
valid_digits_and_spaces = list("0123456789 ")

def is_valid_input(user_input):
    for char in user_input:
        if char not in valid_characters:
            return False
    return True

def check_numeric_input(user_input):
    for char in user_input:
        if char not in valid_digits_and_spaces:
            return False
    return True
def take_string(msg):
    """
    It is used to take string that you want to encode and returns converted list which will multiply to key
    """
    message = []
    # converting the string message into numeric form using above dictionary
    for i in msg:
        temp = codes[i]
        message.append(temp)
    new_msg = []
    # we want to convert the numeric form which is in form of list into 1x2 form
    while len(message) % 2 != 0:
        message.append(0)
    else:
        for i in range(int((len(message))/2)):
            st = i * 2
            end = st + 2
            new_msg.append(message[st:end])
    return new_msg

def key_msg(new_msg,x11,x12,x21,x22):
    """
    this is use to multiply your half-encoded message to key
    """
    result = []
    key = [ [x11, x12],
            [x21, x22]]
        # if the key is inversable, multiplying it with the matrix which is in 1x2 form that we create earlier.
    for m in new_msg:
        x = m[0] * key[0][0] + m[1] * key[1][0]
        result.append(x)
        x = m[0] * key[0][1] + m[1] * key[1][1]
        result.append(x)
    return result

def inverse(key):
    """
    This function use to inverse the given key
    """
    d = (key[0][0]*key[1][1]) - (key[0][1]*key[1][0])
    a,b = key[0]
    c,e = key[1]
    inverse_key = [[round(e/d,4), round(-b/d,4)], [round(-c/d,4), round(a/d,4)]]
    return inverse_key

def inversekey_msg(result,inverse_key):
    """
    This is use to multiply the inverse key with encoded msg
    """
    new_result = []
    for i in range(int((len(result)) / 2)):
        st = i * 2
        end = st + 2
        new_result.append(result[st:end])
    f_result = []
    for m in new_result:
        x = int(round((m[0] * inverse_key[0][0] + m[1] * inverse_key[1][0]), 0))
        f_result.append(x)
        x = int(round((m[0] * inverse_key[0][1] + m[1] * inverse_key[1][1]), 0))
        f_result.append(x)
    return f_result

def decode(f_result):
    """
    This is finally use to decode message
    """
    d_message = ""
    for i in f_result:
        for key, value in codes.items():
            if value == i:
                d_message += key
                break
    return d_message