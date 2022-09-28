from PIL import Image

class ImageFecade:
    def __init__(self, path):
        self.im = Image.open(path)
    
    def load(self):
        self.pixels = self.im.load()

    def color_to_bit(self, color):
        return {
            (0, 0, 0): 0,
            (255, 255, 255): 1
        }[color]

    def bit_to_color(self, bit): 
        return {
            0: (0, 0, 0),
            1: (255, 255, 255)
        }[bit]

    def get_pixel(self, i, j):
        return self.color_to_bit(self.pixels[i, j])

    def set_pixel(self, i, j, bit):
        self.pixels[i, j] = self.bit_to_color(bit)
    
    def save(self, path):
        self.im.save(path)