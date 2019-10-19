from PIL import Image, ImageDraw


# Creating a class "Map" that deals with the actual map display.
class Map:
    """
    Class pertaining to the actual Map image.
    Containing; image, coordinates, color, and assigning color to pixels.
    """

    def __init__(self, file):
        self.file = file
        self.coordinates = []
        self.min_elevation = []
        self.max_elevation = []
        self.all_colors = []
        self.colors_for_rows = []

    def data_from_text_file(self):
        with open(self.file) as text_file:
            self.file_contents = text_file.read()

    def get_coordinates(self):
        self.coordinates = [[int(each) for each in line.split()]
                            for line in self.file_contents.strip("\n").split("\n")]
        print(self.coordinates)

    def get_minimum_maximum_coordinates(self):
        self.min_elevation = self.coordinates[0][0]
        self.max_elevation = self.coordinates[0][0]

        for each in self.coordinates:
            for integer in each:
                if integer < self.min_elevation:
                    self.min_elevation = integer
                if integer > self.max_elevation:
                    self.max_elevation = integer
        print(self.min_elevation)
        print(self.max_elevation)

    # def give_color_to_elevations(self):
    #     for rows in self.coordinates:
    #         for numbers in rows:
    #             color_int = round(
    #                 ((number - self.min_elevation) / (self.max_elevation - self.min_elevation)) * 255)
    #             self.colors_for_rows.append(color_int)
    #         self.all_colors.append(self.colors_for_rows)
    #         self.colors_for_rows = []
    #     print('test')

    def draw_map(self):
        print('Generating...')
        img = Image.new("RGBA", (601, 601), color=(0, 255, 0, 255))
        draw = ImageDraw.Draw(img)
        img.save('map.png')

    # def list_all_coordinates

    # def get_maximum_coordinate

    # def get_minimum_coordinate


if __name__ == "__main__":
    map = Map("elevation_small.txt")
    map.data_from_text_file()
    map.get_coordinates()
    map.get_minimum_maximum_coordinates()
    # map.give_color_to_elevations()
    map.draw_map()
