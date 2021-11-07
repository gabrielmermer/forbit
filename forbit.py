from pyfzf.pyfzf import FzfPrompt
from datetime import date, datetime

today_date = datetime.today().strftime('%Y.%m.%d')
today_date_object = date.today()

sample_date = date(2020, 9, 9)

print(today_date_object - sample_date)

while True:

    # get the data about the person in most need of contacting from the file
    with open("list.csv", "r") as friendlist_file:
        friendlist = friendlist_file.read().splitlines()

        for i in 

    for i in range(100):
        print("")
    print("Welcome to forbit")
    print(sample_date - today_date_object)
    # display friends name with last contact date
    print("press enter to add a new interaction")
    input()

    # ideally it shoud be opening the list.csv but I don't know how to add new friends from input without breaking things
    with open("friends.txt", "r") as friendlist_file:
        friendlist = friendlist_file.read().splitlines()

    name_list = []

 

    # grabs all the names to a list
    # csv version
    # for i in friendlist:
    #     print(i)
    #     split = i.split(",")
    #     name = split[1]
    #     name_list.append(name)
    #     print(name)
    for i in friendlist:
        name_list.append(i)

    print(friendlist)

    # searching for friends
    fzf = FzfPrompt()
    x = fzf.prompt(name_list)
    print(str(x[0]))

    csv_string = str(today_date + "," + x[0])
    with open("list.csv", "a") as friendlist_file:
        friendlist_file.write(csv_string + "\n")
