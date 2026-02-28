def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        # Reads content from the plaintext file
        with open(filename, "r") as file:
            first_line = file.readline().split(",")  # Take the first line elements. Example: "3", "3"
            width, height = int(first_line[0]), int(first_line[1])
            grid = [["H"] * width for _ in range(height)]

            for line in file:
                line = line.strip()
                if not line:
                    print('Error in line: ""')
                    continue
                try:
                    coordinates = line.split(",")
                    x = int(coordinates[0])
                    y = int(coordinates[1])
                    if 0 <= x < width and 0 <= y < height:
                        grid[y][x] = " "
                except (ValueError, IndexError):
                    print("Error in line: \"{}\"".format(line))

            for row in grid:
                print("".join(row))

    # Read all the lines in the file and store them to be printed in
    # the proper format. Remember to properly deal with incorrect lines.
    # (hint: arrays are a good choice of data structure)

    #
    # Print the image to the console here
    #

    # Deals with file reading exceptions
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except (ValueError, IndexError):
        print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))


main()