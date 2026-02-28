import pandas as pd
POSSIBLE_EXTENSION = ["csv","xls","json"]
def main():

    while True:
        file_name = input("Enter the name of the file to be read:\n")
        file_extension = file_name.split(".")[-1]
        while file_extension not in POSSIBLE_EXTENSION:
            print(f"File extension '.{file_extension:s}' is not supported. Please try again.")
            file_name = input("Enter the name of the file to be read:\n")
            file_extension = file_name.split(".")[-1]
        try:
            df = None
            if file_extension == "csv":
                df = pd.read_csv(file_name)
            elif file_extension == "xls":
                df = pd.read_excel(file_name)
            elif file_extension == "json":
                df = pd.read_json(file_name)

            if df is not None:
                print("File read successfully.")
                print("\nPrinting summary statistics:")
                print(df.describe())
                break

        except FileNotFoundError:
            print(f"Error in reading the file '{file_name}'. Please try again.")

main()