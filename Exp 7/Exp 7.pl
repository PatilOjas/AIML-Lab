city(C) :-
% there are 5 cities
length(C, 5),
    
% city names
member(h('Last Stand', _, _), C),
member(h('Mile City', _, _), C),
member(h('New Town', _, _), C),
member(h('Olliopolis', _, _), C),
member(h('Polberg', _, _), C),

% city areas
member(h(_, mountains, _), C),
member(h(_, forest, _), C),
member(h(_, coast, _), C),
member(h(_, desert, _), C),
member(h(_, valley, _), C),
    
% rainfall amounts
member(h(_, _, 12), C),
member(h(_, _, 27), C),
member(h(_, _, 32), C),
member(h(_, _, 44), C),
member(h(_, _, 65), C),

% Hints
% The city in the desert got the least rain; 
% the city in the forest got the most rain.
member(h(_, desert, 12), C),
member(h(_, forest, 65), C),

% New Town is in the mountains.
member(h('New Town', mountains, _), C),

% Last Stand got more rain than Olliopolis.
member(h('Last Stand', _, A), C),
member(h('Olliopolis', _, B), C),
A > B,

% Mile City got more rain than Polberg, but less rain than New Town.
member(h('Mile City', _, D), C),
member(h('Polberg', _, E), C),
D > E,
member(h('New Town', _, F), C),
F > D,
    
% Olliopolis got 44 inches of rain.
member(h('Olliopolis', _, 44), C),

% The city in the mountains got 32 inches of rain; the
% city on the coast got 27 inches of rain.
member(h(_, mountains, 32), C),
member(h(_, coast, 27), C).

query_rain_amount(City_Name, Rainfall_Amount) :-
city(C),
member(h(City_Name, _, Rainfall_Amount), C),
write(City_Name), write(" received "),
write(Rainfall_Amount), write(" inches of rain."),
nl.


query_city_region(City_Name, Region) :-
city(C),
member(h(City_Name, Region, _), C),
write(City_Name), write(" is located in the "),
write(Region), nl.