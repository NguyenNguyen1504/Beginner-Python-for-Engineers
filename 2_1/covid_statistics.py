import pandas as pd
import numpy as np
import datetime as dt

DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"]

def get_date_format(dates):
    # Gets a Pandas Series of dates as strings and attempts to convert each string to a DateTime object
    # Conversion is attempted with every format in 'DATE_FORMATS' list
    # Returns a date format that works for all date strings
    for date_format in DATE_FORMATS:
        reject_format = False
        i = 0
        while not reject_format:
            try:
                dt.datetime.strptime(dates[i], date_format)
                if (i + 1) == len(dates):
                    return date_format
            except ValueError:
                reject_format = True
            i += 1
    raise Exception('An error occurred: no valid date format found.')

def read_and_clean(filename):
    try:
        df = pd.read_csv(filename, sep="\t", dtype=str)               # Read TSV file
        date_format = get_date_format(df['date'])                     # Gets an appropriate date format for the DataFrame
        df['date'] = pd.to_datetime(df["date"], format=date_format)   # Converts column values to DateTime objects
        df['date'] = df['date'].dt.date                               # Removes time value from DateTime object
        for char in [",", ".", " "]:                                  # Clean separators in numeric values
            df["cases"] = df["cases"].str.replace(char, "")
        df["cases"] = pd.to_numeric(df["cases"], errors='coerce')         # Turn the case column to numeric values
        return df

    except FileNotFoundError:
        raise FileNotFoundError
    except OSError:
        raise FileNotFoundError
    except Exception:
        raise Exception

def main():

    read_filename = []
    dfs = []
    column_names = ['date']
    for i in range(1,4):
        filename_i = input(f"Enter the name of file #{i}:\n")
        while filename_i in read_filename:
            print(f"File {filename_i} is already included in this analysis. Please choose a different file.")
            filename_i = input(f"Enter the name of file #{i}:\n")

        try:
            df_i = read_and_clean(filename_i)           # Read and clean that file
            read_filename.append(filename_i)            # Record valid filename
            dfs.append(df_i)                            # Store read data frame
            column_names.append("cases_" + filename_i[:-4]) # Add corresponding column name
        except (FileNotFoundError, OSError):
            print(f"Error in reading file {filename_i}. Closing program.")
            return
        except Exception as e:
            print(e)
            return

    merged_dataframe = pd.merge(dfs[0], dfs[1], how='outer', on='date')
    merged_dataframe = pd.merge(merged_dataframe, dfs[2], how='outer', on='date')
    merged_dataframe.columns = column_names
    print("\nPrinting summary statistics:")
    print(merged_dataframe.describe())
    print("\nPrinting first five rows:")
    print(merged_dataframe.head())

main()


