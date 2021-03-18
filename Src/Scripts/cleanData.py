#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def test():
    """"
    Cleans the data by adding the columns and removing the index
    """
    raw_data_path = "../../Data/Raw/18-03-2021Test.csv"
    processd_data_path = "../../Data/Processed/18-03-2021Test.csv"
    df = pd.read_csv(raw_data_path)
    columns = ['Number', 'realAltitude', "kalmanAltitude"]
    df.columns = columns
    df.drop(labels=['Number'], inplace=True, axis=1)
    df.to_csv(processd_data_path)
    print("INFO: Done\n")


def main():
    """"
    Cleans the data by adding the columns and removing the index
    """
    raw_data_path = "../../Data/Raw/Test2.csv"
    processd_data_path = "../../Data/Processed/Test2.csv"
    df = pd.read_csv(raw_data_path)
    columns = ['Number', 'Temperature', "Pressure", "Altitude", "SeaLevelPressure", "SeaLevelAltitude"]
    df.columns = columns
    df.drop(labels=['Number'], inplace=True, axis=1)
    df.to_csv(processd_data_path)
    print("INFO: Done\n")

if __name__ == '__main__':
    test()

