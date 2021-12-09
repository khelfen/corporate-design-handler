"""Tests for `corporate_design_handler` package."""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from corporate_design_handler import ColorHandler


class TestColorHandler:

    @classmethod
    def setup_class(cls):
        cls.color_handler = ColorHandler()

    def test_update_colors(self):
        new_colors = {
            "Raw Umber": [111, 78, 12],
            "Summer Sky": [76, 178, 220]
        }

        old_len = len(self.color_handler)

        self.color_handler.update_colors(new_colors)

        for color in new_colors.keys():
            assert color in self.color_handler.colors.keys()

        assert (old_len + len(new_colors)) == len(self.color_handler)

    def test_remove_colors(self):
        rm_colors = ["Raw Umber", "Summer Sky"]

        old_len = len(self.color_handler)

        self.color_handler.remove_colors(rm_colors)

        for color in rm_colors:
            assert color not in self.color_handler.colors.keys()

        assert (old_len - len(rm_colors)) == len(self.color_handler)

    def test_add_color_maps(self):
        new_color_maps = {
            "test": ["san_juan", "crusta", "matisse"]
        }

        old_len = len(self.color_handler.color_maps)

        self.color_handler.add_color_maps(new_color_maps)

        for color_map in new_color_maps.keys():
            assert color_map in self.color_handler.color_maps.keys()

        assert (old_len + len(new_color_maps)) == \
               len(self.color_handler.color_maps)

    def test_remove_color_maps(self):
        rm_color_maps = ["test"]

        old_len = len(self.color_handler.color_maps)

        self.color_handler.remove_color_maps(rm_color_maps)

        for color_map in rm_color_maps:
            assert color_map not in self.color_handler.color_maps.keys()

        assert (old_len - len(rm_color_maps)) == \
               len(self.color_handler.color_maps)

    def test_mpl_listed_colormap(self):
        np.random.seed(1)
        data = np.random.randn(30, 30)
        for color_map in self.color_handler.color_maps.keys():
            cmap = self.color_handler.mpl_listed_colormap(
                color_map=color_map)

            assert isinstance(cmap, ListedColormap)

            fig, ax = plt.subplots()

            psm = ax.pcolormesh(
                data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)

            fig.colorbar(psm, ax=ax)

            plt.close()

    def test_mpl_linear_segmented_color_map(self):
        np.random.seed(1)
        data = np.random.randn(30, 30)
        for color_map in self.color_handler.color_maps.keys():
            cmap = self.color_handler.mpl_linear_segmented_color_map(
                color_map=color_map)

            assert isinstance(cmap, LinearSegmentedColormap)

            fig, ax = plt.subplots()

            psm = ax.pcolormesh(
                data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)

            fig.colorbar(psm, ax=ax)

            plt.close()

