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


