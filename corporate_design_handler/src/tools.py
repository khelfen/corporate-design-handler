""" This Module provides helper functions. """


def validate_color_map(handler, color_map, reverse=False, return_as="hex"):
    if isinstance(color_map, str):
        color_map = handler.color_maps[color_map]

    if not hasattr(color_map, "__len__"):
        raise ValueError(
            "Please provide color map by name of the color map or as "
            "array like with the color names as values.") from None
    elif not isinstance(color_map, list):
        color_map = list(color_map)

    if return_as == "hex":
        color_map = [
            handler.colors[color].rgb2hex() for color in color_map]
    elif return_as == "dec":
        color_map = [
            handler.colors[color].rgb2dec() for color in color_map]
    else:
        color_map = [
            handler.colors[color] for color in color_map]

    if reverse:
        color_map.reverse()

    return color_map
