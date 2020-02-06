#User Input for signing in or signing up
options = int(input("Hello!, this is the homepage. Enter 1 to sign in or Enter 2 to sign up!"))


#Making a database to store the user's details
import sqlite3,os

if not os.path.isfile("Details.db"):

    Details = sqlite3.connect("Details.db")
    c=Details.cursor()

    c.execute('''CREATE TABLE Details
    (username text,
    password text,
    first_name text,
    last_name text,
    address text,
    DoB text,
    gender text)
    ''')

    Details.commit()
    Details.close()

#Making a database to store the user's liked movies
import sqlite3,os

if not os.path.isfile("Liked.db"):

    Liked = sqlite3.connect("Liked.db")
    c=Liked.cursor()

    c.execute('''CREATE TABLE Liked
    (username text,
    movie1 text,
    movie2 text,
    movie3 text,
    movie4 text)
    ''')

    Liked.commit()
    Liked.close()

#Making a procedure to input the user's movies and give recommendations
def movie_data_collection():
    print("As you are a new user, we would like to know some of your past viewing history so that we can recommend you relevant films. When you are ready, please press enter")
    input()
        

    #Requesting for the user's 10 previous movies
    print("Please enter the last 10 films, you've watched")

    first_movie = input("1)")
    second_movie = input("2)")
    third_movie = input("3)")
    fourth_movie = input("4)")
    fifth_movie = input("5)")
    sixth_movie = input("6)")
    seventh_movie = input("7)")
    eigth_movie = input("8)")
    nineth_movie = input("9)")
    tenth_movie = input("10)")

    #Making a databse to store the movies
    import sqlite3,os

    if not os.path.isfile("ViewingHistory.db"):

        ViewingHistory = sqlite3.connect("ViewingHistory.db")
        c=ViewingHistory.cursor()

        c.execute('''CREATE TABLE ViewingHistory
        (username text,
        first_movie text,
        second_movie text,
        third_movie text,
        fourth_movie text,
        fifth_movie text,
        sixth_movie text,
        seventh_movie text,
        eigth_movie text,
        nineth_movie text,
        tenth_movie text)
        ''')

        ViewingHistory.commit()
        ViewingHistory.close()

    #Inserting values into the database
    if os.path.isfile("ViewingHistory.db"):

        ViewingHistory = sqlite3.connect("ViewingHistory.db")
        c=ViewingHistory.cursor()
        c.execute('''INSERT INTO ViewingHistory
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (username, first_movie, second_movie, third_movie, fourth_movie, fifth_movie, sixth_movie, seventh_movie, eigth_movie, nineth_movie, tenth_movie))

        ViewingHistory.commit()
        ViewingHistory.close()

    recommendations()

def recommendations():
    #Movies of 3 different genres
    comedy_movies = ['Shaun of the dead', 'Airplane!', 'Superbad', 'Central Intelligence', 'Ghostbusters', 'Hot Fuzz', 'Bridesmaids', 'Stepbrothers', 'Office Space', 'Duck Soup']
    action_movies = ['Fast and Furious', 'Mad Max: Fury Road', 'Die hard', 'The Matrix', 'Aliens', 'Mission Impossible', 'Heat', 'Total Recall', 'Predator', 'John Wick']
    horror_movies = ['IT Chapter Two', 'Midsommar', 'Us', 'Ready or Not', 'Eli', 'Annabelle Comes Home', 'A Quiet Place', 'Halloween', 'The Nun', 'Get out']

    #user input to find the genre of their recent genre viewings
    comedy_preference = int(input("Of the last 10 films you've watched, how many of them are comedy genre-based films"))
    action_preference = int(input("Of the last 10 films you've watched, how many of them are action genre-based films"))
    horror_preference = int(input("Of the last 10 films you've watched, how many of them are horror genre-based films"))

    import random

    #Outcomes based on the users previous viewings and therefore outputting recommendations
    if comedy_preference > action_preference and comedy_preference > horror_preference:

        print("We have understood that comedy is your favourite genre of film and therefore would like to recommend you a couple of comedy films")
        print("Comedy films we would like to recommend you are:")

        print(random.sample(comedy_movies, 3))

        if action_preference > horror_preference:
            print("We would also like to recommend you some action films as they seem to be one of your preferences")
            print(random.sample(action_movies, 2))

        elif action_preference < horror_preference:
            print("We would also like to recommend you some horror films as they seem to be one of your preferences")
            print(random.sample(horror_movies, 2))

        elif action_preference == horror_preference:
            print("We would  also like to recommend a film from horror and a film from action as you seem to have an equal connection with both of them")
            print("A horror film we would like to recommend is", random.sample(horror_movies, 1))
            print("An action film we would like to recommend is", random.sample(action_movies, 1))

    if action_preference > comedy_preference and action_preference > horror_preference:

        print("We have understood that action is your favourite genre of film and therefore would like to recommend you a couple of action films")
        print("Action films we would like to recommend you are:")

        print(random.sample(action_movies, 3))

        if comedy_preference > horror_preference:
            print("We would also like to recommend you some comedy films as they seem to be one of your preferences")
            print(random.sample(comedy_movies, 2))

        elif comedy_preference < horror_preference:
            print("We would also like to recommend you some horror films as they seem to be one of your preferences")
            print(random.sample(horror_movies, 2))

        elif comedy_preference == horror_preference:
            print("We would also like to recommend a film from horror and a film from comedy as you seem to have an equal connection with both of them")
            print("A horror film we would like to recommend is", random.sample(horror_movies, 1))
            print("A comedy film we would like to recommend is", random.sample(comedy_movies, 1))


    if horror_preference > action_preference and horror_preference > comedy_preference:

        print("We have understood that horror is your favourite genre of film and therefore would like to recommend you a couple of horror films")
        print("Horror films we would like to recommend you are:")

        print("Here are some horror recommendations")

        print(random.sample(horror_movies, 3))

        if action_preference > comedy_preference:
            print("We would also like to recommend you some action films as they seem to be one of your preferences")
            print(random.sample(action_movies, 2))

        elif action_preference < comedy_preference:
            print("We would also like to recommend you some comedy films as they seem to be one of your preferences")
            print(random.sample(comedy_movies, 2))

        elif action_preference == comedy_preference:
            print("We would  a film from comedy and a film from action as you seem to have an equal connection with both of them")
            print("A comedy film we would like to recommend is", random.sample(comedy_movies, 1))
            print("An action film we would like to recommend is", random.sample(action_movies, 1))

            
    if comedy_preference == action_preference and comedy_preference > horror_preference:
        print("We have understood that comedy and action are equally your favourite film genre")
        print("We would like to recommend you 2 movies from comedy and 3 movies from action")

        print("Comedy recommendations:")
        print(random.sample(comedy_movies, 2))

        print("Action recommendations:")
        print(random.sample(action_movies, 3))

        
    elif comedy_preference == horror_preference and comedy_preference > action_preference:
        print("We have understood that comedy and horror are equally your favourite film genre")
        print("We would like to recommend you 3 movies from comedy and 2 movies from horror")

        print("Comedy recommendations:")
        print(random.sample(comedy_movies, 3))

        print("Horror recommendations:")
        print(random.sample(horror_movies, 2))

    elif horror_preference == action_preference and horror_preference > comedy_preference:
        print("We have understood that horror and action are equally your favourite film genre")
        print("We would like to recommend you 3 movies from horror and 2 movies from action")

        print("Horror recommendations:")
        print(random.sample(horror_movies, 3))

        print("Action recommendations:")
        print(random.sample(action_movies, 2))

#Procedure of the home menu when a user logins in
def menu():
    while options == 1 or 2:
        
        print("*************************************************HOMEPAGE*************************************************")
        #User home menu options
        print("Enter 1, to see the last 10 movies you've watched \nEnter 2, to add movies to your 'FAVOURITES/LIKED' folder")
        print("Enter 3, to view your 'FAVOURITE/LIKED' folder \nEnter 4, to update your 'FAVOURITE/LIKED' folder")
        print("Enter 5, to view movie recommendations \nEnter 6, to choose additoinal vieiwng preferences other than 'genre'")
        print("Enter 7, to log out")
        HomeMenu = int(input())

        #If input = 1, output of their 10 previous viewings from the database
        if HomeMenu == 1:
            import sqlite3
            
            ViewingHistory = sqlite3.connect("ViewingHistory.db")
            c=ViewingHistory.cursor()

            c.execute('''SELECT * FROM ViewingHistory WHERE username = ? ''', (username,))
            row = c.fetchall()

            print(row)
            input()

            ViewingHistory.commit()
            ViewingHistory.close()
            continue

        #If input = 2, input of liked movies and stores them in a database
        if HomeMenu == 2:
            import sqlite3 as lite
            import sys

            con = lite.connect('Liked.db')

            cur = con.cursor()   
            cur.execute("select username from Liked where username=?", (username,))
            data = cur.fetchall()
            if not data:
                print("You can add 4 movies to your liked folder")
                movie1 = input("1)")
                movie2 = input("2)")
                movie3 = input("3)")
                movie4 = input("4)")

                import sqlite3, os
                if os.path.isfile("Liked.db"):

                    Liked = sqlite3.connect("Liked.db")
                    c=Liked.cursor()
                    c.execute('''INSERT INTO Liked
                    VALUES (?, ?, ?, ?, ?)''', (username, movie1, movie2, movie3, movie4))

                    Liked.commit()
                    Liked.close()

                    print("Movies added to liked folder")
                
            else:
                print("Your FAVOURITES/LIKED  folder is already full, however you can update it in the HomeMenu by enterning 4")
            continue
            

        #If input = 3, output of the liked movies database
        if HomeMenu == 3:
            import sqlite3, os
            Liked = sqlite3.connect("Liked.db")
            c=Liked.cursor()

            c.execute('''SELECT * FROM Liked WHERE username = ? ''', (username,))
            row = c.fetchall()

            print(row)
            input()

            Liked.commit()
            Liked.close()
            continue

        #If input = 4, the user can update their like folder
        if HomeMenu == 4:
            import sqlite3
            #User input
            print("You can update the 4 movies in your liked folder")
            new_movie1 = input("1)")
            new_movie2 = input("2)")
            new_movie3 = input("3)")
            new_movie4 = input("4)")

            Liked = sqlite3.connect("Liked.db")
            c=Liked.cursor()

            #Inserting the values into the database
            c.execute('''UPDATE Liked SET movie1 = ? WHERE username = ? ''',(new_movie1, username,))
            c.execute('''UPDATE Liked SET movie2 = ? WHERE username = ? ''',(new_movie2, username,))
            c.execute('''UPDATE Liked SET movie3 = ? WHERE username = ? ''',(new_movie3, username,))
            c.execute('''UPDATE Liked SET movie4 = ? WHERE username = ? ''',(new_movie4, username,))
                            
            Liked.commit()
            Liked.close()
            continue

        
        if HomeMenu == 5:
            recommendations()
            continue

        #inputting movie information into a databse
        if HomeMenu == 6:

            #Creating the database and enterring data into it
            import sqlite3, os

            if not os.path.isfile("Movies.db"):
                Movies = sqlite3.connect("Movies.db")
                c=Movies.cursor()

                c.execute('''CREATE TABLE Movies
                (Name text,
                IMDB float,
                Starring_actor text,
                Release_date int,
                Length int)
                ''')
                
                c.execute('''INSERT INTO Movies
                VALUES ("Titanic", 7.8, "Leonardo Dicaprio", 1997, 195)''')

                c.execute('''INSERT INTO Movies
                VALUES ("The Godfather", 9.2, "Al Pacino", 1972, 178)''')

                c.execute('''INSERT INTO Movies
                VALUES ("Inception", 8.8, "Leonardo Dicaprio", 2010, 148)''')

                c.execute('''INSERT INTO Movies
                VALUES ("Fate of the Furious", 6.7, "Vin Diesel", 2017, 149)''')

                c.execute('''INSERT INTO Movies
                VALUES ("Ride Along", 6.2, "Kevin Hart", 2014, 100)''')

                c.execute('''INSERT INTO Movies
                VALUES ("21 Jump Street", 7.2, "Ice Cube", 2012, 110)''')

                c.execute('''INSERT INTO Movies
                VALUES ("Riddick", 6.4, "Vin Diesel", 2013, 119)''')

                c.execute('''INSERT INTO Movies
                VALUES ("Straight Outta Compton", 7.9, "Ice Cube", 2015, 167)''')

                c.execute('''INSERT INTO Movies
                VALUES ("Central Intelligence", 6.3, "Kevin Hart", 2016, 56)''')
                
                Movies.commit()
                Movies.close()
            
            print("To find movies based on the following: \nEnter 1, for 'IMDB RATING' \nEnter 2, for starring actors \nEnter 3, for release date \nEnter 4, for length of the film(mins)")
            user_filter = int(input())

            #The IMDB rating will be searched in the database and movies with higher imdb ratings will be outputted
            if user_filter == 1:
                IMDB_filter = float(input("What is the minimun IMDB RATING of movies do you want to use"))

                Movies = sqlite3.connect("Movies.db")
                c=Movies.cursor()

                c.execute('''SELECT Name FROM Movies WHERE IMDB >= ? ''', (IMDB_filter,))
                row = c.fetchall()

                print("Movies with an IMDB of atleast", IMDB_filter,":")
                print(row)
                input()

                Movies.commit()
                Movies.close()
            #Each actor will be searched through the database and their movies will be outputted
            elif user_filter == 2:
                print("Of the following actors, please type in the actor you like to see the movies in that they star in")
                print("Leonardo Dicaprio")
                print("Al Pacino")
                print("Kevin Hart")
                print("Ice Cube")
                print("Vin Diesel")
                actors_filter = input()

                Movies = sqlite3.connect("Movies.db")
                c=Movies.cursor()

                c.execute('''SELECT Name FROM Movies WHERE Starring_actor = ? ''', (actors_filter,))
                row = c.fetchall()

                print("Movies that", actors_filter,"stars in:")
                print(row)
                input()

                Movies.commit()
                Movies.close()       
            # Year release is searched through the database and movies that are newer than the inputted year will be outputted
            elif user_filter == 3:
                releaseDATE_filter = int(input("What is the earliest year release you would like to see movies from, e.g. 2005"))

                Movies = sqlite3.connect("Movies.db")
                c=Movies.cursor()

                c.execute('''SELECT Name FROM Movies WHERE Release_date >= ? ''', (releaseDATE_filter,))
                row = c.fetchall()

                print("Movies made from", releaseDATE_filter,":")
                print(row)
                input()

                Movies.commit()
                Movies.close()
            #Length of movie will be inputted and movies with a shorter length of time will be outputted
            elif user_filter == 4:
                length_filter = int(input("What is the maximum length of movies in minutes would you like to see"))

                Movies = sqlite3.connect("Movies.db")
                c=Movies.cursor()

                c.execute('''SELECT Name FROM Movies WHERE Length <= ? ''', (length_filter,))
                row = c.fetchall()

                print("Movies that are no longer than", length_filter, "minutes:")
                print(row)
                input()

                Movies.commit()
                Movies.close()
            continue
        
        if HomeMenu == 7:
            print("Thank you for using our service, we look forward to seeing you next time")
            break

            
            
         
#If the user has decided to sign up
if options == 2:
    while options == 2:
        #user input for username
        username = input("Please enter a username")

        import sqlite3 as lite
        import sys

        con = lite.connect('Details.db')
        ID_check = username

        cur = con.cursor()   
        cur.execute("select username from Details where username=?", (ID_check,))
        data = cur.fetchall()
        if not data:
            print('Username is available')
            break
        else:
            print('Username is unavailable')
            continue


    #Creation of while loop
    while options == 2:
        #User input of password
        password1 = input("Please enter a password, your password must meet the following requirements:\nContain atleast 5 chatacters \nContain 1 upper case letter \nContain atleast 1 number")

        #Checking if password meets requirements
        if (any(x.isupper() for x in password1) and any(x.isdigit() for x in password1) and len(password1) >= 5):
            password2 = input("Please re-enter your password")
            
        #If password doesnt fit the requirements, the loop will repeat    
        #elif (any(x.isupper() for x in password1) or any(x.isdigit() for x in password1) or len(password1) <= 5):
         #   print("Sorry, your password does not fit the requirements, please try again.")
          #  continue
        else:
            print("Sorry, your password does not fit the requirements, please try again.")
            continue

        #Checking if the two passwords match, outputing whether they are the same
        if password1 == password2:
            print("Well done, sign up is complete")
            print("Your username is", username)
            print("Your password is", password1)
            break

        #Checking if the two passwords matchs, outputing whether they arent the same
        else:
            print("Sorry, passwords dont match")
            continue

    #User details#
    first_name = input("Please enter your first name")
    last_name = input("Please enter your last name")
    address = input("Please enter your address")
    DoB = input("Please enter your date of birth in the format DD/MM/YYYY")
    gender = input("Please enter your gender")
    

    #Import of sqlite
    import sqlite3,os

    #Creating a database if one isnt already existing
    if not os.path.isfile("Details.db"):

        #Connecting the database to sqlite
        Details = sqlite3.connect("Details.db")
        c=Details.cursor()

        #Creating a table called
        c.execute('''CREATE TABLE Details
        (username text,
        password text,
        first_name text,
        last_name text,
        address text,
        DoB text,
        gender text)
        ''')
        Details.commit()
        Details.close()

    #Inserting the variables into the database
    if os.path.isfile("Details.db"):

        Details = sqlite3.connect("Details.db")
        c=Details.cursor()
        c.execute('''INSERT INTO Details
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (username, password1, first_name, last_name, address, DoB, gender))
 
        Details.commit()
        Details.close()

    movie_data_collection()
    print("You will now be directed to the HomePage")
    menu()

#If the user has decided to log in
if options == 1:
    while options == 1:

        #User input of their username
        username = input("Please enter your username")

        #Checking if the username exists in the database
        import sqlite3 as lite
        import sys

        con = lite.connect('Details.db')
        ID_check = username

        cur = con.cursor()
        cur.execute("select username from Details where username=?", (ID_check,))
        data = cur.fetchall()

        #If the username doesn't exist then the loop will restart
        if not data:
            print("This username doesn't exist, please try again")
            continue

        #If the username does exist, they will be asked for their password
        else:
            while options == 1:
                #User input for their password
                password_check = input("Please enter your password")

                #Checking whether the password exists in the databse
                import sqlite3 as lite
                import sys

                con = lite.connect('Details.db')
                ID_check = password_check

                cur = con.cursor()
                cur.execute("select password from Details where password=?", (ID_check,))
                data = cur.fetchall()

                #If the password is incorrect then the sub loop will repeat itself
                if not data:
                    print ("Incorrect password")
                    continue

                #If the password is correct then access is granted and the loop is ended
                else:
                    print("Access granted")
                    print("Welcome back" ,username)
                    break
        #Breaking the whole loop
        break
    menu()






























