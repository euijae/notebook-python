
def defang_ip_address(address):
    result = ''

    for i in range(len(address)):
        char = address[i]

        result += '[.]' if (char == '.') else char

    return result


def defang_ip_address2(address):
    return "[.]".join(address.split("."))


print(defang_ip_address("1.1.1.1"))
