movies={
    "Sisu":9.8,
    "Gamers":3.8,
    
}

def add_movies():
    name=input("enter movie name: ")
    rating=float(input("enter movie rating: "))
    movies[name]=rating
    print("Movies added succefully")

def show_movies():
    if not movies:
        print("no movies available yet")
    else:
        for movie, rating in movies.items():
            print(movie,";",rating)

def highest_rating():
    if not movies:
        print("no movies available yet")
    else:
        highest=max(movies,key=movies.get)
        print(movies[highest])
def average_rating():
    average=sum(movies.values())/len(movies)

    print(average)
add_movies()
show_movies()
highest_rating()
average_rating()