import hashlib
import colorsys

def shift_rgb(rgb, hue_shift):
    h, l, s = colorsys.rgb_to_hls(*rgb)
    h = (h + hue_shift) % 1.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return r, g, b

def string_to_rgb(input_string) -> tuple[float, float, float]:
    hash_object = hashlib.sha256()
    hash_object.update(input_string.encode('utf-8'))
    hash_str = hash_object.hexdigest()

    r = int(hash_str[:2], 16) / 255.0
    g = int(hash_str[2:4], 16) / 255.0
    b = int(hash_str[4:6], 16) / 255.0

    return shift_rgb((r,g,b), 0.9)


