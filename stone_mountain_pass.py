from PIL import Image, ImageDraw

#=========================================================================| CLASS: MAP |===============================#


class Map:
    """
    Class pertaining to the actual Map image.
    Containing; image, coordinates, color, and assigning color to pixels.
    """
#----------------------------------------------------------| Initialization |----------------------#
    def __init__(self, file):
        self.file = file
        self.coordinates = []
        self.min_elevation = []
        self.max_elevation = []
        self.gradient = {}
        self.width = 0
        self.height = 0

#----------------------------------------------------------| Read The File |-----------------------#
    def data_from_text_file(self):
        print("> Reading File...")
        with open(self.file) as text_file:
            self.file_contents = text_file.read()
            print("     - COMPLETE -")

#----------------------------------------------------------| 'Cleaning' Coordinates |--------------#
    def get_coordinates(self):
        print('\n' "> Fetching List...")
        self.coordinates = [[int(each) for each in line.split()]
                            for line in self.file_contents.strip("\n").split("\n")]
        # for row in self.file_contents:
        #     row = [int(each)
        #            for each in self.file_contents.split("\n")]
        print(self.coordinates)
        print('\n' "› Width of List:", len(self.coordinates))
        print("› Length of Total Numbers:", len(self.file_contents))

    def unique_elevations(self):
        flat_list = [item for sublist in self.coordinates for item in sublist]
        flat_list.sort()
        self.unique_elevations = set(flat_list)

#----------------------------------------------------------| Min/Max Coordinates |-----------------#
    def get_minimum_maximum_coordinates(self):
        min_elevation = self.min_elevation = self.coordinates[0][0]
        max_elevation = self.max_elevation = self.coordinates[0][0]

        for each in self.coordinates:
            for integer in each:
                if integer < self.min_elevation:
                    self.min_elevation = integer
                if integer > self.max_elevation:
                    self.max_elevation = integer
        print("› Minimum Coordinate:", self.min_elevation)
        print("› Maximum Coordinate:", self.max_elevation)
        return (min_elevation, max_elevation)


#----------------------------------------------------------| Elevations to Brightness |------------#
    def elevations_to_brightness(self):
        color_list = []
        row_of_color = []
        min_elevation = self.min_elevation
        max_elevation = self.max_elevation

        # for row in self.coordinates:
        for elevation in self.unique_elevations:
            brightness = (elevation - min_elevation) / \
                (max_elevation - min_elevation)
            # row_of_color.append(color_list)
            greyscale = int(255 * brightness)
            self.gradient[elevation] = (greyscale, greyscale, greyscale, 255)
        #     color_list.append(row_of_color)
        #     row_of_color = []
        # print("› Width of color_list", len(color_list))
        # return color_list

#----------------------------------------------------------| !_Ranges_! |--------------------------#
    # def split_into_lists(self):
    #     # Range goes from 1:darkest to 10:brightest.
    #     self.range1 = []
    #     self.range2 = []
    #     self.range3 = []
    #     self.range4 = []
    #     self.range5 = []
    #     self.range6 = []
    #     self.range7 = []
    #     self.range8 = []
    #     self.range9 = []
    #     self.range10 = []
    #     i = 0

    #     for pixels in self.coordinates:
    #         if i < 4:
    #             self.coordinates.append(i)

    #     print("› Ranges: ")
    #     print("     - Range 1:", self.range1)
    #     print("     - Range 2:", self.range2)
    #     print("     - Range 3:", self.range3)
    #     print("     - Range 4:", self.range4)
    #     print("     - Range 5:", self.range5)
    #     print("     - Range 6:", self.range6)
    #     print("     - Range 7:", self.range7)
    #     print("     - Range 8:", self.range8)
    #     print("     - Range 9:", self.range9)
    #     print("     - Range 10:", self.range10)

#----------------------------------------------------------| Drawing Map |-------------------------#

    def draw_map(self):
        print('\n' "...Generating Map...")
        self.height = len(self.coordinates)
        self.width = len(self.coordinates[0])
        self.image = Image.new(
            "RGBA", (self.width, self.height), color=(0, 0, 255, 255))
        for y, row in enumerate(self.coordinates):
            for x, elevation in enumerate(row):
                self.image.putpixel((x, y), self.gradient[elevation])
        # img = Image.new("RGBA", (601, 601), color=(0, 255, 0, 255))
        # draw = ImageDraw.Draw(img)
        self.image.save('map.png')
        print("> Image Generated!")
        print("     - Height:", self.height)
        print("     - Width:", self.width)
        print("> Image Saved!")
        print("> Image Info:", self.image, '\n')

#=========================================================================| FUNCTION CALL |============================#


if __name__ == "__main__":
    map = Map("elevation_small.txt")
    map.data_from_text_file()
    map.get_coordinates()
    map.unique_elevations()
    map.get_minimum_maximum_coordinates()
    map.elevations_to_brightness()
    map.draw_map()
