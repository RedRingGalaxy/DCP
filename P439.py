# Problem Statement [Medium] O(n(n+1)/2)
'''
Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting  airport, compute the preson's
itinerary. If no such itinerary exists, return null. If there are multiple
possible  itinerarys, return lexicographically smallest one. All flights
must be used in itinerary.

Ex-1: Flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
    and starting aireport  'YUL'.
    Output:= ['YUL','YYZ','SFO','HKO','ORD']

Ex-2: Flights = [(SFO,COM), (COM, YYZ)] and  Starting airport COM
    Output:= null

Ex-3: Flights = [(A,B),(A,C),(B,C),(C,A)] and Starting ariport A,
    Output:=[A,B,C,A,C] even though [A,C,A,B,C] is also valid itinerary.
    However, first is the smallest one.

'''
# TODO: Return lexicographically smallest route of flights
def find_shortest_route(flights,airport) -> list:
    temp_flights = flights.copy()
    path = [airport]

    next_flgt = ''

    for i in flights:
        if i[0] == airport and (next_flgt == '' or next_flgt > i[1]):
            next_flgt = i[1]
            
    path.append(next_flgt)

    #print(path)

    temp_flights.remove((airport,next_flgt))
    airport = next_flgt
    next_flgt = ''

    #print(temp_flights)

    while len(temp_flights) > 0:
        for i in temp_flights:
            if i[0] == airport and (next_flgt == '' or next_flgt > i[1]):
                next_flgt = i[1]

        if next_flgt != '':        
            path.append(next_flgt)
            temp_flights.remove((airport,next_flgt))
            airport = next_flgt
            next_flgt = ''
        else:
            break

    return path if len(temp_flights) == 0 else None


        


if __name__ == "__main__":
    flights1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    airport1 = 'YUL'

    flights2 = [('A','C'),('A','B'),('B','C'),('C','A')]
    airport2 = 'A'

    flights3 = [('SFO', 'COM'), ('COM', 'YYZ')]
    airport3 = 'COM'

    print(find_shortest_route(flights1,airport1))
    print(find_shortest_route(flights2,airport2))
    print(find_shortest_route(flights3,airport3))
