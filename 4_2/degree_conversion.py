import pandas as pd
def to_dms(degree, direction):
    cardinal_direction = ""
    abs_degree = abs(degree)
    if direction == "Latitude":
        if degree > 0:
            cardinal_direction = "N"
        else:
            cardinal_direction = "S"
    elif direction == "Longitude":
        if degree > 0:
            cardinal_direction = "E"
        else:
            cardinal_direction = "W"
    else:
        return None

    mins, abs_degree = abs_degree - int(abs_degree), int(abs_degree)
    mins = mins * 60
    secs, mins = mins - int(mins), int(mins)
    secs = secs * 60

    return "{}°{}\'{:.2f}\" {}".format(abs_degree, mins, secs, cardinal_direction)


def main():
    while True:
        filename = input("Enter the name of the file to be read:\n")
        try:
            table = pd.read_csv(filename)
            print("File read successfully.")
            latitudes = list(map(lambda degree: to_dms(degree,"Latitude"), table["Latitude"]))
            longitudes = list(map(lambda degree: to_dms(degree, "Longitude"), table["Longitude"]))
            coordinates = list(zip(latitudes,longitudes))
            results = list(zip(table["City"], coordinates))
            print("Conversions are as follows:")
            for (city,(lati,longi)) in results:
                print(f"{city}: {lati}, {longi}")

            break
        except (FileNotFoundError, OSError):
            print("Error in reading the file 'unknown.csv'. Please try again.")

main()

