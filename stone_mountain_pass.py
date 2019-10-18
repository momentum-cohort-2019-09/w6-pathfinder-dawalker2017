from PIL import Image, ImageDraw, ImageFilter


# Creating a class "Map" that deals with the actual map display.
class Map:
    """
    Class pertaining to the actual Map image.
    Containing; image, coordinates, color, and assigning color to pixels.
    """

    def __init__(self, file):
        self.file = file

    def data_from_text_file(self, file):
        with open('file') as text_file:
            file_contents = text_file.read()

        coordinates_list = [
            int(each) for each in line.split()
            for line in file_contents.split("\n")]

        min = coordinates_list[0][0]
        max = coordinates_list[0][0]

        for each in coordinates_list:
            for integer in each:
                if integer < min:
                    min = integer
                if integer > max:
                    max = integer

        colors_for_text = []
        rows_of_colors = []

        for rows in coordinates_list:
            for numbers in rows:
                color_int = round(((number - min) / (max - min)) * 255)
                rows_of_colors.append(color_int)
        colors_for_text.append(rows_of_colors)
        rows_of_colors = []

    def draw_map(self):
        img = Image.new("RGBA", (601, 601), color=(65, 60, 35, 255))
        draw = ImageDraw.Draw(img)
        # draw.rectangle([0, 0, 600, 600], width=5, outline=(0, 0, 0, 255))
        img.save('map.png')

    # def list_all_coordinates

    # def get_maximum_coordinate

    # def get_minimum_coordinate


if __name__ == "__main__":
    map = Map("elevation_small.txt")
