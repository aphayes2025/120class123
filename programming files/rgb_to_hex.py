# rgb to hex function
def rgb_to_hex(r, g, b):
    # red
    r = max(0, min(255, r))
    # green
    g = max(0, min(255, g))
    # blue
    b = max(0, min(255, b))
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
