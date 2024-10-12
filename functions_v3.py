
# ------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Condoms
'''
def scoring_condoms(arr):
    score_condoms = 3
    if arr[1] == "v_unp":
        score_condoms -= 3
    elif arr[1] == "unp":
        score_condoms -= 2
    elif arr[1] == "sl_unp":
        score_condoms -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        score_condoms += 1
    elif arr[1] == "imp":
        score_condoms += 2
    else:
        score_condoms += 3
    
    if arr[2] == "v_unp":
        score_condoms -= 1.5
    elif arr[2] == "unp":
        score_condoms -= 1
    elif arr[2] == "sl_unp":
        score_condoms -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        score_condoms += 0.5
    elif arr[2] == "imp":
        score_condoms += 1
    else:
        score_condoms += 1.5
    
    if arr[3] == "v_unp":
        score_condoms -= 3
    elif arr[3] == "unp":
        score_condoms -= 2
    elif arr[3] == "sl_unp":
        score_condoms -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        score_condoms += 1
    elif arr[3] == "imp":
        score_condoms += 2
    else:
        score_condoms += 3
    
    if arr[4] == "v_unp":
        score_condoms -= 3
    elif arr[4] == "unp":
        score_condoms -= 2
    elif arr[4] == "sl_unp":
        score_condoms -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        score_condoms += 1
    elif arr[4] == "imp":
        score_condoms += 2
    else:
        score_condoms += 3
    
    if arr[5] == 'no':
        pass
    else:
        score_condoms += 1.5

    return score_condoms

# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Internal Condoms
'''

def scoring_internal_condoms(arr):
    internal_condom_score = 3

    if arr[1] == "v_unp":
        internal_condom_score -= 3
    elif arr[1] == "unp":
        internal_condom_score -= 2
    elif arr[1] == "sl_unp":
        internal_condom_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        internal_condom_score += 1
    elif arr[1] == "imp":
        internal_condom_score += 2
    else:
        internal_condom_score += 3

    if arr[2] == "v_unp":
        internal_condom_score -= 1.5
    elif arr[2] == "unp":
        internal_condom_score -= 1
    elif arr[2] == "sl_unp":
        internal_condom_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        internal_condom_score += 0.5
    elif arr[2] == "imp":
        internal_condom_score += 1
    else:
        internal_condom_score += 1.5
    
    if arr[3] == "v_unp":
        internal_condom_score -= 3
    elif arr[3] == "unp":
        internal_condom_score -= 2
    elif arr[3] == "sl_unp":
        internal_condom_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        internal_condom_score += 1
    elif arr[3] == "imp":
        internal_condom_score += 2
    else:
        internal_condom_score += 3
    
    if arr[4] == "v_unp":
        internal_condom_score -= 3
    elif arr[4] == "unp":
        internal_condom_score -= 2
    elif arr[4] == "sl_unp":
        internal_condom_score -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        internal_condom_score += 1
    elif arr[4] == "imp":
        internal_condom_score += 2
    else:
        internal_condom_score += 3
    
    if arr[5] == 'no':
        pass
    elif arr[5] == 'mild':
        internal_condom_score -= 15
    elif arr[5] == 'moderate':
        internal_condom_score -= 25
    else:
        internal_condom_score -= 50
    
    if arr[6] == 'no':
        pass
    else:
        internal_condom_score += 1.5
    
    return internal_condom_score

# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Cervical Cap
'''

def scoring_cervical_cap(arr):
    cervical_cap_score = 3

    if arr[1] == "v_unp":
        cervical_cap_score -= 3
    elif arr[1] == "unp":
        cervical_cap_score -= 2
    elif arr[1] == "sl_unp":
        cervical_cap_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        cervical_cap_score += 1
    elif arr[1] == "imp":
        cervical_cap_score += 2
    else:
        cervical_cap_score += 3
    
    if arr[2] == "v_unp":
        cervical_cap_score -= 3
    elif arr[2] == "unp":
        cervical_cap_score -= 2
    elif arr[2] == "sl_unp":
        cervical_cap_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        cervical_cap_score += 1
    elif arr[2] == "imp":
        cervical_cap_score += 2
    else:
        cervical_cap_score += 3

    if arr[3] == "v_unp":
        cervical_cap_score -= 3
    elif arr[3] == "unp":
        cervical_cap_score -= 2
    elif arr[3] == "sl_unp":
        cervical_cap_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        cervical_cap_score += 1
    elif arr[3] == "imp":
        cervical_cap_score += 2
    else:
        cervical_cap_score += 3
    
    if arr[4] == 'no':
        pass
    elif arr[4] == 'mild':
        cervical_cap_score -= 15
    elif arr[4] == 'moderate':
        cervical_cap_score -= 25
    else:
        cervical_cap_score -= 50
    
    if arr[5] == 'no':
        pass
    elif arr[5] == 'mild':
        cervical_cap_score -= 15
    elif arr[5] == 'moderate':
        cervical_cap_score -= 25
    else:
        cervical_cap_score -= 50
    
    return cervical_cap_score

# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
FAM
'''

