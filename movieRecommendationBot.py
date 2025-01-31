from csv import DictReader
from sys import exit
from random import randint
from os import system
from time import sleep
from pyfiglet import figlet_format
from termcolor import colored


def main():
    greeting = figlet_format("Welcome to the Movie Recommendation Bot", font = "small")
    print(colored(greeting, "green"))

    first_choice = enquire(question_materials("Do you want to specify a movie category? "))
    print()

    if first_choice == "yes":
        category = enquire(category_materials()).capitalize()
        print()

        if category == "Sci-fi":
            category = "Sci-Fi"

        elif category == "Stop":
            print("The program has been terminated")
            exit(0)

    elif first_choice == "no":
        category = "none"

    else:
        print("The program has been terminated")
        exit(0)

    second_choice = enquire(question_materials("Would you like to list the movies in a certain ranking range on IMDB? "))
    print()

    if second_choice == "yes":
        counter = 0
        while True:
            if counter == 0:
                lower_bound = get_float("Enter a rank with a lower bound of 0: ")
                upper_bound = get_float("Enter a rank with an upper bound of 10: ")

            else:
                print("\nMake sure the selected boundaries are reasonable and meet the specified conditions\n")
                lower_bound = get_float("Lower bound: ")
                upper_bound = get_float("Upper bound: ")

            if lower_bound >= 0 and upper_bound <= 10 and lower_bound <= upper_bound:
                break

            else:
                counter = 1

    elif second_choice == "no":
        lower_bound, upper_bound = 0, 10

    else:
        print("The program has been terminated")
        exit(0)

    sleep(0.3)
    system('clear')

    if first_choice == "no" and second_choice == "no":
        print("You have not specified any criteria for the movies to be listed\n")

    listmovies(category, lower_bound, upper_bound)


def listmovies(category, lower_rating, upper_rating):
    file = open("IMDB-Sorted-Movie-Data.csv")
    reader = DictReader(file)

    list = []
    if category == "none":
        for movie in reader:
            rating = float(movie["Rating"])
            if rating >= lower_rating and rating <= upper_rating:
                list.append(movie)

    else:
        for movie in reader:
            genre, rating = movie["Genre"], float(movie["Rating"])
            if not genre.find(category) == -1 and rating >= lower_rating and rating <= upper_rating:
                list.append(movie)

    file.close()

    size = len(list)
    if size == 0:
        print("No films were found that met the criteria")

    elif size == 1:
        print("Only 1 movie was found that met the criteria")

    else:
        print(f"{size} movies were found that met the criteria")

    if not size == 0:
        print("\n(If you say no, we will make a list of the results together)")
        choice = enquire(question_materials("Would you like me to suggest a movie for you? "))

        if choice == "yes":
            recommended = list[randint(0, size - 1)]
            title, rating = recommended["Title"], recommended["Rating"]

            sleep(0.3)
            system('clear')

            print(f"Here is my suggestion...\n\nMovie name: {title}\tIMDB rating: {rating}")
            decision = enquire(question_materials("\nDo you want to see the details of this movie? "))

            if decision == "yes":
                flag = 0

            else:
                return

        elif choice == "no":

            sleep(0.3)
            system('clear')

            if size <= 50:
                print(f"I can list up to {size} movies for you")

            else:
                print("(I'll limit you to 50 for the sake of an easily viewable list)")
                size = 50

            counter = 0
            while True:
                if counter == 0:
                    number = get_int("How many movies would you like to view? ")

                else:
                    number = get_int("You need to enter a number that meets the criteria: ")

                print()

                if number == 0:
                    return

                elif number > 0 and number <= size:
                    break

                else:
                    counter = 1

            i = 1
            for movie in list:
                if i > number:
                    break

                print(str(i) + '.', movie["Title"] + '  ' + movie["Rating"])
                i += 1
                sleep(0.1)
                print()

            length = len(list)

            while length > 0 and number < length:
                flag = eliminate(list, number)
                length = len(list)

                if flag == 1:
                    break

                elif flag == 2:
                    return

            choice = enquire(question_materials("Do you want to select a movie from the list and view its details? "))

            print()

            counter = 0
            if choice == "yes":
                while True:
                    if counter == 0:
                        requested = get_int("Enter the movie number: ")

                    else:
                        requested = get_int("Please enter a number from the list: ")

                    print()

                    if requested >= 1 and requested <= number:
                        break

                    else:
                        counter = 1

                flag = 1

            else:
                return

        else:
            print("\nThe program has been terminated")
            return

        sleep(0.3)
        system('clear')


        if flag == 0:
            moviedetails(recommended)

        else:
            moviedetails(list[requested - 1])

    else:
        return 1


