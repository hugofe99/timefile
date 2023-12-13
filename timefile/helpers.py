import hashlib
import colorsys
from typing import Any


def shift_rgb(rgb, hue_shift):
    h, l, s = colorsys.rgb_to_hls(*rgb)
    h = (h + hue_shift) % 1.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return r, g, b


def string_to_rgb(input_string):
    hash_object = hashlib.sha256()
    hash_object.update(input_string.encode("utf-8"))
    hash_str = hash_object.hexdigest()

    r = int(hash_str[:2], 16) / 255.0
    g = int(hash_str[2:4], 16) / 255.0
    b = int(hash_str[4:6], 16) / 255.0

    return shift_rgb((r, g, b), 0.9)


def has_len(obj) -> bool:
    return hasattr(obj, "__len__") and callable(getattr(obj, "__len__"))


def has_str(obj) -> bool:
    return hasattr(obj, "__str__") and callable(getattr(obj, "__str__"))


def filter_obj(obj) -> int | float | str:
    if isinstance(obj, (int, float, str)):
        return obj
    elif has_len(obj):
        return len(obj)
    elif has_str(obj):
        return str(obj)
    else:
        return str(type(obj).__name__)


def filter_kwargs(kwargs: dict):
    return {key: filter_obj(value) for key, value in kwargs.items()}