def scoring_fam(arr):
    fam_score = 3

    if arr[1] == "v_unp":
        fam_score -= 3
    elif arr[1] == "unp":
        fam_score -= 2
    elif arr[1] == "sl_unp":
        fam_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        fam_score += 1
    elif arr[1] == "imp":
        fam_score += 2
    else:
        fam_score += 3
    
    if arr[2] == "v_unp":
        fam_score -= 3
    elif arr[2] == "unp":
        fam_score -= 2
    elif arr[2] == "sl_unp":
        fam_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        fam_score += 1
    elif arr[2] == "imp":
        fam_score += 2
    else:
        fam_score += 3
    
    if arr[3] == 'no':
        pass
    elif arr[3] == 'mild':
        fam_score -= 15
    elif arr[3] == 'moderate':
        fam_score -= 25
    else:
        fam_score -= 50
    
    return fam_score
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------
    
'''
Arm Implant
'''

def scoring_arm_implant(arr):
    arm_implant_score = 3

    if arr[1] == "v_unp":
        arm_implant_score -= 3
    elif arr[1] == "unp":
        arm_implant_score -= 2
    elif arr[1] == "sl_unp":
        arm_implant_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        arm_implant_score += 1
    elif arr[1] == "imp":
        arm_implant_score += 2
    else:
        arm_implant_score += 3
    
    if arr[2] == "v_unp":
        arm_implant_score -= 3
    elif arr[2] == "unp":
        arm_implant_score -= 2
    elif arr[2] == "sl_unp":
        arm_implant_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        arm_implant_score += 1
    elif arr[2] == "imp":
        arm_implant_score += 2
    else:
        arm_implant_score += 3
    
    if arr[3] == "v_unp":
        arm_implant_score += 3
    elif arr[3] == "unp":
        arm_implant_score += 2
    elif arr[3] == "sl_unp":
        arm_implant_score += 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        arm_implant_score -= 1
    elif arr[3] == "imp":
        arm_implant_score -= 2
    else:
        arm_implant_score -= 3
    
    if arr[4] == 'p':
        arm_implant_score += 3
    else:
        pass

    if arr[5] == "v_unp":
        arm_implant_score += 3
    elif arr[5] == "unp":
        arm_implant_score += 2
    elif arr[5] == "sl_unp":
        arm_implant_score += 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        arm_implant_score -= 1
    elif arr[5] == "imp":
        arm_implant_score -= 2
    else:
        arm_implant_score -= 3

    if arr[6] == "v_unp":
        arm_implant_score += 3
    elif arr[6] == "unp":
        arm_implant_score += 2
    elif arr[6] == "sl_unp":
        arm_implant_score += 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        arm_implant_score -= 1
    elif arr[6] == "imp":
        arm_implant_score -= 2
    else:
        arm_implant_score -= 3

    if arr[7] == 'no':
        pass
    else:
        arm_implant_score += 3
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild' and arr[9] != 'no':
        arm_implant_score -= 7.5
    elif arr[8] == 'moderate' and arr[9] != 'no':
        arm_implant_score -= 12.5
    elif arr[8]=='severe' and arr[9] != 'no':
        arm_implant_score -= 25
    elif arr[8] == 'mild' and arr[9] == 'no':
        arm_implant_score -= 15
    elif arr[8] == 'moderate' and arr[9] == 'no':
        arm_implant_score -= 25
    elif arr[8]== 'severe' and arr[9] == 'no':
        arm_implant_score -= 50
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[8] != 'no':
        arm_implant_score -= 7.5
    elif arr[9] == 'moderate' and arr[8] != 'no':
        arm_implant_score -= 12.5
    elif arr[9] == 'severe' and arr[8] != 'no':
        arm_implant_score -= 25
    elif arr[9] == 'mild' and arr[8] == 'no':
        arm_implant_score -= 15
    elif arr[9] == 'moderate' and arr[8] == 'no':
        arm_implant_score -= 25
    elif arr[9]== 'severe' and arr[8] == 'no':
        arm_implant_score -= 50
    
    if arr[10] == 'no':
        pass
    else:
        arm_implant_score += 3
    
    if arr[11] == 'no':
        pass
    else:
        arm_implant_score += 3
    
    return arm_implant_score

# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Copper IUD
'''

def scoring_copper_iud(arr):
    copper_iud_score = 3

    if arr[1] == "v_unp":
        copper_iud_score -= 3
    elif arr[1] == "unp":
        copper_iud_score -= 2
    elif arr[1] == "sl_unp":
        copper_iud_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        copper_iud_score += 1
    elif arr[1] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[2] == "v_unp":
        copper_iud_score -= 3
    elif arr[2] == "unp":
        copper_iud_score -= 2
    elif arr[2] == "sl_unp":
        copper_iud_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        copper_iud_score += 1
    elif arr[2] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[3] == "v_unp":
        copper_iud_score -= 3
    elif arr[3] == "unp":
        copper_iud_score -= 2
    elif arr[3] == "sl_unp":
        copper_iud_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        copper_iud_score += 1
    elif arr[3] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[4] == "v_unp":
        copper_iud_score -= 3
    elif arr[4] == "unp":
        copper_iud_score -= 2
    elif arr[4] == "sl_unp":
        copper_iud_score -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        copper_iud_score += 1
    elif arr[4] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[5] == 'no':
        pass
    elif arr[5] == 'mild':
        copper_iud_score -= 15
    elif arr[5] == 'moderate':
        copper_iud_score -= 25
    else:
        copper_iud_score -= 50
    
    if arr[6] == 'no':
        pass
    elif arr[6] == 'mild':
        copper_iud_score -= 15
    elif arr[6] == 'moderate':
        copper_iud_score -= 25
    else:
        copper_iud_score -= 50
    
    if arr[7] == 'no':
        pass
    else:
        copper_iud_score += 3
    
    return copper_iud_score

# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Hormonal IUD
'''

def scoring_hormonal_iud(arr):
    hormonal_iud_score = 3
    if arr[1] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[1] == "unp":
        hormonal_iud_score -= 2
    elif arr[1] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[1] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[2] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[2] == "unp":
        hormonal_iud_score -= 2
    elif arr[2] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[2] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3

    if arr[3] == "v_unp":
        hormonal_iud_score += 3
    elif arr[3] == "unp":
        hormonal_iud_score += 2
    elif arr[3] == "sl_unp":
        hormonal_iud_score += 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        hormonal_iud_score -= 1
    elif arr[3] == "imp":
        hormonal_iud_score -= 2
    else:
        hormonal_iud_score -= 3
    
    if arr[4] == 'p':
        hormonal_iud_score += 3
    else:
        pass
    
    if arr[5] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[5] == "unp":
        hormonal_iud_score -= 2
    elif arr[5] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[5] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[6] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[6] == "unp":
        hormonal_iud_score -= 2
    elif arr[6] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[6] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[7] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[7] == "unp":
        hormonal_iud_score -= 2
    elif arr[7] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[7] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[8] == 'no':
        pass
    elif arr[8]  == 'mild':
        hormonal_iud_score -= 15
    elif arr[8] == 'moderate':
        hormonal_iud_score -= 25
    else:
        hormonal_iud_score -= 50
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        patch_score -= 7.5
    elif arr[9] == 'moderate' and arr[10] != 'no':
        patch_score -= 12.5
    elif arr[9]=='severe' and arr[10] != 'no':
        patch_score -= 25
    elif arr[9] == 'mild' and arr[10] == 'no':
        patch_score -= 15
    elif arr[9] == 'moderate' and arr[10] == 'no':
        patch_score -= 25
    elif arr[9]== 'severe' and arr[10] == 'no':
        patch_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        patch_score -= 7.5
    elif arr[10] == 'moderate' and arr[9] != 'no':
        patch_score -= 12.5
    elif arr[10] == 'severe' and arr[9] != 'no':
        patch_score -= 25
    elif arr[10] == 'mild' and arr[9] == 'no':
        patch_score -= 15
    elif arr[10] == 'moderate' and arr[9] == 'no':
        patch_score -= 25
    elif arr[10]== 'severe' and arr[9] == 'no':
        patch_score -= 50
    
    if arr[11] == 'no':
        pass
    else:
        hormonal_iud_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    if arr[13] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    if arr[14] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    if arr[15] == 'no':
        pass
    elif arr[15]  == 'mild':
        hormonal_iud_score -= 15
    elif arr[15] == 'moderate':
        hormonal_iud_score -= 25
    else:
        hormonal_iud_score -= 50
    
    if arr[16] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    return hormonal_iud_score 
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------
    

