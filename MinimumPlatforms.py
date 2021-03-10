"""
Given arrival and departure times of all trains that reach a railway station.
Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day.
Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other.
At any given instance of time, same platform can not be used for both departure of a train and arrival of another train.
In such cases, we need different platforms,
"""


# Time Complexity O (n + nlogn)
def minimumPlatform(arrival, departure, n):
    platform = 1
    required_platform = 1
    arrival.sort
    departure.sort
    x = 1
    y = 0
    # Iterating in both array
    while (x < n and y < n):
        if arrival[x] <= departure[y]:
            platform += 1
            x += 1
        elif arrival[x] > departure[y]:
            platform -= 1
            y += 1
        if platform > required_platform:
            required_platform = platform
    return required_platform


n = 6
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print("Platform Required is ===> ", minimumPlatform(arrival, departure, 6))

"""
Output:
Platform Required is ===>  3
"""