def eliminate(movie_list, output_count):
    new_option = enquire(question_materials("If there are movies you've watched before, do you want me to remove them and create a new list? "))
    print()

    if new_option == "yes":
        size = len(movie_list)

        counter = 0
        while True:
            if counter == 0:
                piece = get_int("How many movies do you want to exclude? ")
                print()

            else:
                piece = get_int("Please enter a number that will not exceed the limits: ")
                print()

            if piece <= size - output_count and piece <= output_count and piece >= 0:
                break

            else:
                counter = 1

        if piece == 0:
            return 1

        print("Movies to exclude from the list")

        take_away = []

        for i in range(piece):
            counter = 0
            flag = 0

            while True:
                if counter == 0:
                    available = get_int(str(i + 1) + '. ')

                elif counter == 1:
                    if flag == 0:
                        print()

                    available = get_int(f"Enter a valid number for movie {i + 1}: ")
                    print()

                    flag = 1

                else:
                    if flag == 0:
                        print()

                    print("You already chose this movie")
                    available = get_int(f"Try entering a different number for movie {i + 1}: ")
                    print()

                    flag = 1

                if available <= output_count and available >= 1:
                    try:
                        take_away.index(available)
                    except ValueError:
                        break
                    else:
                        counter = 2

                else:
                    counter = 1

            take_away.append(available)

        rectifier = 0
        for i in range(piece):
            movie_list.pop(take_away[i] - 1 - rectifier)
            rectifier += 1

        system('clear')

        if output_count <= len(movie_list):
            i = 1
            for movie in movie_list:
                if i > output_count:
                    break

                print(str(i) + '.', movie["Title"] + '  ' + movie["Rating"])
                i += 1
                sleep(0.1)
                print()

        else:
            for movie in movie_list:
                print(str(i) + '.', movie["Title"] + '  ' + movie["Rating"])
                sleep(0.1)
                print()

        return 0

    elif new_option == "no":
        return 1

    else:
        print("The program has been terminated")
        return 2


def moviedetails(movie):
    print("Name:", movie["Title"] + '\n')

    sleep(0.1)

    print("Genre:", movie["Genre"] + '\n')

    sleep(0.1)

    print("Storyline:", movie["Description"] + '\n')

    sleep(0.1)

    print("Director:", movie["Director"] + '\n')

    sleep(0.1)

    print("Actors:", movie["Actors"] + '\n')

    sleep(0.1)

    print("Release date:", movie["Year"] + '\n')

    runtime = int(movie["Runtime (Minutes)"])
    hour = int(runtime / 60)
    minute = runtime % 60

    sleep(0.1)

    print(f"Runtime: {hour} hour(s) {minute} minute(s)" + '\n')

    sleep(0.1)

    revenue = movie["Revenue (Millions)"]
    if revenue == '':
        revenue = "no information"
        print("Revenue:", revenue + '\n')

    else:
        print("Revenue:", revenue, "millions" + '\n')

    sleep(0.1)

    print("IMDB rating:", movie["Rating"] + '\n')

    metascore = movie["Metascore"]
    if metascore == '':
        metascore = "no information"

    sleep(0.1)

    print("Metascore:", metascore + '\n')


def enquire(materials):
    counter = 0
    while True:
        if counter == 0:
            feedback = input(materials[0]).lower()
            counter += 1

        elif counter == 1:
            feedback = input(materials[1]).lower()
            counter += 1

        else:
            feedback = input(materials[2]).lower()

        keys = {}
        for i in range(materials[4]):
            flag = feedback.find(materials[3][i])
            if not flag == -1:
                keys[flag] = i

        sentinel = -1

        while not len(keys) == 0:
            prior = min(keys.keys())
            flag = keys[prior]
            word_len = len(materials[3][flag])

            sentinel = 0
            suitable_chars = [' ', '.', ',', '!', '(', ')']
            if not prior == 0:
                try:
                    suitable_chars.index(feedback[prior - 1])
                except ValueError:
                    sentinel = -1

            if not len(feedback[prior + word_len: ]) == 0:
                try:
                    suitable_chars.index(feedback[prior + word_len])
                except ValueError:
                    sentinel = -1

            if sentinel == -1:
                keys.pop(prior)
            else:
                break

        if not feedback == "" and sentinel == 0:
            break

    return materials[3][flag]


def category_materials():
    materials = [
        "Categories: Comedy, Sci-Fi, Horror, Romance, Action, Thriller, Drama, Mystery, Crime, Animation, Adventure, Fantasy\n\nChoose a category: ",
        "\nYou can guide me by using one of the categories mentioned above in your answer\n---> ",
        "\nYou can direct me by typing one of the categories specified in your answer or you can close me by typing stop\n---> ",
        ["comedy", "sci-fi", "horror", "romance", "action", "thriller", "drama", "mystery", "crime", "animation", "adventure", "fantasy", "stop"]
    ]
    materials.append(len(materials[3]))

    return materials


def question_materials(main_question):
    materials = [
        main_question,
        "\nYou can guide me by using yes or no in your answer\n---> ",
        "\nYou can direct me by having the words yes or no in your answer or you can close me by typing stop\n---> ",
        ["yes", "no", "stop"]
    ]
    materials.append(len(materials[3]))

    return materials


def get_float(text):
    while True:
        try:
            number = float(input(text))
        except ValueError:
            print("\nInvalid input!\n")
        else:
            return number


def get_int(text):
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print("\nInvalid input!\n")
        else:
            return number


if __name__ == "__main__":
    main()