'''
Patch
'''

def scoring_patch(arr):
    patch_score = 3

    if arr[1] == "v_unp":
        patch_score -= 3
    elif arr[1] == "unp":
        patch_score -= 2
    elif arr[1] == "sl_unp":
        patch_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        patch_score+= 1
    elif arr[1] == "imp":
        patch_score += 2
    else:
        patch_score += 3
    
    if arr[2] == "v_unp":
        patch_score -= 1.5
    elif arr[2] == "unp":
        patch_score -= 1
    elif arr[2] == "sl_unp":
        patch_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        patch_score+= 0.5
    elif arr[2] == "imp":
        patch_score += 1
    else:
        patch_score += 1.5
    
    if arr[3] == "v_unp":
        patch_score -= 3
    elif arr[3] == "unp":
        patch_score -= 2
    elif arr[3] == "sl_unp":
        patch_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        patch_score+= 1
    elif arr[3] == "imp":
        patch_score += 2
    else:
        patch_score += 3
    
    if arr[4] == "v_unp":
        patch_score += 3
    elif arr[4] == "unp":
        patch_score += 2
    elif arr[4] == "sl_unp":
        patch_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        patch_score -= 1
    elif arr[4] == "imp":
        patch_score -= 2
    else:
        patch_score -= 3
    
    if arr[5] == 'ep':
        patch_score += 3
    else:
        pass

    if arr[6] == "v_unp":
        patch_score -= 3
    elif arr[6] == "unp":
        patch_score -= 2
    elif arr[6] == "sl_unp":
        patch_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        patch_score+= 1
    elif arr[6] == "imp":
        patch_score += 2
    else:
        patch_score += 3
    
    if arr[7] == 'no':
        pass
    elif arr[7] == 'mild':
        patch_score -= 15
    elif arr[7] == 'moderate':
        patch_score -= 25
    else:
        patch_score -= 50

    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild' and arr[9] != 'no':
        patch_score -= 7.5
    elif arr[8] == 'moderate' and arr[9] != 'no':
        patch_score -= 12.5
    elif arr[8]=='severe' and arr[9] != 'no':
        patch_score -= 25
    elif arr[8] == 'mild' and arr[9] == 'no':
        patch_score -= 15
    elif arr[8] == 'moderate' and arr[9] == 'no':
        patch_score -= 25
    elif arr[8]== 'severe' and arr[9] == 'no':
        patch_score -= 50
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[8] != 'no':
        patch_score -= 7.5
    elif arr[9] == 'moderate' and arr[8] != 'no':
        patch_score -= 12.5
    elif arr[9] == 'severe' and arr[8] != 'no':
        patch_score -= 25
    elif arr[9] == 'mild' and arr[8] == 'no':
        patch_score -= 15
    elif arr[9] == 'moderate' and arr[8] == 'no':
        patch_score -= 25
    elif arr[9]== 'severe' and arr[8] == 'no':
        patch_score -= 50
    
    if arr[10] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[11] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[13] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[14] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[15] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[16] == 'no':
        pass
    else:
        patch_score += 3
    
    if arr[17] == 'no':
        pass
    else:
        patch_score += 3
    
    if arr[18] == 'no':
        pass
    elif arr[18] == 'mild':
        patch_score -= 15
    elif arr[18] == 'moderate':
        patch_score -= 25
    else:
        patch_score -= 50
    
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        patch_score -= 15
    elif arr[19] == 'moderate':
        patch_score -= 25
    else:
        patch_score -= 50
    
    if arr[20] == 'no':
        pass
    else:
         patch_score += 3
    
    if arr[21] == 'no':
        pass
    else:
         patch_score += 1.5
    
    if arr[22] == 'no':
        pass
    else:
        patch_score -= 100
    
    return patch_score
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------
    
'''
Combo Pill
'''

