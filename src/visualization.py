import matplotlib.pyplot as plt
import pandas as pd


def plot_group_distribution_over_time(
    df: pd.DataFrame,
    timestamp_col: str = "timestamp",
    group_col: str = "group",
    freq: str = "D",  # "D" = daily, "H" = hourly, etc.
    figsize: tuple = (10, 5)
):
    """
    Plots the proportion of each group over time.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing timestamp and group columns.
    timestamp_col : str
        Name of the timestamp column.
    group_col : str
        Name of the group column (e.g., control/treatment).
    freq : str
        Time aggregation frequency (default: daily).
        Examples: "D" (day), "H" (hour)
    figsize : tuple
        Size of the plot.
    """

    # Ensure datetime
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])

    # Aggregate by time
    df["time_bin"] = df[timestamp_col].dt.to_period(freq).dt.to_timestamp()

    # Compute proportions
    distribution = (
        df.groupby("time_bin")[group_col]
        .value_counts(normalize=True)
        .unstack()
    )

    # Plot
    distribution.plot(figsize=figsize)

    plt.title("Group Distribution Over Time")
    plt.xlabel("Time")
    plt.ylabel("Proportion")
    plt.legend(title="Group")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()