from PIL import Image, ImageDraw, ImageFilter


# Creating a class "Map" that deals with the actual map display.
class Map:
    """
    Class pertaining to the actual Map image.
    Containing; image, coordinates, color, and assigning color to pixels.
    """
    with open("elevation_small.txt") as elevations_file:
        file_contents = elevations_file.read()
        # print(file_contents)

    def draw_map(self):
        img = Image.new("RGBA", (601, 601), color=(65, 60, 35, 255))
        draw = ImageDraw.Draw(img)
        # draw.rectangle([0, 0, 600, 600], width=5, outline=(0, 0, 0, 255))
        img.save('map.png')

    # def list_all_coordinates

    # def get_maximum_coordinate

    # def get_minimum_coordinate