def scoring_combo_pill(arr):
    combo_pill_score = 3

    if arr[1] == "v_unp":
        combo_pill_score -= 3
    elif arr[1] == "unp":
        combo_pill_score -= 2
    elif arr[1] == "sl_unp":
        combo_pill_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        combo_pill_score += 1
    elif arr[1] == "imp":
        combo_pill_score += 2
    else:
        combo_pill_score += 3
    
    if arr[2] == "v_unp":
        combo_pill_score -= 1.5
    elif arr[2] == "unp":
        combo_pill_score -= 1
    elif arr[2] == "sl_unp":
        combo_pill_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        combo_pill_score += 0.5
    elif arr[2] == "imp":
        combo_pill_score += 1
    else:
        combo_pill_score += 1.5
    
    if arr[3] == "v_unp":
        combo_pill_score -= 3
    elif arr[3] == "unp":
        combo_pill_score -= 2
    elif arr[3] == "sl_unp":
        combo_pill_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        combo_pill_score += 1
    elif arr[3] == "imp":
        combo_pill_score += 2
    else:
        combo_pill_score += 3
    
    if arr[4] == "v_unp":
        combo_pill_score += 3
    elif arr[4] == "unp":
        combo_pill_score += 2
    elif arr[4] == "sl_unp":
        combo_pill_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        combo_pill_score -= 1
    elif arr[4] == "imp":
        combo_pill_score -= 2
    else:
        combo_pill_score -= 3
    
    if arr[5] == 'ep':
        combo_pill_score += 3
    else:
        pass

    if arr[6] == "v_unp":
        combo_pill_score -= 3
    elif arr[6] == "unp":
        combo_pill_score -= 2
    elif arr[6] == "sl_unp":
        combo_pill_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        combo_pill_score+= 1
    elif arr[6] == "imp":
        combo_pill_score += 2
    else:
        combo_pill_score += 3
    
    if arr[7] == 'no':
        pass
    elif arr[7] == 'mild':
        combo_pill_score -= 15
    elif arr[7] == 'moderate':
        combo_pill_score -= 25
    else:
        combo_pill_score -= 50

    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild' and arr[9] != 'no':
        combo_pill_score -= 7.5
    elif arr[8] == 'moderate' and arr[9] != 'no':
        combo_pill_score -= 12.5
    elif arr[8]=='severe' and arr[9] != 'no':
        combo_pill_score -= 25
    elif arr[8] == 'mild' and arr[9] == 'no':
        combo_pill_score -= 15
    elif arr[8] == 'moderate' and arr[9] == 'no':
        combo_pill_score -= 25
    elif arr[8]== 'severe' and arr[9] == 'no':
        combo_pill_score -= 50
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[8] != 'no':
        combo_pill_score -= 7.5
    elif arr[9] == 'moderate' and arr[8] != 'no':
        combo_pill_score -= 12.5
    elif arr[9] == 'severe' and arr[8] != 'no':
        combo_pill_score -= 25
    elif arr[9] == 'mild' and arr[8] == 'no':
        combo_pill_score -= 15
    elif arr[9] == 'moderate' and arr[8] == 'no':
        combo_pill_score -= 25
    elif arr[9]== 'severe' and arr[8] == 'no':
        combo_pill_score -= 50
    
    if arr[10] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[11] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[13] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[14] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[15] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[16] == 'no':
        pass
    else:
        combo_pill_score += 3
    
    if arr[17] == 'no':
        pass
    else:
        combo_pill_score += 3
    
    if arr[18] == 'no':
        pass
    elif arr[18] == 'mild':
        combo_pill_score -= 15
    elif arr[18] == 'moderate':
        combo_pill_score -= 25
    else:
        combo_pill_score -= 50
    
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        combo_pill_score -= 15
    elif arr[19] == 'moderate':
        combo_pill_score -= 25
    else:
        combo_pill_score -= 50
    
    if arr[20] == 'no':
        pass
    else:
         combo_pill_score += 3
    
    if arr[21] == 'no':
        pass
    else:
         combo_pill_score += 3
    
    if arr[22] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    return combo_pill_score
     
# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Mini Pill
'''

def scoring_mini_pill(arr):
    mini_pill_score = 3

    if arr[1] == "v_unp":
        mini_pill_score -= 3
    elif arr[1] == "unp":
        mini_pill_score -= 2
    elif arr[1] == "sl_unp":
        mini_pill_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        mini_pill_score += 1
    elif arr[1] == "imp":
        mini_pill_score += 2
    else:
        mini_pill_score += 3
    
    # Pregnancy Prevention
    if arr[2] == "v_unp":
        mini_pill_score -= 1.5
    elif arr[2] == "unp":
        mini_pill_score -= 1
    elif arr[2] == "sl_unp":
        mini_pill_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        mini_pill_score += 0.5
    elif arr[2] == "imp":
        mini_pill_score += 1
    else:
        mini_pill_score += 1.5
    
    # Management of Periods 
    if arr[3] == "v_unp":
        mini_pill_score -= 3
    elif arr[3] == "unp":
        mini_pill_score -= 2
    elif arr[3] == "sl_unp":
        mini_pill_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        mini_pill_score += 1
    elif arr[3] == "imp":
        mini_pill_score += 2
    else:
        mini_pill_score += 3
    
    # Weight Management
    if arr[4] == "v_unp":
        mini_pill_score += 3
    elif arr[4] == "unp":
        mini_pill_score += 2
    elif arr[4] == "sl_unp":
        mini_pill_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        mini_pill_score -= 1
    elif arr[4] == "imp":
        mini_pill_score -= 2
    else:
        mini_pill_score -= 3
    
    if arr[5] == 'p':
        mini_pill_score += 3
    else:
        pass
    
    if arr[6] == "v_unp":
        mini_pill_score -= 3
    elif arr[6] == "unp":
        mini_pill_score -= 2
    elif arr[6] == "sl_unp":
        mini_pill_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        mini_pill_score += 1
    elif arr[6] == "imp":
        mini_pill_score += 2
    else:
        mini_pill_score += 3
    
    if arr[7] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild' and arr[9] != 'no':
        mini_pill_score -= 7.5
    elif arr[8] == 'moderate' and arr[9] != 'no':
        mini_pill_score -= 12.5
    elif arr[8]=='severe' and arr[9] != 'no':
        mini_pill_score -= 25
    elif arr[8] == 'mild' and arr[9] == 'no':
        mini_pill_score -= 15
    elif arr[8] == 'moderate' and arr[9] == 'no':
        mini_pill_score -= 25
    elif arr[8]== 'severe' and arr[9] == 'no':
        mini_pill_score -= 50
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[8] != 'no':
        mini_pill_score -= 7.5
    elif arr[9] == 'moderate' and arr[8] != 'no':
        mini_pill_score -= 12.5
    elif arr[9] == 'severe' and arr[8] != 'no':
        mini_pill_score -= 25
    elif arr[9] == 'mild' and arr[8] == 'no':
        mini_pill_score -= 15
    elif arr[9] == 'moderate' and arr[8] == 'no':
        mini_pill_score -= 25
    elif arr[9]== 'severe' and arr[8] == 'no':
        mini_pill_score -= 50
    
    if arr[10] == 'no':
        pass
    else:
        mini_pill_score -= 100
    
    if arr[11] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[12] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[13] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[14] == 'no':
        pass
    else:
        mini_pill_score += 1.5
    
    return mini_pill_score

# ------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Ring
'''
def scoring_ring(arr):
    ring_score = 3

    # Cost Effectiveness
    if arr[1] == "v_unp":
        ring_score -= 3
    elif arr[1] == "unp":
        ring_score -= 2
    elif arr[1] == "sl_unp":
        ring_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        ring_score += 1
    elif arr[1] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    # Pregnancy Prevention
    if arr[2] == "v_unp":
        ring_score -= 1.5
    elif arr[2] == "unp":
        ring_score -= 1
    elif arr[2] == "sl_unp":
        ring_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        ring_score += 0.5
    elif arr[2] == "imp":
        ring_score += 1
    else:
        ring_score += 1.5
    
    # Management of Periods 
    if arr[3] == "v_unp":
        ring_score -= 3
    elif arr[3] == "unp":
        ring_score -= 2
    elif arr[3] == "sl_unp":
        ring_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        ring_score += 1
    elif arr[3] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    # Weight Management
    if arr[4] == "v_unp":
        ring_score += 3
    elif arr[4] == "unp":
        ring_score += 2
    elif arr[4] == "sl_unp":
        ring_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        ring_score -= 1
    elif arr[4] == "imp":
        ring_score -= 2
    else:
        ring_score -= 3
    
    # Willingness Vagina
    if arr[6] == "v_unp":
        ring_score -= 3
    elif arr[6] == "unp":
        ring_score -= 2
    elif arr[6] == "sl_unp":
        ring_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        ring_score += 1
    elif arr[6] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    # Hormones
    if arr[5] == 'ep':
        ring_score += 3

    # Medical Practioner 
    if arr[7] == "v_unp":
        ring_score -= 3 
    elif arr[7] == "unp":
        ring_score -= 2
    elif arr[7] == "sl_unp":
        ring_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        ring_score += 1
    elif arr[7] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    # Acne, 1
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild' or arr[8] == 'moderate' or arr[8] == 'severe':
        ring_score += 3
    
    # Anxiety, -1
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        patch_score -= 7.5
    elif arr[9] == 'moderate' and arr[10] != 'no':
        patch_score -= 12.5
    elif arr[9]=='severe' and arr[10] != 'no':
        patch_score -= 25
    elif arr[9] == 'mild' and arr[10] == 'no':
        patch_score -= 15
    elif arr[9] == 'moderate' and arr[10] == 'no':
        patch_score -= 25
    elif arr[9]== 'severe' and arr[10] == 'no':
        patch_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[8] != 'no':
        patch_score -= 7.5
    elif arr[9] == 'moderate' and arr[8] != 'no':
        patch_score -= 12.5
    elif arr[9] == 'severe' and arr[8] != 'no':
        patch_score -= 25
    elif arr[9] == 'mild' and arr[8] == 'no':
        patch_score -= 15
    elif arr[9] == 'moderate' and arr[8] == 'no':
        patch_score -= 25
    elif arr[9]== 'severe' and arr[8] == 'no':
        patch_score -= 50
    
    # Hyper, -1
    if arr[11] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Blood Clots
    if arr[12] == 'no':
        pass
    else:
        ring_score -= 100
    
    # CHF_CAD
    if arr[13] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Breast
    if arr[14] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Smoker
    if arr[15] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Migraine
    if arr[16] == 'no':
        pass
    else:
        ring_score -= 100
    
    # PCOS
    if arr[17] == 'no':
        pass
    else:
        ring_score += 3
    
    # Endometriosis
    if arr[18] == 'no':
        pass
    else:
        ring_score += 3
    
    # Top Gender Dysphoria
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        ring_score -= 15
    elif arr[19] == 'moderate':
        ring_score -= 25
    else:
        ring_score -= 50
    
    # Top Surgery
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        ring_score -= 15
    elif arr[20] == 'moderate':
        ring_score -= 25
    else:
        ring_score -= 50

    # BGDP
    if arr[21] == 'no':
        pass
    else:
        ring_score += 3

    # GDVI

    if arr[22] == 'no':
        pass
    elif arr[22] == 'mild':
        ring_score -= 15
    elif arr[22] == 'moderate':
        ring_score -= 25
    else:
        ring_score -= 50
    
    # GDP

    if arr[23] == 'no':
        pass
    elif arr[23] == 'mild':
        ring_score -= 7.5
    elif arr[23] == 'moderate':
        ring_score -= 12.5
    else:
        ring_score -= 25

    # HRT

    if arr[24] == 'no':
        pass
    else:
        ring_score -= 100
    

