# Movie Recommendation Bot

## Description:

Movie Recommendation Bot is an interactive and highly user-friendly Python application designed to offer personalized movie recommendations based on user's preferences. The application interacts with the user in a conversational manner, soliciting their preferences and providing recommendations accordingly. Thus, the program allows the user to discover their next favorite movie in the overwhelming landscape of movie options available today.

Two different programs were created to ensure the integrity of the Project:

### sortmoviedata.py

The `sortmoviedata.py` script reads data from an input CSV file named `IMDB-Movie-Data.csv` obtained from [here](https://data.world/promptcloud/imdb-data-from-2006-to-2016). This CSV file contains details about 1000 movies with columns Rank, Title, Genre, Description, Director, Actors, Year, Runtime (Minutes), Rating, Votes, Revenue (Millions), and Metascore. The script sorts these movies from high to low according to IMDb scores and writes this sorted data into a new file named `IMDB-Sorted-Movie-Data.csv`.

### movierecommendationbot.py

The `movierecommendationbot.py` is the main program that reads from the sorted CSV file `IMDB-Sorted-Movie-Data.csv` to make movie recommendations to the user. The bot first greets the user and then asks if the user would like to specify a movie category and a ranking range on IMDb. The program can handle any genre listed in the dataset, and any IMDb score range between 0 and 10.

The bot offers the user two main options:

1. To get a random movie suggestion from the list of movies that match the specified criteria.
2. To list the movies that match the criteria.

For the second option, if the user has watched some of the listed movies before, the bot can exclude those movies and create a new list. Users can view all the details of a movie by selecting it from the list.

If no criteria are specified, the bot defaults to suggesting movies from any genre and any IMDb score range.

## Technical features of the program:

Design decisions were taken with a focus on user experience, code maintainability, and efficiency. The inclusion of `pyfiglet` and `termcolor` enhances the UI's aesthetic appeal. The `time` module adds a layer of realism to the interaction by controlling the pacing of the application's responses, mimicking the pauses of a real conversation. The `os` module ensures that the screen does not get overcrowded with text by timely clearing the console, maintaining a clean and focused interface. This approach to design not only makes the program more engaging but also helps manage the user's cognitive load.

The modular approach of the codebase promotes easy maintenance, testing, and understanding. Each module can be independently worked upon, thus reducing the complexity and enhancing productivity. Furthermore, this allows for easy scaling and enhancements in the future.

## Possible improvements:

One of the key strengths of this project is its potential for enhancement. The current setup offers a solid base upon which more complex features can be implemented. For instance, integration with a movie database API can provide real-time recommendations. A graphical user interface could be introduced for a richer user experience.

## Video demo:

https://github.com/user-attachments/assets/cb6d182f-db28-46df-8a34-50740c54c0ea

Presentation of the project on YouTube, [Movie Recommendation Bot](https://youtu.be/l5QJs692LSs)
