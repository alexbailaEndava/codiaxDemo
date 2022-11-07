def getKey():
    key = ""
    hex = open("key.txt", "r").read().split("0x")[1:]

    for unit in hex:
        unit = "0x" + unit

    for unit in hex:
        key = key + chr(int(unit, base=16))
    return key