from statsmodels.stats.proportion import proportions_ztest
import statsmodels.formula.api as smf
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


def segment_ztest(df, segment_col):
    """
    Perform one-sided two-proportion z-tests within each segment.
    """

    results = []

    segments = df[segment_col].unique()

    for segment in segments:

        subset = df[df[segment_col] == segment]

        summary = (
            subset.groupby("group")["converted"]
            .agg(["sum", "count"])
        )

        success = summary.loc[
            ["treatment", "control"],
            "sum"
        ].values

        n_obs = summary.loc[
            ["treatment", "control"],
            "count"
        ].values

        z_stat, p_value = proportions_ztest(
            success,
            n_obs,
            alternative="larger"
        )

        treatment_rate = (
            success[0] / n_obs[0]
        )

        control_rate = (
            success[1] / n_obs[1]
        )

        uplift = treatment_rate - control_rate

        relative_uplift = uplift / control_rate

        results.append({
            segment_col: segment,
            "control_rate": control_rate,
            "treatment_rate": treatment_rate,
            "absolute_uplift": uplift,
            "relative_uplift": relative_uplift,
            "z_stat": z_stat,
            "p_value": p_value
        })

    return pd.DataFrame(results)


def logistic_segment_interaction(df, segment_name):

    model = smf.logit(
        f"converted ~ C(group) * C({segment_name})",
        data=df
    ).fit(disp=False)

    interaction_mask = (
        model.params.index.str.contains(":")
    )

    interaction_summary = pd.DataFrame({
        "interaction_term": model.params.index[interaction_mask],
        "coefficient": model.params[interaction_mask].values,
        "p_value": model.pvalues[interaction_mask].values
    })

    interaction_summary["significant_5pct"] = (
        interaction_summary["p_value"] < 0.05
    )

    return interaction_summary