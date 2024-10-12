import pandas as pd
import itertools
from functions_v3 import scoring_arm_implant, scoring_sterilization, scoring_gel, scoring_withdrawal, scoring_shot, scoring_patch, scoring_mini_pill, scoring_combo_pill, scoring_cervical_cap, scoring_hormonal_iud, scoring_condoms, scoring_copper_iud, scoring_fam, scoring_internal_condoms, scoring_ring

# Data for permutations
contraceptives = [['ring']]
cost_effectiveness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
partner_willingness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
pregnancy_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
prevents_sti = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
management_of_periods = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
weight_management = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
hormones_used = ['ep', 'p', 'none']
willingness_vagina = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
medical_practitioner = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
medical_procedure = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
acne = ['no', 'mild', 'moderate', 'severe']
anxiety = ['no', 'mild', 'moderate', 'severe']
depression = ['no', 'mild', 'moderate', 'severe']
hyper = ['no', 'yes']
bclots = ['no', 'yes']
chf_cad = ['no', 'yes']
breast = ['no', 'yes']
smoker = ['no', 'yes']
migraine = ['no', 'yes']
pcos = ['no', 'yes']
endmt = ['no', 'yes']
tgd = ['no', 'mild', 'moderate', 'severe']
ts = ['no', 'yes']
bgdper = ['no', 'mild', 'moderate', 'severe']
gd_vaginal_insertion = ['no', 'mild', 'moderate', 'severe']
gdp = ['no', 'mild', 'moderate', 'severe']
hrt = ['no', 'yes']

# --------------------------------------------------------------------------------------------------------------------------------------------
# Internal Condoms
contraceptive_int_condom = [['internal_condom']]
internal_condom_options = list(itertools.product(contraceptive_int_condom, cost_effectiveness, pregnancy_prevention, prevents_sti,
                                                  willingness_vagina, 
                                                 gd_vaginal_insertion, gdp 
                                                 ))
int_num = 0
for i in internal_condom_options:
    score = scoring_internal_condoms(i)
    internal_condom_options[int_num] = internal_condom_options[int_num] + (score, ) 
    int_num += 1

df = pd.DataFrame(internal_condom_options)
df.to_csv('individual_permutations/int_condoms_permutations.csv', index=False, header=False)

# --------------------------------------------------------------------------------------------------------------------------------------------

# Cervical Cap
contraceptive_cervical_cap = [['cervical_cap']]
cervical_cap_options = list(itertools.product(contraceptive_cervical_cap, cost_effectiveness, willingness_vagina, medical_practitioner, 
                                              gd_vaginal_insertion, 
                                              gdp))

cervical_cap_num = 0
for i in cervical_cap_options:
    score = scoring_cervical_cap(i)
    cervical_cap_options[cervical_cap_num] = cervical_cap_options[cervical_cap_num] + (score, )
    cervical_cap_num += 1

df = pd.DataFrame(cervical_cap_options)
df.to_csv('individual_permutations/cervical_cap_permutations.csv', index=False, header=False)

# --------------------------------------------------------------------------------------------------------------------------------------------


#FAM
contraceptive_fam = [['FAM']]
fam_options = list(itertools.product(contraceptive_fam, cost_effectiveness, partner_willingness, gdp))

fam_num = 0
for i in fam_options:
    score = scoring_fam(i)
    fam_options[fam_num] = fam_options[fam_num] + (score, )
    fam_num += 1

df = pd.DataFrame(fam_options)
df.to_csv('individual_permutations/fam_permutations.csv', index=False, header=False)


# --------------------------------------------------------------------------------------------------------------------------------------------

# Arm Implant

contraceptive_arm_implant = [['Arm_Implant']]
arm_implant_options = list(itertools.product(contraceptive_arm_implant, pregnancy_prevention, management_of_periods, 
                                             weight_management, hormones_used, medical_practitioner, medical_procedure,
                                             acne, anxiety, depression, bgdper, gdp))

arm_implant_num = 0
for i in arm_implant_options:
    score = scoring_arm_implant(i)
    arm_implant_options[arm_implant_num] = arm_implant_options[arm_implant_num] + (score, )
    arm_implant_num += 1

df = pd.DataFrame(arm_implant_options)
df.to_csv('individual_permutations/arm_implant_permutations.csv', index=False, header=False)


# --------------------------------------------------------------------------------------------------------------------------------------------

# Copper IUD

contraceptive_copper_iud = [['copper_iud']]
copper_iud_options = list(itertools.product(contraceptive_copper_iud, pregnancy_prevention, willingness_vagina, 
                                            medical_practitioner, medical_procedure, bgdper, gd_vaginal_insertion, 
                                            gdp))
copper_iud_num = 0
for i in copper_iud_options:
    score = scoring_copper_iud(i)
    copper_iud_options[copper_iud_num] = copper_iud_options[copper_iud_num] + (score, )
    copper_iud_num += 1

df = pd.DataFrame(copper_iud_options)
df.to_csv('individual_permutations/copper_iud_permutations.csv', index=False, header=False)
# --------------------------------------------------------------------------------------------------------------------------------------------

# Hormonal IUD

contraceptive_h_iud = [['hormonal_iud']]
h_iud_options = list(itertools.product(contraceptive_h_iud, pregnancy_prevention, management_of_periods, weight_management, 
                                       hormones_used, willingness_vagina, medical_practitioner, medical_procedure, 
                                       acne, anxiety, depression, breast, pcos, endmt, bgdper, gd_vaginal_insertion, gdp))

h_iud_num = 0
for i in h_iud_options:
    score = scoring_hormonal_iud(i)
    h_iud_options[h_iud_num] = h_iud_options[h_iud_num] + (score, )
    h_iud_num += 1

