import csv

def main():
    movie_list = []

    with open("IMDB-Movie-Data.csv") as infile:
        reader = csv.DictReader(infile)

        for movie in reader:
            movie_list.append(movie)

    movie_list.sort(reverse=True, key=ratings)

    with open("IMDB-Sorted-Movie-Data.csv", 'w', newline='') as outfile:
        titles = ["Rank", "Title", "Genre", "Description", "Director", "Actors", "Year", "Runtime (Minutes)", "Rating", "Votes", "Revenue (Millions)", "Metascore"]
        writer = csv.DictWriter(outfile, fieldnames=titles)

        writer.writeheader()

        for i in range(len(movie_list)):
            writer.writerow(movie_list[i])

def ratings(e):
    return e["Rating"]

main()