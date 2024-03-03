import cmath

def lab_2():
    new_model = [300, 100, -100]
    old_model = [80, 50, -20]

    prob_new_model = [0.2, 0.5, 0.3]
    prob_old_model = [0.2, 0.7, 0.1]

    M_new_model = new_model[0] * prob_new_model[0] + new_model[1] * prob_new_model[1] + new_model[2] * prob_new_model[2]
    M_old_model = old_model[0] * prob_old_model[0] + old_model[1] * prob_old_model[1] + old_model[2] * prob_old_model[2]

    print(f"Expected value (new model) - {M_new_model}")
    print(f"Expected value (old model) - {M_old_model}\n")

    var_new_model = prob_new_model[0] * ((new_model[0] - M_new_model) ** 2) + prob_new_model[1] * ((new_model[1] - M_new_model) ** 2) + prob_new_model[2] * ((new_model[2] - M_new_model) ** 2)
    var_old_model = prob_old_model[0] * ((old_model[0] - M_old_model) ** 2) + prob_old_model[1] * ((old_model[1] - M_old_model) ** 2) + prob_old_model[2] * ((old_model[2] - M_old_model) ** 2) 

    print(f"Variance (new model) - {var_new_model}")
    print(f"Variance (old model) - {var_old_model}\n")

    quatro_new_model = cmath.sqrt(var_new_model)
    quatro_old_model = cmath.sqrt(var_old_model)

    print(f"Standard deviation (new model) - {quatro_new_model.real}")
    print(f"Standard deviation (old model) - {quatro_old_model.real}\n")

    cof_A = quatro_new_model.real / abs(M_new_model)
    cof_B = quatro_old_model.real / abs(M_old_model)

    print(f"Coefficient of variation (new model) - {cof_A}")
    print(f"Coefficient of variation (old model) - {cof_B}\n")

    print("Conclusion:")


    if quatro_new_model.real < quatro_old_model.real:
        print("We are introducing a new model")
    else:
        print("It is not worth introducing a new model into production.")

if __name__ == "__main__":
    lab_2()
