### creating library ####
import pandas as pd


def analyze_iqr(data):
    
    """
     Automatic IQR analysis
    Input: list or pandas Series
    Output: dictionary with Q1, Q3, IQR, lower bound, upper bound, outliers
    """

    # convert to pandas series if needed.pandas series object madhe convert karte 
    # Pandas Series = Excel cha column sarkha, jithe numeric calculations + quantiles easy karayche.
    # if not isinstance(data, pd.Series): → fakta jar data already Pandas Series nasel tar convert kar
    # Jar already Pandas Series asel tar convert nahi kart
    if not isinstance(data, pd.Series):
        data = pd.Series(data)

    # quartiles 
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)

    IQR = q3 - q1

    # bounds
    lower_bound = q1 - 1.5 * IQR
    upper_bound = q3 + 1.5 * IQR

    # outliers mahnje lower outlier asel lower limit kadycha nahitr upper- limit ne kadhycha 
    outliers = data[(data < lower_bound) | (data > upper_bound)]

    # reutrn everything in dictonery
    result = {
        "q1": q1,
        "q3": q3,
        "IQR": IQR,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "outliers": outliers.tolist()  # tolist mahnje pandas series la convert karto normal python list madhe
    }

    return result


# why we used tolist Dictionary madhe clean output hava asto
# JSON compatible hava asto
# User la simple list disavi
# Printing neat diste  [Pandas object → .tolist() → Python list]