df = pd.DataFrame(h_iud_options)
df.to_csv('individual_permutations/hormonal_iud_permutations.csv', index=False, header=False)


# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Patch
'''

contraceptive_patch = [['patch']]

patch_options = list(itertools.product(contraceptive_patch, cost_effectiveness, pregnancy_prevention, management_of_periods,
                                       weight_management, hormones_used, medical_practitioner, acne, anxiety,
                                       depression, hyper, bclots, chf_cad, breast, smoker, migraine, pcos, endmt, 
                                       tgd, ts, bgdper, gdp, hrt))

patch_num = 0
for i in patch_options:
    score = scoring_patch(i)
    patch_options[patch_num] = patch_options[patch_num] + (score, )
    patch_num += 1

df = pd.DataFrame(patch_options)
df.to_csv('individual_permutations/patch_permutations.csv', index=False, header=False)

# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Combo Pill
'''

contraceptive_combo_pill = [['combo_pill']]

combo_pill_options = list(itertools.product(contraceptive_combo_pill, cost_effectiveness, pregnancy_prevention, management_of_periods,
                                       weight_management, hormones_used, medical_practitioner, acne, anxiety,
                                       depression, hyper, bclots, chf_cad, breast, smoker, migraine, pcos, endmt, 
                                       tgd, ts, bgdper, gdp, hrt))

combo_pill_num = 0
for i in combo_pill_options:
    score = scoring_combo_pill(i)
    combo_pill_options[combo_pill_num] = combo_pill_options[combo_pill_num] + (score, )
    combo_pill_num += 1

df = pd.DataFrame(combo_pill_options)
df.to_csv('individual_permutations/combo_pill_permutations.csv', index=False, header=False)

# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Mini Pill
'''

contraceptive_mini_pill = [['mini_pill']]

mini_pill_options = list(itertools.product(contraceptive_mini_pill, cost_effectiveness, pregnancy_prevention, management_of_periods, 
                                           weight_management, hormones_used, medical_practitioner, acne, anxiety, depression, 
                                           breast, pcos, endmt, bgdper, gdp))

mini_pill_num = 0
for i in mini_pill_options:
    score = scoring_mini_pill(i)
    mini_pill_options[mini_pill_num] = mini_pill_options[mini_pill_num] + (score, )
    mini_pill_num += 1

df = pd.DataFrame(mini_pill_options)
df.to_csv('individual_permutations/mini_pill_permutations.csv', index=False, header=False)

# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Ring
'''

contraceptive_ring = [['ring']]

ring_options = list(itertools.product(contraceptive_ring, cost_effectiveness, pregnancy_prevention, management_of_periods, 
                                      weight_management, hormones_used, willingness_vagina, medical_practitioner, acne, 
                                      anxiety, depression, hyper, bclots, chf_cad, breast, smoker, migraine, pcos, 
                                      endmt, tgd, ts, bgdper, gd_vaginal_insertion, gdp))
ring_num = 0
for i in ring_options:
    score = scoring_ring(i)
    ring_options[ring_num] = ring_options[ring_num] + (score, )
    ring_num += 1

df = pd.DataFrame(ring_options)
df.to_csv('individual_permutations/ring_permutations.csv', index=False, header=False)

# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Shot
'''

contraceptive_shot = [['shot']]

shot_options = list(itertools.product(contraceptive_shot, pregnancy_prevention, management_of_periods, 
                                      weight_management, hormones_used, medical_practitioner, medical_procedure, 
                                      acne, anxiety, depression, hyper, bclots, chf_cad, breast, smoker, migraine, 
                                      pcos, endmt, tgd, ts, bgdper, gdp, hrt))
shot_num = 0

for i in shot_options:
    score = scoring_shot(i)
    shot_options[shot_num] = shot_options[shot_num] + (score, )
    shot_num += 1

df = pd.DataFrame(shot_options)
df.to_csv('individual_permutations/shot_permutations.csv', index=False, header=False)


# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Sterilization
'''

contraceptive_sterilization = [['sterilization']]

ster_options = list(itertools.product(contraceptive_sterilization, pregnancy_prevention, management_of_periods, medical_practitioner, 
                                      medical_procedure, pcos, endmt, bgdper, gdp))

ster_num = 0
for i in ster_options:
    score = scoring_sterilization(i)
    ster_options[ster_num] = ster_options[ster_num] + (score, )
    ster_num += 1

df = pd.DataFrame(ster_options)
df.to_csv('individual_permutations/ster_permutations.csv', index=False, header=False)


# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Gel
'''

contraceptive_gel = [['gel']]

gel_options = list(itertools.product(contraceptive_gel, cost_effectiveness, partner_willingness, willingness_vagina))

gel_num = 0
for i in gel_options:
    score = scoring_gel(i)
    gel_options[gel_num] = gel_options[gel_num] + (score, )
    gel_num += 1

df = pd.DataFrame(gel_options)
df.to_csv('individual_permutations/gel_permutations.csv', index=False, header=False)

# --------------------------------------------------------------------------------------------------------------------------------------------

'''
Withdrawal
'''

contraceptive_withdrawal = [['withdrawal']]

withdrawal_options = list(itertools.product(contraceptive_withdrawal, cost_effectiveness, partner_willingness, gdp))

withdrawal_num = 0
for i in withdrawal_options:
    score = scoring_withdrawal(i)
    withdrawal_options[withdrawal_num] = withdrawal_options[withdrawal_num] + (score, )
    withdrawal_num += 1

df = pd.DataFrame(withdrawal_options)
df.to_csv('individual_permutations/withdrawal_permutations.csv', index=False, header=False)