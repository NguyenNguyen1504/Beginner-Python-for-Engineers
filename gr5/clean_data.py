import pandas as pd
import numpy as np
import datetime as dt


def main():
    df_results = pd.read_csv("results.csv",encoding="latin1")
    df_bet2122 = pd.read_csv("bet21-22.csv",encoding="latin1")
    df_bet2122 = df_bet2122.drop(columns = ['Div'])

    # Reformat results Date and Time
    df_results['DateTime'] = pd.to_datetime(df_results['DateTime'])
    df_results['Date'] = df_results['DateTime'].dt.date
    df_results['Time'] = df_results['DateTime'].dt.time
    df_results = df_results.drop(columns = ['DateTime'])

    # Drop seasons 1993-2000
    START_DATE = pd.to_datetime('2001-08-01').date()
    df_results = df_results[df_results['Date'] > START_DATE].copy()

    # Reformat bet2122 Date and Time
    df_bet2122['Date'] = pd.to_datetime(df_bet2122['Date'], dayfirst = True).dt.date
    df_bet2122['Time'] = pd.to_datetime(df_bet2122['Time'], format = '%H:%M').dt.time

    # Drop unnecessary columns
    columns_results = ['Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HS', 'AS', 'HST', 'AST']
    df_results = df_results[columns_results].copy()
    columns_bet2122 = ['Date', 'HomeTeam', 'AwayTeam', 'B365H', 'B365D', 'B365A', 'AvgH', 'AvgD', 'AvgA']
    df_bet2122 = df_bet2122[columns_bet2122].copy()

    print("Bet:\n")
    print(df_bet2122.head(30))
    print("Results:\n")
    print(df_results.head(30))


main()
