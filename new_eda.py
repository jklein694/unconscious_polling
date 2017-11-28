import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def analyze(data, plot=False):
    # assert self.data, "You must load data to run the analysis"

    if type(data) == pd.DataFrame:
        analyze_df(data, plot)
    elif type(data) == pd.Series:
        analyze_series(data, plot)
    else:
        "Type {} is currently unsupported.\n\nPlease post support requests on GitHub.\nBest,\n- @messiest"

def analyze_series(df, plot=False):
    """
    :param df: Data to run data analysis on
    :type df: pandas DataFrame
    :return: None
    :rtype: None
    """
    assert type(df) is pd.Series, "Expected pandas.Series, {} is type {}".format(df, type(df))

    print("Series Name:\n-  {}".format(df.name))
    print("Data Type: {}\n".format(df.dtype))
    print("Unique Values: {}\n".format(df.nunique()))
    print("Missing Values: {}".format(df.isnull().sum()))
    print("\n{}".format(df.describe(include='all')))

    if df.nunique() == 1:  # skip plotting for columns with only one value
        print("\n{} is homogeneous".format(df.name))
        return

    if df.nunique() == df.count():  # skip plotting when all values are unique
        print("\nIndex eligible - All values of {} are unique\n".format(df.name))

    # plotting
    if not plot:
        return
    else:
        if df.dtype in [np.int64, np.float64]:
            sns.distplot(df)
            plt.title(df.name)
        elif df.dtype in [np.object, datetime.datetime]:
            sns.countplot(df)
            plt.title(df.name)
        plt.show()


def analyze_df(df, plot=False):
    """
    :param df: Data to run data analysis on
    :type df: pandas DataFrame
    :return: None
    :rtype: None
    """
    assert type(df) is pd.DataFrame, "Expected pandas.DataFrame, {} is type {}".format(df, type(df))

    print("Dataframe Index:\n-  {}".format(df.index))
    print("Dataframe Shape:\n-  {}".format(df.shape))
    for item in df:
        print("---" * 39)
        print("Feature: {}".format(item))
        print("Data Type: {}\n".format(df[item].dtypes))
        print("Unique Values: {}\n".format(df[item].nunique()))
        print("Missing Values: {}".format(df[item].isnull().sum()))
        print("\n{}".format(df[item].describe(include='all')))

        if df[item].nunique() == 1:  # skip plotting for columns with only one value
            print("\n{} is homogeneous".format(item))
            continue

        if df[item].nunique() == df[item].count():  # skip plotting when all values are unique
            print("\nIndex eligible - All values of {} are unique\n".format(item))
            continue

        # plotting
        if not plot:
            continue
        else:
            if df[item].dtype in [np.int64, np.float64]:
                sns.distplot(df[item])
                plt.title(item)
            elif df[item].dtype in [np.object, datetime.datetime]:
                sns.countplot(df[item])
                plt.title(item)
            plt.show()


def corr_plot(self, adv=False):
    assert type(self.data) is pd.DataFrame, "Data must be a pandas DataFrame to plot correlations"
    g = sns.PairGrid(self.data)
    g = g.map_diag(sns.kdeplot, shade=True, lw=3, legend=True)
    if adv:
        g = g.map_upper(sns.regplot,
                        scatter_kws=dict(),
                        line_kws=dict(color='b'))
        g = g.map_lower(sns.kdeplot,
                        cmap='Blues_d',
                        color='b')
    else:
        g = g.map_offdiag(sns.regplot,
                          scatter_kws=dict(),
                          line_kws=dict(color='b'))
    plt.show()


analyze(data)