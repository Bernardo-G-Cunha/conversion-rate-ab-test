import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind

def chi_square_group_test(df, col):
    contingency = pd.crosstab(df[col], df["group"])
    chi2, p, dof, expected = chi2_contingency(contingency)
    
    return {
        "variable": col,
        "chi2_stat": chi2,
        "p_value": p
    }


def t_test(df, col):
    control = df[df["group"] == "control"][col]
    treatment = df[df["group"] == "treatment"][col]
    
    stat, p = ttest_ind(control, treatment, equal_var=False)
    
    return {
        "variable": col,
        "t_stat": stat,
        "p_value": p,
        "control_mean": control.mean(),
        "treatment_mean": treatment.mean()
    }