# ------------------------------------------------------------------------------------------------------------------------------------------------------

def scoring_shot(arr):
    shot_score = 3

    if arr[1] == "v_unp":
        shot_score -= 1.5
    elif arr[1] == "unp":
        shot_score -= 1
    elif arr[1] == "sl_unp":
        shot_score -= 0.5
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        shot_score += 0.5
    elif arr[1] == "imp":
        shot_score += 1
    else:
        shot_score += 1.5
    
    if arr[2] == "v_unp":
        shot_score -= 3
    elif arr[2] == "unp":
        shot_score -= 2
    elif arr[2] == "sl_unp":
        shot_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        shot_score += 1
    elif arr[2] == "imp":
        shot_score += 2
    else:
        shot_score += 3
    
    if arr[3] == "v_unp":
        shot_score += 3
    elif arr[3] == "unp":
        shot_score += 2
    elif arr[3] == "sl_unp":
        shot_score += 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        shot_score -= 1
    elif arr[3] == "imp":
        shot_score -= 2
    else:
        shot_score -= 3
    
    if arr[4] == 'p':
        shot_score +=3
    else:
        pass

    if arr[5] == "v_unp":
        shot_score -= 3
    elif arr[5] == "unp":
        shot_score -= 2
    elif arr[5] == "sl_unp":
        shot_score -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        shot_score += 1
    elif arr[5] == "imp":
        shot_score += 2
    else:
        shot_score += 3
    
    if arr[6] == "v_unp":
        shot_score -= 3
    elif arr[6] == "unp":
        shot_score -= 2
    elif arr[6] == "sl_unp":
        shot_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        shot_score += 1
    elif arr[6] == "imp":
        shot_score += 2
    else:
        shot_score += 3
    
    if arr[7] == 'no':
        pass
    else:
        shot_score += 3
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild' and arr[9] != 'no':
        shot_score -= 7.5
    elif arr[8] == 'moderate' and arr[9] != 'no':
        shot_score -= 12.5
    elif arr[8]=='severe' and arr[9] != 'no':
        shot_score -= 25
    elif arr[8] == 'mild' and arr[9] == 'no':
        shot_score -= 15
    elif arr[8] == 'moderate' and arr[9] == 'no':
        shot_score -= 25
    elif arr[8]== 'severe' and arr[9] == 'no':
        shot_score -= 50
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[8] != 'no':
        shot_score -= 7.5
    elif arr[9] == 'moderate' and arr[8] != 'no':
        shot_score -= 12.5
    elif arr[9] == 'severe' and arr[8] != 'no':
        shot_score -= 25
    elif arr[9] == 'mild' and arr[8] == 'no':
        shot_score -= 15
    elif arr[9] == 'moderate' and arr[8] == 'no':
        shot_score -= 25
    elif arr[9]== 'severe' and arr[8] == 'no':
        shot_score -= 50
    
    if arr[10] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[11] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[13] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[14] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[15] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[16] == 'no':
        pass
    else:
        shot_score +=3

    if arr[17] == 'no':
        pass
    else:
        shot_score +=3
    
    if arr[18] == 'no':
        pass
    elif arr[18] == 'mild':
        shot_score -= 15
    elif arr[18] == 'moderate':
        shot_score -= 25
    else:
        shot_score -= 50
    
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        shot_score -= 15
    elif arr[19] == 'moderate':
        shot_score -= 25
    else:
        shot_score -= 50
    
    if arr[20] == 'no':
        pass
    else:
        shot_score += 3
    
    if arr[21] == 'no':
        pass
    else:
        shot_score += 1.5
    
    if arr[22] == 'no':
        pass
    else:
        shot_score -= 100
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Sterilization
'''

def scoring_sterilization(arr):
    sterilization_scores = 3

    if arr[1] == "v_unp":
        sterilization_scores -= 3
    elif arr[1] == "unp":
        sterilization_scores -= 2
    elif arr[1] == "sl_unp":
        sterilization_scores -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        sterilization_scores += 1
    elif arr[1] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[2] == "v_unp":
        sterilization_scores -= 3
    elif arr[2] == "unp":
        sterilization_scores -= 2
    elif arr[2] == "sl_unp":
        sterilization_scores -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        sterilization_scores += 1
    elif arr[2] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[3] == "v_unp":
        sterilization_scores -= 3
    elif arr[3] == "unp":
        sterilization_scores -= 2
    elif arr[3] == "sl_unp":
        sterilization_scores -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        sterilization_scores += 1
    elif arr[3] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[4] == "v_unp":
        sterilization_scores -= 3
    elif arr[4] == "unp":
        sterilization_scores -= 2
    elif arr[4] == "sl_unp":
        sterilization_scores -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        sterilization_scores += 1
    elif arr[4] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[5] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    if arr[6] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    if arr[7] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    if arr[8] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    return sterilization_scores

    
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def scoring_gel(arr):

    gel_score = 3

    if arr[1] == "v_unp":
        gel_score -= 3
    elif arr[1] == "unp":
        gel_score -= 2
    elif arr[1] == "sl_unp":
        gel_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        gel_score += 1
    elif arr[1] == "imp":
        gel_score += 2
    else:
        gel_score += 3
    
    if arr[2] == "v_unp":
        gel_score -= 3
    elif arr[2] == "unp":
        gel_score -= 2
    elif arr[2] == "sl_unp":
        gel_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        gel_score += 1
    elif arr[2] == "imp":
        gel_score += 2
    else:
        gel_score += 3
    
    if arr[3] == "v_unp":
        gel_score -= 3
    elif arr[3] == "unp":
        gel_score -= 2
    elif arr[3] == "sl_unp":
        gel_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        gel_score += 1
    elif arr[3] == "imp":
        gel_score += 2
    else:
        gel_score += 3
    
    return gel_score

# ------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Withdrawal
'''

def scoring_withdrawal(arr):

    withdrawal_score = 3

    if arr[1] == "v_unp":
        withdrawal_score -= 3
    elif arr[1] == "unp":
        withdrawal_score -= 2
    elif arr[1] == "sl_unp":
        withdrawal_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        withdrawal_score += 1
    elif arr[1] == "imp":
        withdrawal_score += 2
    else:
        withdrawal_score += 3
    
    if arr[2] == "v_unp":
        withdrawal_score -= 3
    elif arr[2] == "unp":
        withdrawal_score -= 2
    elif arr[2] == "sl_unp":
        withdrawal_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        withdrawal_score += 1
    elif arr[2] == "imp":
        withdrawal_score += 2
    else:
        withdrawal_score += 3
    
    if arr[3] == 'no':
        pass
    elif arr[3] == 'mild':
        withdrawal_score -= 15
    elif arr[3]== 'moderate':
        withdrawal_score -= 25
    else:
        withdrawal_score -= 50
    
    return withdrawal_score
