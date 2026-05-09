from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
import numpy as np

def conversion_ztest(df):
    success = df.loc[["treatment", "control"], "sum"].values
    nobs = df.loc[["treatment", "control"], "count"].values

    z_stat, p_value = proportions_ztest(success, nobs, alternative="larger")

    return {
        "variable": "conversion",
        "z_stat": z_stat,
        "p_value": p_value,
    }

def confidence_interval(conversion_rates, summary):

    p1 = conversion_rates["control"]
    p2 = conversion_rates["treatment"]

    n1 = summary.loc["control", "count"]
    n2 = summary.loc["treatment", "count"]

    diff = conversion_rates["treatment"] - conversion_rates["control"]

    se = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)

    ci_low = diff - 1.96 * se
    ci_high = diff + 1.96 * se

    return {
        "Lower Bound": ci_low,
        "Upper Bound": ci_high
    }