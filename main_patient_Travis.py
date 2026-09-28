#Name: Travis Heinrichs, tka6pn
from patient_class_Travis import *

# Importing libraries for graphing and statistical analyses
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 
import pandas as pd
from sklearn.linear_model import LinearRegression

Patient.instantiate_from_csv("Metadata and Protein Data for Module 1.csv")

# Bar graph of Amyloid-Beta and Tau concentrations by Atherosclerosis severity

# Creating empty lists to store the data we want to graph
abeta40_levels_of_patients_with_no_atherosclerosis = []
abeta42_levels_of_patients_with_no_atherosclerosis = []
ttau_levels_of_patients_with_no_atherosclerosis = []
ptau_levels_of_patients_with_no_atherosclerosis = []

abeta40_levels_of_patients_with_mild_atherosclerosis = []
abeta42_levels_of_patients_with_mild_atherosclerosis = []
ttau_levels_of_patients_with_mild_atherosclerosis = []
ptau_levels_of_patients_with_mild_atherosclerosis = []

abeta40_levels_of_patients_with_moderate_atherosclerosis = []
abeta42_levels_of_patients_with_moderate_atherosclerosis = []
ttau_levels_of_patients_with_moderate_atherosclerosis = []
ptau_levels_of_patients_with_moderate_atherosclerosis = []

abeta40_levels_of_patients_with_severe_atherosclerosis = []
abeta42_levels_of_patients_with_severe_atherosclerosis = []
ttau_levels_of_patients_with_severe_atherosclerosis = []
ptau_levels_of_patients_with_severe_atherosclerosis = []

# Adding the data to graph to the lists created above
for patient in Patient.filter(Patient.all_patients, atherosclerosis = "None"):
   abeta40_levels_of_patients_with_no_atherosclerosis.append(patient.abeta40_level)
   abeta42_levels_of_patients_with_no_atherosclerosis.append(patient.abeta42_level)
   ttau_levels_of_patients_with_no_atherosclerosis.append(patient.ttau_level)
   ptau_levels_of_patients_with_no_atherosclerosis.append(patient.ptau_level)

for patient in Patient.filter(Patient.all_patients, atherosclerosis = "Mild"):
   abeta40_levels_of_patients_with_mild_atherosclerosis.append(patient.abeta40_level)
   abeta42_levels_of_patients_with_mild_atherosclerosis.append(patient.abeta42_level)
   ttau_levels_of_patients_with_mild_atherosclerosis.append(patient.ttau_level)
   ptau_levels_of_patients_with_mild_atherosclerosis.append(patient.ptau_level)

for patient in Patient.filter(Patient.all_patients, atherosclerosis = "Moderate"):
   abeta40_levels_of_patients_with_moderate_atherosclerosis.append(patient.abeta40_level)
   abeta42_levels_of_patients_with_moderate_atherosclerosis.append(patient.abeta42_level)
   ttau_levels_of_patients_with_moderate_atherosclerosis.append(patient.ttau_level)
   ptau_levels_of_patients_with_moderate_atherosclerosis.append(patient.ptau_level)   

for patient in Patient.filter(Patient.all_patients, atherosclerosis = "Severe"):
   abeta40_levels_of_patients_with_severe_atherosclerosis.append(patient.abeta40_level)
   abeta42_levels_of_patients_with_severe_atherosclerosis.append(patient.abeta42_level)
   ttau_levels_of_patients_with_severe_atherosclerosis.append(patient.ttau_level)
   ptau_levels_of_patients_with_severe_atherosclerosis.append(patient.ptau_level)


x_abeta40_no_atherosclerosis_bar = (statistics.mean(abeta40_levels_of_patients_with_no_atherosclerosis)) #find the means (for bar graph)
x_abeta42_no_atherosclerosis_bar = (statistics.mean(abeta42_levels_of_patients_with_no_atherosclerosis)) #find the means (for bar graph)
x_ttau_no_atherosclerosis_bar = (statistics.mean(ttau_levels_of_patients_with_no_atherosclerosis)) #find the means (for bar graph)
x_ptau_no_atherosclerosis_bar = (statistics.mean(ptau_levels_of_patients_with_no_atherosclerosis)) #find the means (for bar graph)

