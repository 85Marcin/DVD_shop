import pdb

from models.director import Director
from models.film import Film
from models.distributor import Distributor

import repositories.director_repository as director_repository
import repositories.film_repository as film_repository
import repositories.distributor_repository as distributor_repository

director_repository.delete_all()
distributor_repository.delete_all()
film_repository.delete_all()

howard_hawks = Director("Howard Hawks")
director_repository.save(howard_hawks)
david_lnych = Director("David Lynch")
director_repository.save(david_lnych)
john_ford = Director("John Ford")
director_repository.save(john_ford)
alfred_hitchcock = Director("Alfred Hitchcock")
director_repository.save(alfred_hitchcock)

warner_home_enertainment = Distributor("Warner Home Entertainment")
distributor_repository.save(warner_home_enertainment)
high_fliers_films = Distributor("High Fliers Films")
distributor_repository.save(high_fliers_films)

rio_bravo = Film("Rio Bravo", "western", howard_hawks, warner_home_enertainment, 0, 3, 11)
film_repository.save(rio_bravo)
blue_velvet = Film("Blue Velvet","thriller", david_lnych, high_fliers_films, 3, 4, 12)
film_repository.save(blue_velvet)
stagecoach =Film("Stagecoach", "western", john_ford, high_fliers_films, 6, 2, 5)
film_repository.save(stagecoach)
psycho = Film("Psycho", "horror", alfred_hitchcock, warner_home_enertainment, 5, 6, 13 )
film_repository.save(psycho)


big_sleep = Film("Big Sleep", "film noir", howard_hawks, warner_home_enertainment, 9, 3,14)
film_repository.save(big_sleep)











