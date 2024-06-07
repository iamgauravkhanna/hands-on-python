for i in [1, 2, 3, 4, 5]:
    print('Printing after each loop')
    print('i = ' + str(i))
    if i == 2:
        print('Element found')
        print('')
        break
    # else:
    #     print('i not found')
print(i)