from collections import namedtuple
from corporate_design_handler.config.config import settings


RGB = namedtuple(
    "RGB", "red, green, blue")


class Color(RGB):
    """
    """
    def __init__(self, **kwargs):
        self.min_rgb_value = settings.color_class.min_rgb_value
        self.max_rgb_value = settings.color_class.max_rgb_value

        assert all(
            isinstance(val, int) for val in self), (
            "RGB values must be integers.")

        assert all(
            self.min_rgb_value <= val <= self.max_rgb_value
            for val in self), (
            f"RGB values must lay between {self.min_rgb_value} "
            f"and {self.max_rgb_value}.")

    def rgb2hex(self):
        """
        """
        return "#%02x%02x%02x" % self

    def rgb2dec(self):
        """
        """
        return tuple(
            color / self.max_rgb_value for color in self)
