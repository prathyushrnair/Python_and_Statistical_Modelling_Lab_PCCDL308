def largest (number_of_list):
    big=number_of_list[0]
    for i in number_of_list:
        if big < i:
            big=i
    return big
result=largest([5,3,4,7,1,3])
print('The largest number is ..',result)