#Name: Travis Heinrichs, tka6pn

import csv #so that I can use the dictreader to convert file into list
class Patient:
    all_patients = []
#here's my constructor:
    def __init__(self, donor_ID: str, age_at_death: int, sex: str, years_of_education: int, apoe_genotype: str, cognitive_status: str, brain_pH = float, thal_score = str, atherosclerosis = str, abeta40_level = float, abeta42_level = float, ttau_level = float, ptau_level = float): 
            self.donor_ID = donor_ID
            self.age_at_death = age_at_death
            self.sex = sex
            self.years_of_education = years_of_education
            self.apoe_genotype = apoe_genotype
            self.cognitive_status = cognitive_status
            self.brain_pH = brain_pH
            self.thal_score = thal_score
            self.atherosclerosis = atherosclerosis
            self.abeta40_level = abeta40_level
            self.abeta42_level = abeta42_level
            self.ttau_level = ttau_level
            self.ptau_level = ptau_level
            Patient.all_patients.append(self)
#here's my representer:
    def __repr__(self):  
            return f"{self.donor_ID}: ({self.age_at_death} | {self.sex} | {self.years_of_education} | {self.apoe_genotype} | {self.cognitive_status} | {self.brain_pH} | {self.thal_score} | {self.atherosclerosis} | {self.abeta42_level} | {self.ptau_level})" 
#here's how I created patient objects from the csv data:
    @classmethod 
    def instantiate_from_csv(cls, filename: str):

        #the code below will open the .csv file and create a list of all the rows in your spreadsheet
        
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
        
        #the code below will create a patient object for each row, based on the data: 
        
            for row in rows_of_patients:
                    Patient(
                    donor_ID = str(row['Donor ID']),
                    age_at_death = int(row['Age at Death']),
                    sex = str(row['Sex']),
                    years_of_education = int(row['Years of education']),
                    apoe_genotype = str(row['APOE Genotype']),
                    cognitive_status = str(row['Cognitive Status']),
                    brain_pH = float(row['Brain pH']),
                    thal_score = str(row['Thal']),
                    atherosclerosis = str(row['Atherosclerosis']),
                    abeta40_level= float(row['ABeta40 pg/ug']),
                    abeta42_level = float(row['ABeta42 pg/ug']),
                    ttau_level = float(row['pTAU pg/ug']),
                    ptau_level = float(row['pTAU pg/ug'])
                )
#here's my getter:
    def get_brain_pH(self): 
        return self.brain_pH
#here's my code for a class method to filter and print
    @classmethod
    def filter(cls, list, donor_ID:str ="any", age_at_death:int ="any", sex:str ="any", years_of_education:int ="any", apoe_genotype:str ="any", cognitive_status:str ="any", brain_pH:float ="any", thal_score:str ="any", atherosclerosis:str ="any", abeta40_level:float = "any", abeta42_level:float ="any", ttau_level:float ="any", ptau_level:float = "any"):
        all_patients = list
        remove_list = []
        attr_list = (
                    donor_ID,
                    age_at_death,
                    sex,
                    years_of_education,
                    apoe_genotype,
                    cognitive_status,
                    brain_pH,
                    thal_score,
                    atherosclerosis,
                    abeta40_level,
                    abeta42_level,
                    ttau_level,
                    ptau_level
                    )
        attr_name = (
                    "donor_ID",
                    "age_at_death",
                    "sex",
                    "years_of_education",
                    "apoe_genotype",
                    "cognitive_status",
                    "brain_pH",
                    "thal_score",
                    "atherosclerosis",
                    "abeta40_level",
                    "abeta42_level",
                    "ttau_level",
                    "ptau_level"
                    )
        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in all_patients:
                    if getattr(patient,attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)
                all_patients = [patient for patient in all_patients if patient not in remove_list]
                remove_list.clear()

        return all_patients