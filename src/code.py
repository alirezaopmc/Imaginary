from PIL import Image

COLOR_TO_PIXEL = {
    "WHITE": (255, 255, 255, 255),
    "BLACK": (0, 0, 0, 255),
    "RED": (255, 0, 0, 255),
    "GREEN": (0, 255, 0, 255),
    "BLUE": (0, 0, 255, 255),
}

PIXEL_TO_COLOR = {
    pixel: color for (color, pixel) in COLOR_TO_PIXEL.items()
}


class ImageFecade:
    def __init__(self, path):
        self.im = Image.open(path)

    def load(self):
        self.pixels = self.im.load()

    def color_to_pixel(self, color):
        return COLOR_TO_PIXEL[color]

    def pixel_to_color(self, pixel):
        return PIXEL_TO_COLOR[pixel]

    def get_pixel(self, i, j):
        return self.color_to_bit(self.pixels[i, j])

    def set_pixel(self, i, j, bit):
        self.pixels[i, j] = self.bit_to_color(bit)

    def save(self, path):
        self.im.save(path)


class Maze
