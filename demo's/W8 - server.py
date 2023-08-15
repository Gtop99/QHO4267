import matplotlib.pyplot as plt

def coffee_sleep(n=5):
    coffee = []
    sleep = []
    for i in range(n):
        coffee.append(int(input("Enter amount of coffee you drink per week: ")))
        sleep.append(int(input("Enter average sleep duration per night: ")))
    return coffee, sleep


#print(coffee_sleep())

def movies(n=5):
    movie = {}
    for i in range(n):
        genre = input("Enter your favourite movie genre: ")
        movie[genre] = movie.get(genre, 0) + 1
    return movie

print(movies(2))