x_abeta40_mild_atherosclerosis_bar = (statistics.mean(abeta40_levels_of_patients_with_mild_atherosclerosis)) #find the means (for bar graph)
x_abeta42_mild_atherosclerosis_bar = (statistics.mean(abeta42_levels_of_patients_with_mild_atherosclerosis)) #find the means (for bar graph)
x_ttau_mild_atherosclerosis_bar = (statistics.mean(ttau_levels_of_patients_with_mild_atherosclerosis)) #find the means (for bar graph)
x_ptau_mild_atherosclerosis_bar = (statistics.mean(ptau_levels_of_patients_with_mild_atherosclerosis)) #find the means (for bar graph)

x_abeta40_severe_atherosclerosis_bar = (statistics.mean(abeta40_levels_of_patients_with_severe_atherosclerosis)) #find the means (for bar graph)
x_abeta42_severe_atherosclerosis_bar = (statistics.mean(abeta42_levels_of_patients_with_severe_atherosclerosis)) #find the means (for bar graph)
x_ttau_severe_atherosclerosis_bar = (statistics.mean(ttau_levels_of_patients_with_severe_atherosclerosis)) #find the means (for bar graph)
x_ptau_severe_atherosclerosis_bar = (statistics.mean(ptau_levels_of_patients_with_severe_atherosclerosis)) #find the means (for bar graph)

x_abeta40_moderate_atherosclerosis_bar = (statistics.mean(abeta40_levels_of_patients_with_moderate_atherosclerosis)) #find the means (for bar graph)
x_abeta42_moderate_atherosclerosis_bar = (statistics.mean(abeta42_levels_of_patients_with_moderate_atherosclerosis)) #find the means (for bar graph)
x_ttau_moderate_atherosclerosis_bar = (statistics.mean(ttau_levels_of_patients_with_moderate_atherosclerosis)) #find the means (for bar graph)
x_ptau_moderate_atherosclerosis_bar = (statistics.mean(ptau_levels_of_patients_with_moderate_atherosclerosis)) #find the means (for bar graph)


abeta40_no_atherosclerosis_stdev = (statistics.stdev(abeta40_levels_of_patients_with_no_atherosclerosis)) #find standard dev
abeta42_no_atherosclerosis_stdev = (statistics.stdev(abeta42_levels_of_patients_with_no_atherosclerosis))
ttau_no_atherosclerosis_stdev = (statistics.stdev(ttau_levels_of_patients_with_no_atherosclerosis))
ptau_no_atherosclerosis_stdev = (statistics.stdev(ptau_levels_of_patients_with_no_atherosclerosis))

abeta40_mild_atherosclerosis_stdev = (statistics.stdev(abeta40_levels_of_patients_with_mild_atherosclerosis)) #find standard dev
abeta42_mild_atherosclerosis_stdev = (statistics.stdev(abeta42_levels_of_patients_with_mild_atherosclerosis))
ttau_mild_atherosclerosis_stdev = (statistics.stdev(ttau_levels_of_patients_with_mild_atherosclerosis))
ptau_mild_atherosclerosis_stdev = (statistics.stdev(ptau_levels_of_patients_with_mild_atherosclerosis))

abeta40_moderate_atherosclerosis_stdev = (statistics.stdev(abeta40_levels_of_patients_with_moderate_atherosclerosis)) #find standard dev
abeta42_moderate_atherosclerosis_stdev = (statistics.stdev(abeta42_levels_of_patients_with_moderate_atherosclerosis))
ttau_moderate_atherosclerosis_stdev = (statistics.stdev(ttau_levels_of_patients_with_moderate_atherosclerosis))
ptau_moderate_atherosclerosis_stdev = (statistics.stdev(ptau_levels_of_patients_with_moderate_atherosclerosis))

abeta40_severe_atherosclerosis_stdev = (statistics.stdev(abeta40_levels_of_patients_with_severe_atherosclerosis)) #find standard dev
abeta42_severe_atherosclerosis_stdev = (statistics.stdev(abeta42_levels_of_patients_with_severe_atherosclerosis))
ttau_severe_atherosclerosis_stdev = (statistics.stdev(ttau_levels_of_patients_with_severe_atherosclerosis))
ptau_severe_atherosclerosis_stdev = (statistics.stdev(ptau_levels_of_patients_with_severe_atherosclerosis))


atherosclerosis_condition_cols = ['None', 'Mild', 'Moderate', 'Severe'] # Setting x-axis labels for bar graph

x = np.arange(len(atherosclerosis_condition_cols)) #creates a list [0,1,2,3]
width = 0.2

