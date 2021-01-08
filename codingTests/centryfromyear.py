def centuryFromYear(year):
    lst = list(str(year))
    cent = 0
    if len(lst) <= 2:
        cent = 1
    else:
        if len(lst) == 3:
            first2 = lst[:1]
        else:
            first2 = lst[:2]


        if int(year) % 100 == 0:
            separator = ''
            cent = int(separator.join(first2))
        else:
            separator = ''
            cent = int(separator.join(first2)) + 1

    print(cent)

centuryFromYear(400)