from tabulate import tabulate


def main():

    
    print("\nTaskMaster-TODO")
    running = True
    database, count = [], 0

    while running:

        action = get_input()

        if action == "V":
            view(database)
        elif action == "C":
            database, count = create(database, count)
        elif action == "U":
            database = update(database)
        elif action == "D":
            database = delete(database)
        else:
            running = False


def get_input():
    instructions = [{"Key": "V", "Actn": "Viewing a Tasks"},
                    {"Key": "C", "Actn": "Creating a Task"},
                    {"Key": "U", "Actn": "Updating a Task"},
                    {"Key": "D", "Actn": "Deleting a Task"},
                    {"Key": "E", "Actn": "Exiting Interface"}]

    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_outline"))
        action = input("What do you want to do?: ").upper()

        if action in ["V", "C", "U", "D", "E"]:
            return action
        


        else:
            print("Invalid key, try again.")


def view(data):


    print(tabulate(data, headers="keys", tablefmt="rounded_grid"))


def create(data, i):


    task, i = input("Task: "), i + 1


    data.append({"ID": i, "Task": task})
    return data, i


def update(data):


    numbers = list(task["ID"] for task in data)

    while True:
        view(data)


        try:


            i = int(input("What are the tasks will update?: "))
            if i in numbers:
                break
            else:
                print("Your task ID is Invalid, please try again.")

        except ValueError:
            print("Invalid Input has been recieved, Please try again.")

    new = input("What changes you want to make?: ")


    for task in data:
        if task["ID"] == i:
            task["Task"] = new

    return data



def delete(data):

    numbers = list(task["ID"] for task in data)




    while True:
        view(data)
        try:
            i = int(input("Deleting task, but Which one?: "))
            if i in numbers:
                break
            else:
                print("Your task ID is Invalid, please try again.")

        except ValueError:
            print("Invalid Input has been recieved, Please try again.")

    for j in range(len(data)):
        if data[j]["ID"] == i:
            del data[j]
            break

    return data


if __name__ == "__main__":
    main()