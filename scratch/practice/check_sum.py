def check_sum(num_list):

    for i in range(0, len(num_list)-1):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == 0:
                return True

    return False