plt.bar(
    x - 1.5*width, #subtracts x value by 0.3 (0.2 times 1.5); this is so each bar representing abeta 40 is displaced 0.3 units from each of the x locations [0,1,2,3]
    [x_abeta40_no_atherosclerosis_bar, #at x = -0.3
     x_abeta40_mild_atherosclerosis_bar, # at x = 0.7
     x_abeta40_moderate_atherosclerosis_bar, #at x = 1.7
     x_abeta40_severe_atherosclerosis_bar], #at x = 2.7
    width, #width of bar
    label="ABeta40",
    yerr=[[0,0,0,0], # so that standard deviation bar only goes up (assymmetrical)
         [abeta40_no_atherosclerosis_stdev,
         abeta40_mild_atherosclerosis_stdev,
         abeta40_moderate_atherosclerosis_stdev,
         abeta40_severe_atherosclerosis_stdev]],
    capsize=5 #width of the cap on the standard deviation bar
)

plt.bar(
    x - 0.5*width, 
    [x_abeta42_no_atherosclerosis_bar, # at x =-0.1
     x_abeta42_mild_atherosclerosis_bar, #at x = 0.9
     x_abeta42_moderate_atherosclerosis_bar, #at x = 1.9
     x_abeta42_severe_atherosclerosis_bar], #at x = 2.9
    width,
    label="ABeta42",
    yerr=[[0,0,0,0],
          [abeta42_no_atherosclerosis_stdev,
          abeta42_mild_atherosclerosis_stdev,
          abeta42_moderate_atherosclerosis_stdev,
          abeta42_severe_atherosclerosis_stdev]],
    capsize=5
)

plt.bar(
    x + 0.5*width,
    [x_ttau_no_atherosclerosis_bar, #at x = 0.1
     x_ttau_mild_atherosclerosis_bar, #at x = 1.1
     x_ttau_moderate_atherosclerosis_bar, #at x = 2.1
     x_ttau_severe_atherosclerosis_bar], #at x = 3.1
    width,
    label="tTAU",
    yerr=[[0,0,0,0],
          [ttau_no_atherosclerosis_stdev,
          ttau_mild_atherosclerosis_stdev,
          ttau_moderate_atherosclerosis_stdev,
          ttau_severe_atherosclerosis_stdev]],
    capsize=5
)

plt.bar(
    x + 1.5*width,
    [x_ptau_no_atherosclerosis_bar, #at x = 0.3
     x_ptau_mild_atherosclerosis_bar, #at x = 1.3
     x_ptau_moderate_atherosclerosis_bar, #at x = 2.3
     x_ptau_severe_atherosclerosis_bar], #at x = 3.3
    width,
    label="pTAU",
    yerr=[[0,0,0,0],
          [ptau_no_atherosclerosis_stdev,
          ptau_mild_atherosclerosis_stdev,
          ptau_moderate_atherosclerosis_stdev,
          ptau_severe_atherosclerosis_stdev]],
    capsize=5
)

plt.xticks(x, atherosclerosis_condition_cols) 

plt.xlabel("Atherosclerosis")
plt.ylabel("Concentration (pg/ug)")
plt.title("Differences in Amyloid Beta and Tau by Atherosclerosis Severity")

plt.legend(title="Protein") #creates the key

f_abeta40, p_abeta40 = stats.f_oneway( #lines 182-208 generates the anova 
   abeta40_levels_of_patients_with_no_atherosclerosis,
   abeta40_levels_of_patients_with_mild_atherosclerosis,
   abeta40_levels_of_patients_with_moderate_atherosclerosis,
   abeta40_levels_of_patients_with_severe_atherosclerosis
)

f_abeta42, p_abeta42 = stats.f_oneway(
   abeta42_levels_of_patients_with_no_atherosclerosis,
   abeta42_levels_of_patients_with_mild_atherosclerosis,
   abeta42_levels_of_patients_with_moderate_atherosclerosis,
   abeta42_levels_of_patients_with_severe_atherosclerosis
)

f_ttau, p_ttau = stats.f_oneway(
   ttau_levels_of_patients_with_no_atherosclerosis,
   ttau_levels_of_patients_with_mild_atherosclerosis,
   ttau_levels_of_patients_with_moderate_atherosclerosis,
   ttau_levels_of_patients_with_severe_atherosclerosis
)

