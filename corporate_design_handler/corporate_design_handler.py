"""Main module."""
import matplotlib.pyplot as plt

from copy import copy, deepcopy
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from corporate_design_handler.config.config import settings
from corporate_design_handler.src.data_classes import Color
from corporate_design_handler.src.tools import validate_color_map


# TODO:
#  logging with loguru https://pypi.org/project/loguru/
#  docstrings
#  pytests
#  type checking
#  flake8, black


class ColorHandler:
    """ ColorHandler Class """
    def __init__(self, colors=None, color_maps=None):
        """

        """
        if colors is None:
            colors = dict(settings.colors)
        if color_maps is None:
            color_maps = dict(settings.color_maps)

        self.colors = colors
        self.color_maps = color_maps

    @property
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, colors):
        """
        """
        try:
            self._colors = {
                name: Color(red=red, green=green, blue=blue)
                for name, (red, green, blue) in colors.items()}

        except ValueError:
            raise ValueError(
                "Colors must be given as a dictionary with the color name as "
                "dict key and the RGB values as list as dict value.") from None

    def update_colors(self, new_colors):
        colors = self.colors
        colors.update(new_colors)

        self.colors = colors

    def remove_colors(self, rm_colors):
        if isinstance(rm_colors, str):
            del self.colors[rm_colors]
        elif hasattr(rm_colors, "__len__"):
            for key in rm_colors:
                del self.colors[key]
        else:
            raise ValueError(
                "Provide colors to remove either in form of a list with the "
                "keys you want to remove or in the case of a single color as "
                "string.") from None

    @property
    def color_maps(self):
        return self._color_maps

    @color_maps.setter
    def color_maps(self, color_maps):
        if not isinstance(color_maps, dict):
            color_maps = dict(color_maps)

        color_keys = self.colors.keys()

        for key, values in color_maps.items():
            if not all(val in color_keys for val in values):

                values_not_in_keys = [
                    val for val in values if val not in color_keys]

                raise ValueError(
                    "Not all color names are represented within the given "
                    "colors. Make sure the given color maps only include "
                    "colors which are represented. The following colors in "
                    f"color map {key} are not within the colors: "
                    f"{values_not_in_keys}") from None

        self._color_maps = color_maps

    def add_color_maps(self, new_color_maps):
        color_maps = self.color_maps
        color_maps.update(new_color_maps)

        self.color_maps = color_maps

    def remove_color_maps(self, rm_color_maps):
        if isinstance(rm_color_maps, str):
            del self.color_maps[rm_color_maps]
        elif hasattr(rm_color_maps, "__len__"):
            for key in rm_color_maps:
                del self.color_maps[key]
        else:
            raise ValueError(
                "Provide color maps to remove either in form of a list with "
                "the keys you want to remove or in the case of a single color "
                "map as string.") from None

    def mpl_listed_colormap(
        self, color_map="blues", reverse=False, n_colors=None, **kwargs):
        color_map = validate_color_map(
            self, color_map, reverse=reverse)

        if n_colors is None:
            n_colors = len(color_map)
        elif not isinstance(n_colors, int):
            try:
                n_colors = int(n_colors)
            except ValueError:
                raise ValueError(
                    "Please provide the total number of colors as integer."
                ) from None

        return ListedColormap(
            color_map, N=n_colors)

    def mpl_linear_segmented_color_map(
        self, color_map="green_to_orange", reverse=False,
        distribution="uniform", cvals=None, cmap_name="", **kwargs):
        color_map = validate_color_map(
            self, color_map, reverse=reverse)

        if distribution == "custom":
            # https://stackoverflow.com/a/46778420/13491957
            if cvals is None:
                raise ValueError(
                    "Please provide the variable 'cvals' if the distribution "
                    "is set to custom.") from None
            elif len(cvals) != len(color_map):
                raise ValueError(
                    "Please provide a matching number of values that "
                    "correspond to the colors of your color map. The given "
                    f"number of values is {len(cvals)} while the number of "
                    f"colors is {len(color_map)}.") from None

            norm = plt.Normalize(min(cvals), max(cvals))

            color_map = list(zip(map(norm, cvals), color_map))

        return LinearSegmentedColormap.from_list(
            name=cmap_name, colors=color_map, **kwargs)

    def copy(self, deep=True):
        """Return a copy of the color handler."""
        return self.__copy__(deep=deep)

    def __copy__(self, deep=True):
        if deep:
            return deepcopy(self)
        return copy(self)

    def __len__(self):
        return len(self.colors)

    def __str__(self):
        return (f"{self.__class__.__name__}({len(self.colors)} colors, "
                f"{len(self.color_maps)} color maps)")

    def __repr__(self):
        message = str(self)

        if len(self.colors) + len(self.color_maps) > 0:
            message += "\n"

        if len(self.colors) > 0:
            message += "Colors:\n"
            for name, color in self.colors.items():
                message += (name + ": " + str(color) + "\n")

        if len(self.color_maps) > 0:
            message += "Color Maps:\n"
            for name, color_map in self.color_maps.items():
                message += (name + ": " + str(color_map) + "\n")

        return message

if __name__ == "__main__":
    ColorHandler()
