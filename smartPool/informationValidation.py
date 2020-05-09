

def validation_cpf(cpf):

    cpf = cpf.replace(".","")
    cpf = cpf.replace("-","")

    if cpf.isnumeric() is False or len(cpf) != 11:

        return False
    else:
        cpf_int = []
        for i in cpf:
            cpf_int.append(int(i))

        cpf_test = cpf_int[:9]

        sum_digits = 0

        while len(cpf_test) < 11:
            for i,v in enumerate(cpf_test):
                sum_digits += (len(cpf_test) +1 -i)*v


            rest = sum_digits%11
            sum_digits = 0

            if rest > 1:
                rest = 11 - rest
                cpf_test.append(rest)
            else:
                rest = 0
                cpf_test.append(rest)


        if cpf_test == cpf_int:
            return True

        else:
            return False


#def validation_password():