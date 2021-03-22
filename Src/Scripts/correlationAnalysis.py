#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn, scipy
from sklearn.metrics import r2_score
from scipy.stats import kendalltau
from scipy.stats import spearmanr
from scipy.stats import pearsonr

def correlate_data(df):
    # calculate R 2 score
    corr1 = r2_score(df['realAltitude'], df['runningMedian'])
    corr2 = r2_score(df['realAltitude'], df['digitalSmooth'])
    corr3 = r2_score(df['realAltitude'], df['kalman'])
    print("\nR2 score\n{}\n".format("-" * 30))
    print("RunningMedian: ", corr1)
    print("DigitalSmooth: ", corr2)
    print("Kalman: ", corr3)

    # calculate Pearson's correlation
    corr1, _ = pearsonr(df['realAltitude'], df['runningMedian'])
    corr2, _ = pearsonr(df['realAltitude'], df['digitalSmooth'])
    corr3, _ = pearsonr(df['realAltitude'], df['kalman'])
    print("\nPearsons correlation\n{}\n".format("-" * 30))
    print("RunningMedian: ", corr1)
    print("DigitalSmooth: ", corr2)
    print("Kalman: ", corr3)

    # calculate spearman's correlation
    corr1, _ = spearmanr(df['realAltitude'], df['runningMedian'])
    corr2, _ = spearmanr(df['realAltitude'], df['digitalSmooth'])
    corr3, _ = spearmanr(df['realAltitude'], df['kalman'])
    print("\nSpearmans correlation\n{}\n".format("-" * 30))
    print("RunningMedian: ", corr1)
    print("DigitalSmooth: ", corr2)
    print("Kalman: ", corr3)

def main():
    processed_data_path = "../../Data/Processed/filtersData.csv"
    df = pd.read_csv(processed_data_path)
    df.drop("Unnamed: 0", inplace=True, axis=1)
    df.drop("exponentialFilter", inplace=True, axis=1)
    df.drop("movingAveragew3", inplace=True, axis=1)
    df.drop("movingAveragew2", inplace=True, axis=1)
    df.drop("movingAveragew1", inplace=True, axis=1)
    df = df.iloc[20:]
    correlate_data(df=df)
    print("\nINFO: DONE\n")

if __name__ == "__main__":
    main()