f_ptau, p_ptau = stats.f_oneway(
   ptau_levels_of_patients_with_no_atherosclerosis,
   ptau_levels_of_patients_with_mild_atherosclerosis,
   ptau_levels_of_patients_with_moderate_atherosclerosis,
   ptau_levels_of_patients_with_severe_atherosclerosis
)

plt.text(
   0.02, 0.95, #coordinates for the text, along with line 217
   "One-Way Anova\n" #imputes the anova values
   f"Aβ40: F = {f_abeta40:.3f}, p = {p_abeta40:.3f}\n"
   f"Aβ42: F = {f_abeta42:.3f}, p = {p_abeta42:.3f}\n"
   f"tTAU: F = {f_ttau:.3f}, p = {p_ttau:.3f}\n"
   f"pTAU: F = {f_ptau:.3f}, {p_ptau:.3f}",
   transform=plt.gca().transAxes,
   verticalalignment ="top" #coordinates correspond to top edge of text
)

plt.show()


# Graphing scatter plot of Amyloid-Beta 40 concentration and Brain pH

# Creating empty lists to store the data we want to graph
brain_pH = []
ptau_level = []
ttau_level = []
abeta40_level = []
abeta42_level = []

# Adding the data we want to the lists created above
for patient in Patient.all_patients:
   abeta40_level.append(patient.abeta40_level)
   abeta42_level.append(patient.abeta42_level)
   ptau_level.append(patient.ptau_level)
   ttau_level.append(patient.ttau_level)     
   brain_pH.append(patient.brain_pH) #made list of patients' pH

X = [brain_pH]
y = [abeta40_level]

X = np.array(brain_pH).reshape(-1,1)
y = np.array(abeta40_level)


# Running and graphing linear regression of Amyloid-Beta 40 concentration and Brain pH
model = LinearRegression()
model.fit(X,y)
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)
equation = f"y = {slope:2f}x + {intercept:2f}\nR²= {r2:2f}"
plt.text(0.02, 0.95, equation, transform=plt.gca().transAxes, color = "red", fontsize=12, verticalalignment = "top")

# Creating scatter plot
plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color = "red")
plt.xlabel("Brain pH")
plt.ylabel("Aβ40 Concentration (pg/ug)")
plt.title("Amyloid-Beta 40 vs Brain pH")

plt.show()


X = [brain_pH]
y = [abeta42_level]

X = np.array(brain_pH).reshape(-1,1)
y = np.array(abeta42_level)


# Running and graphing linear regression of Amyloid-Beta 42 concentration and Brain pH
model = LinearRegression()
model.fit(X,y)
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)
equation = f"y = {slope:2f}x + {intercept:2f}\nR²= {r2:2f}"
plt.text(0.02, 0.95, equation, transform=plt.gca().transAxes, color = "red", fontsize=12, verticalalignment = "top")

# Creating scatter plot
plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color = "red")
plt.xlabel("Brain pH")
plt.ylabel("Aβ42 Concentration (pg/ug)")
plt.title("Amyloid-Beta 42 vs Brain pH")

plt.show()


X = [brain_pH]
y = [ttau_level]

X = np.array(brain_pH).reshape(-1,1)
y = np.array(ttau_level)


# Running and graphing linear regression of ttau concentration and Brain pH
model = LinearRegression()
model.fit(X,y)
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)
equation = f"y = {slope:2f}x + {intercept:2f}\nR²= {r2:2f}"
plt.text(0.02, 0.95, equation, transform=plt.gca().transAxes, color = "red", fontsize=12, verticalalignment = "top")

# Creating scatter plot
plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color = "red")
plt.xlabel("Brain pH")
plt.ylabel("tTAU Concentration (pg/ug)")
plt.title("tTAU vs Brain pH")

plt.show()

X = [brain_pH]
y = [ptau_level]

X = np.array(brain_pH).reshape(-1,1)
y = np.array(ptau_level)


# Running and graphing linear regression of ptau concentration and Brain pH
model = LinearRegression()
model.fit(X,y)
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)
equation = f"y = {slope:2f}x + {intercept:2f}\nR²= {r2:2f}"
plt.text(0.02, 0.95, equation, transform=plt.gca().transAxes, color = "red", fontsize=12, verticalalignment = "top")

# Creating scatter plot
plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color = "red")
plt.xlabel("Brain pH")
plt.ylabel("pTAU Concentration (pg/ug)")
plt.title("pTAU vs Brain pH")

plt.show()