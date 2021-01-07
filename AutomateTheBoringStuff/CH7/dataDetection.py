import re


def dateDetector():
    while True:
        try:
            dateRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
            givenText = input("Input text to search: ")
            date1 = dateRegex.search(givenText)
            foundDate = date1.group()
            return dateValidator(foundDate)

        except AttributeError:
            print(''' Text does not contain a valid date. \n Please enter date in mm/dd/yyyy format''')
            print()
            continue


def dateValidator(foundDate):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthsNum = list(range(1,13))

    thirtydays = [9,4,6,11]

    days = int(foundDate[0]+foundDate[1])
    month =int(foundDate[3] + foundDate[4])
    year = ""
    for i in list(range(6,10)):
        year= year+foundDate[i]
    year = int(year)

    #Check if month/days/year are reasonable
    if month > 12:
        return f"bro what is the {month}th month??? {foundDate} is clearly not a real date"
    elif days > 31:
        return f"{days} ??? not a real day though is it???"
    elif year == 3000:
        return f"NOT MUCH HAS CHANGED BUT WE LIVE UNDERWATER"
    elif year > 3000:
        return f"{foundDate} is mega in the future but ok!"

    #Check if days valid in month
    elif month in thirtydays and days == 31:
        return f"30 days hath September blah blah and {months[month]}"

    #February
    elif month == 2:
            if days != 29 and year % 4 == 0:
                return f"{year} is a leap year bruh."
            elif days != 28:
                return f"Since when does February have {days} days???"
    #Goth christmas
    elif month == 10 and days == 31:
        return f"Ok spooky!! Halloween {year}"
    else:
        return f"ok. {foundDate} is  date, I guess."



print(dateDetector())