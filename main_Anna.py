import csv
import statistics
import matplotlib.pyplot as plt
from patient_Anna import Patient
import numpy as np
from sklearn.linear_model import LinearRegression

CSV_FILE = "Metadata and Protein Data for Module 1.csv"

# Column names in the CSV are converted to the attribute names used by Patient.
COLUMN_MAP = {
    "Donor ID": "donor_id",
    "Primary Study Name": "primary_study_name",
    "Secondary Study Name": "secondary_study_name",
    "Age at Death": "age_at_death",
    "Sex": "sex",
    "Race (choice=White)": "race_white",
    "Race (choice=Black/ African American)": "race_black",
    "Race (choice=Asian)": "race_asian",
    "Race (choice=American Indian/ Alaska Native)": "race_american_indian",
    "Race (choice=Native Hawaiian or Pacific Islander)": "race_native_hawaiian",
    "Race (choice=Unknown or unreported)": "race_unknown",
    "Race (choice=Other)": "race_other",
    "specify other race": "specify_other_race",
    "Hispanic/Latino": "hispanic_latino",
    "Highest level of education": "highest_education",
    "Years of education": "years_education",
    "APOE Genotype": "apoe_genotype",
    "Cognitive Status": "cognitive_status",
    "Age of onset cognitive symptoms": "age_onset_cognitive_symptoms",
    "Age of Dementia diagnosis": "age_dementia_diagnosis",
    "Known head injury": "known_head_injury",
    "Have they had neuroimaging": "neuroimaging",
    "Last CASI Score": "last_casi_score",
    "Interval from last CASI in months": "interval_last_casi_months",
    "Last MMSE Score": "last_mmse_score",
    "Interval from last MMSE in months": "interval_last_mmse_months",
    "Last MOCA Score": "last_moca_score",
    "Interval from last MOCA in months": "interval_last_moca_months",
    "PMI": "pmi",
    "Rapid Frozen Tissue Type": "rapid_frozen_tissue_type",
    "Ex Vivo Imaging": "ex_vivo_imaging",
    "Fresh Brain Weight": "fresh_brain_weight",
    "Brain pH": "brain_ph",
    "Overall AD neuropathological Change": "overall_ad_change",
    "Thal": "thal",
    "Braak": "braak",
    "CERAD score": "cerad_score",
    "Overall CAA Score": "overall_caa_score",
    "Highest Lewy Body Disease": "highest_lewy_body_disease",
    "Total Microinfarcts (not observed grossly)": "total_microinfarcts_not_grossly",
    "Total microinfarcts in screening sections": "total_microinfarcts_screening",
    "Atherosclerosis": "atherosclerosis",
    "Arteriolosclerosis": "arteriolosclerosis",
    "LATE": "late",
    "RIN": "rin",
    "Severely Affected Donor": "severely_affected_donor",
    "ABeta40 pg/ug": "abeta40",
    "ABeta42 pg/ug": "abeta42",
    "tTAU pg/ug": "ttau",
    "pTAU pg/ug": "ptau",
    }

# Convert numeric-looking CSV values to int/float when possible.
def convert_value(value):
    if value == "":
        return None
    try:
        number = float(value)
        return int(number) if number.is_integer() else number
    except ValueError:
        return value

def load_patients(filename):
    patients = []
    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = {
                COLUMN_MAP[column]: convert_value(value)
                for column, value in row.items()
            }
            patients.append(Patient(**data))
    return patients

def main():
    patients = load_patients(CSV_FILE)
    print(f"Loaded {len(patients)} patients.\n")

    # 5. Sort patients by age at death and print them.
    sorted_patients = sorted(patients, key=lambda p: p.age_at_death)

    # Bar graph: mean +/- SD brain pH, comparing dementia/no dementia and dementia patients while also separating female and male patients.

    statuses = ["No dementia", "Dementia"]
    sexes = ["Female", "Male"]

    x = range(len(statuses))
    width = 0.35
    '''
    plt.figure(figsize=(8, 5))
    for i, sex in enumerate(sexes):
        means = []
        stds = []
        for status in statuses:
            values = [
                p.brain_ph for p in patients
                if p.cognitive_status == status and p.sex == sex
            ]
            means.append(statistics.mean(values))
            stds.append(statistics.stdev(values))
        positions = [value + (i - 0.5) * width for value in x]
        plt.bar(positions, means, width=width, yerr=stds,
            capsize=5, label=sex)
    plt.xticks(list(x), statuses)
    plt.xlabel("Cognitive status")
    plt.ylabel("Brain pH (mean +/- SD)")
    plt.title("Mean Brain pH by Cognitive Status and Sex")
    plt.legend()
    plt.tight_layout()
    plt.savefig("brain_pH_bar_graph.png", dpi=200)
    plt.show()'''

    x = np.array([p.age_at_death for p in patients]).reshape(-1, 1)
    y = np.array([p.brain_ph for p in patients])

    model = LinearRegression()
    model.fit(x, y)

    slope = model.coef_[0]
    intercept = model.intercept_
    r2 = model.score(x, y)
# Annotate equation
    equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"
    plt.text(x.max(), y.max(), equation, color="red", fontsize=12, verticalalignment='top')

    # Scatter plot for age at death vs brain ph
    ages = [p.age_at_death for p in patients]
    ph_values = [p.brain_ph for p in patients]
    plt.figure(figsize=(8, 5))
    plt.scatter(ages, ph_values, alpha=0.75)
    plt.xlabel("Age at Death (years)")
    plt.ylabel("Brain pH")
    plt.title("Brain pH vs. Age at Death")
    plt.tight_layout()
    plt.savefig("brain_pH_vs_age_scatter.png", dpi=200)
    plt.show()

if __name__ == "__main__":
    main()