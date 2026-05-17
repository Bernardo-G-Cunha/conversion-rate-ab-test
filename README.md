# Conversion Rate A/B Test Analysis

A complete A/B testing analysis focused on conversion rate optimization, including experiment validation, statistical inference, guardrail metric evaluation, and segmentation analysis.

---

## Project Overview

This project analyzes the results of a randomized A/B test designed to evaluate whether a new product experience improves user conversion performance.

The analysis covers the full experimentation workflow:

* data cleaning and preprocessing
* experiment validation
* statistical hypothesis testing
* effect size estimation
* guardrail metric analysis
* segmentation analysis
* interaction effect modeling
* executive-level reporting

The primary objective is to determine whether the treatment group achieves a higher conversion rate than the control group while ensuring that revenue-related metrics are not negatively affected.

---

## Business Context

A company wants to evaluate whether a proposed product variation leads to improved user conversion.

Users are randomly assigned to either:

* **Control Group** → current experience
* **Treatment Group** → proposed variation

The analysis evaluates whether the treatment produces statistically and practically meaningful improvements.

---

## Dataset

The dataset contains user-level experimental observations, including:

| Column             | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `user id`          | Unique user identifier                                   |
| `group`            | Experimental group assignment (`control` or `treatment`) |
| `landing_page`     | Page version shown to the user                           |
| `converted`        | Binary conversion outcome                                |
| `purchase_amount`  | Purchase amount per user                                 |
| `timestamp`        | Event timestamp                                          |
| `age`              | User age                                                 |
| `gender`           | User gender                                              |
| `device_type`      | User device category                                     |
| `location`         | Geographic location                                      |
| `session_duration` | Session duration                                         |
| `pages_visited`    | Number of pages visited                                  |

---

## Project Structure

```text
conversion-rate-ab-test/
│
├── data/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_experiment_validation.ipynb
│   ├── 03_statistical_analysis.ipynb
│   └── 04_segmentation_analysis.ipynb
│
├── reports/
│   └── final_report.md
│
├── src/
│   ├── stats.py
│   ├── visualization.py
│   └── validation.py
│
├── requirements.txt
└── README.md
```

---

## Analysis Workflow

### 1. Data Cleaning and Preprocessing

The raw dataset is cleaned and validated before analysis.

Main preprocessing steps include:

* duplicate removal
* missing value handling
* type conversion
* data consistency checks
* validation assertions

---

### 2. Experiment Validation

Before interpreting experimental results, several validation procedures are performed to verify the integrity of the randomization process.

Validation steps include:

* Sample Ratio Mismatch (SRM) analysis
* covariate balance testing
* temporal consistency analysis

The results provide no evidence against the validity of the experiment design.

---

### 3. Statistical Analysis

The primary analysis evaluates whether the treatment group achieves a higher conversion rate than the control group.

Methods used:

* one-sided two-proportion z-test
* confidence interval estimation
* uplift calculation
* effect size interpretation

### Main Result

| Metric          | Control | Treatment               |
| --------------- | ------- | ----------------------- |
| Conversion Rate | 11.87%  | 17.95%                  |
| Absolute Uplift | -       | +6.08 percentage points |
| Relative Uplift | -       | +51%                    |

The treatment produced a statistically significant positive effect on conversion performance.

---

### 4. Guardrail Metric Analysis

Purchase amount is evaluated as a guardrail metric to ensure that conversion gains are not accompanied by negative business effects.

Results indicate that the treatment also improved average revenue per user (ARPU).

| Metric                  | Control | Treatment |
| ----------------------- | ------- | --------- |
| Average Purchase Amount | 4.45    | 6.76      |
| Relative Increase       | -       | +52%      |

---

### 5. Segmentation Analysis

The treatment effect is evaluated across multiple user segments:

* device type
* gender
* location

Additional logistic regression models with interaction terms are used to assess treatment heterogeneity.

The analysis suggests that the observed treatment effect remains reasonably consistent across evaluated user groups.

---

## Tools and Technologies

* Python
* Pandas
* NumPy
* SciPy
* Statsmodels
* Matplotlib
* Jupyter Notebook

---

## Key Statistical Concepts

This project applies several statistical concepts commonly used in experimentation and product analytics:

* randomized controlled experiments
* causal inference
* hypothesis testing
* confidence intervals
* uplift analysis
* guardrail metrics
* covariate balance
* logistic regression
* interaction effects

---

## Final Recommendation

The results support deploying the treatment as a replacement for the current experience.

The treatment improved both conversion performance and revenue-related metrics while remaining reasonably consistent across evaluated user segments.

Continued monitoring after deployment would still be recommended in a real production environment.

---

## Repository Goals

This project was developed to demonstrate practical skills in:

* experimentation analysis
* statistical inference
* product analytics
* business-oriented communication
* end-to-end analytical workflows

---

## Author

Bernardo Garcia Cunha
