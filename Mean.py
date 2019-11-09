def compute_average_method1():
    numbers_list=[]
    while True:
        k = input("Please enter a number: ")
        if not k:
            break
        else:
            numbers_list.append(float(k))

    if len(numbers_list) > 0:
        print("The mean is {}".format(sum(numbers_list) / len(numbers_list)))
    else:
        print("Empty list")


def compute_average_method2():
    k = input("Enter numbers comma separated: ")  #
    float_k = [float(k1) for k1 in k.split(",")]    # ["1", "2", "3", "4"]
    print("The average is {}".format(sum(float_k)/len(float_k)))


compute_average_method2()