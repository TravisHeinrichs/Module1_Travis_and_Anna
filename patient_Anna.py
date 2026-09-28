class Patient:
    # Represents one patient/donor from the Module 1 dataset.
    def __init__(self, donor_id, primary_study_name, secondary_study_name, age_at_death, sex, race_white,
                 race_black, race_asian, race_american_indian, race_native_hawaiian, race_unknown, race_other,
                 specify_other_race, hispanic_latino, highest_education, years_education, apoe_genotype, cognitive_status,
                 age_onset_cognitive_symptoms, age_dementia_diagnosis, known_head_injury, neuroimaging, last_casi_score,
                 interval_last_casi_months, last_mmse_score, interval_last_mmse_months, last_moca_score,
                 interval_last_moca_months, pmi, rapid_frozen_tissue_type, ex_vivo_imaging, fresh_brain_weight, brain_ph,
                 overall_ad_change, thal, braak, cerad_score, overall_caa_score, highest_lewy_body_disease,
                 total_microinfarcts_not_grossly, total_microinfarcts_screening, atherosclerosis, arteriolosclerosis,
                 late, rin, severely_affected_donor, abeta40, abeta42, ttau, ptau):
        self.donor_id = donor_id
        self.primary_study_name = primary_study_name
        self.secondary_study_name = secondary_study_name
        self.age_at_death = age_at_death
        self.sex = sex
        self.race_white = race_white
        self.race_black = race_black
        self.race_asian = race_asian
        self.race_american_indian = race_american_indian
        self.race_native_hawaiian = race_native_hawaiian
        self.race_unknown = race_unknown
        self.race_other = race_other
        self.specify_other_race = specify_other_race
        self.hispanic_latino = hispanic_latino
        self.highest_education = highest_education
        self.years_education = years_education
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.age_onset_cognitive_symptoms = age_onset_cognitive_symptoms
        self.age_dementia_diagnosis = age_dementia_diagnosis
        self.known_head_injury = known_head_injury
        self.neuroimaging = neuroimaging
        self.last_casi_score = last_casi_score
        self.interval_last_casi_months = interval_last_casi_months
        self.last_mmse_score = last_mmse_score
        self.interval_last_mmse_months = interval_last_mmse_months
        self.last_moca_score = last_moca_score
        self.interval_last_moca_months = interval_last_moca_months
        self.pmi = pmi
        self.rapid_frozen_tissue_type = rapid_frozen_tissue_type
        self.ex_vivo_imaging = ex_vivo_imaging
        self.fresh_brain_weight = fresh_brain_weight
        self.brain_ph = brain_ph
        self.overall_ad_change = overall_ad_change
        self.thal = thal
        self.braak = braak
        self.cerad_score = cerad_score
        self.overall_caa_score = overall_caa_score
        self.highest_lewy_body_disease = highest_lewy_body_disease
        self.total_microinfarcts_not_grossly = total_microinfarcts_not_grossly
        self.total_microinfarcts_screening = total_microinfarcts_screening
        self.atherosclerosis = atherosclerosis
        self.arteriolosclerosis = arteriolosclerosis
        self.late = late
        self.rin = rin
        self.severely_affected_donor = severely_affected_donor
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        def __repr__(self):
            return (f"Patient(id={self.donor_id!r}, age_at_death={self.age_at_death}, "f"sex={self.sex!r}, cognitive_status={self.cognitive_status!r}, "f"brain_pH={self.brain_ph})")

        @classmethod
        def filter_patients(cls, patients, **criteria):
            # Return patients matching all supplied attribute=value criteria.
            return [
                patient for patient in patients
                if all(getattr(patient, attr, None) == value
                       for attr, value in criteria.items())
                ]