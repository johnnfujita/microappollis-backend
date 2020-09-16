def CPFValidator(cpf):
    divisor_1 = 10
    verifier_1 = 0
    divisor_2 = 11
    verifier_2 = 0
    list_cpf = cpf.split()
    for idx in range(len(cpf)):
        if idx <= (len(cpf)-3):
            print(idx)
            verifier_1 += int(cpf[idx]) * divisor_1
            divisor_1 = divisor_1 - 1
    subtractor = verifier_1 % 11
    final_result_1 = 11 - subtractor
    if (final_result_1 > 9 and int(cpf[9]) == 0) or (final_result_1 <= 9 and  final_result_1 == int(cpf[9])):
        for idx in range(len(cpf)):
            if idx <= (len(cpf)-2):
                verifier_2 += int(cpf[idx]) * divisor_2
                divisor_2 = divisor_2 - 1
        subtractor_2 = verifier_2 % 11
        final_result_2 = 11 - subtractor_2
        if (final_result_2 > 9 and int(cpf[10]) == 0) or (final_result_2 <= 9 and int(cpf[10]) == final_result_2):
            return True
        else:
            return False
    else:
        return False


def ccvalidator(ccnumber):

# length OK
# PAN Personal Account Number  7th digit to next to the last digit TODO
# Luhn Algorithm OK
# IIN Issuer Identification Number 4 to 6 intial numbers TODO
# BIN Bank Identification Number TODO

    brand = ""
    valid = False
    if (ccnumber[:2] == "34" or ccnumber[:2] == "37") and len(ccnumber) == 15:
        brand = "American Express"
    elif ccnumber[:3] in ["300", "301", "302", "303", "304", "305", "309"] and len(ccnumber) == 14:
        brand = "Diner Club - Carte Blanche"
    elif ccnumber[:2] in  ["36", "38", "39"] and len(ccnumber) == 14:
        brand = "Diner Club - International"
    elif ccnumber[:2] == "54" and len(ccnumber) == 16:
        brand = "Diner Club - USA & Canada"
    elif (ccnumber[0:4] == "6011" or ccnumber[0:6] in [str(i) for i in range(622126, 622926)] or ccnumber[:3] in [str(i) for i in range(644,650)] or ccnumber[:2] == 65) and len(ccnumber) in [i for i in range(16,20)]:
        # Multi checks 
        brand = "Discover"
    elif ccnumber[:3] in ["637", "638", "639"] and len(ccnumber) == 16:
        brand = "InstaPayment"
    elif ccnumber[:4] in [str(i) for i in range(3528, 3590)] and len(ccnumber) in [16, 17, 18, 19]:
        brand = "JCB"
    elif (ccnumber[:4] in ["5018", "5020", "5038", "5612", "5893", "6304", "6759", "6761", "6762", "6763", "0604", "6390"]) and len(ccnumber) in [12, 13, 14, 15, 16, 17, 18, 19]:
        brand = "Maestro"
    elif (ccnumber[:2] in ["51", "52", "53", "54", "55"] or ccnumber[:6] in [str(i) for i in range(222100, 272100)]) and len(ccnumber) == 16:
        brand = "Master Card"
    elif ccnumber[:4] in ["4026", "4175", "4508", "4913", "4917"] and len(ccnumber) == 16:
        brand = "Visa Electron"
    elif ccnumber[0] == "4" and (len(ccnumber) == 13 or len(ccnumber) == 16 or len(ccnumber) == 19):
        brand = "Visa" 
    else:
        brand = "Unkown"
    
    last_digit = ccnumber[-1]
    
    ccnumber_droped_last_digit = ccnumber[:-1]
    
    reverse_ccnumber = ccnumber_droped_last_digit[::-1]
    
    items_to_sum = []
    counter = 0
    
    for index in range(len(reverse_ccnumber)):
       
        counter+=1
        if index % 2 == 0:
            digit = int(reverse_ccnumber[index]) * 2
            
            if digit <= 9:
                
                items_to_sum.append(digit)
            else:
                
                digit = digit - 9
                
                items_to_sum.append(digit)
        else:
            items_to_sum.append(int(reverse_ccnumber[index]))
            
    sum_up = sum(items_to_sum)
   
    if (sum_up + int(last_digit)) % 10 == 0:
        valid = True
        return [brand, valid]
    else:
        valid = False
        return [brand, valid]



print(ccvalidator("6761769605245436"))

    