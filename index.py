def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max



print(max_num_in_list([5,7,3,1000,-1]))      # changes made
      
