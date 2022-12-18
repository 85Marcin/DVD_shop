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

warner_home_enertainment = Distributor("Warner Home Entertainment")
distributor_repository.save(warner_home_enertainment)
high_fliers_films = Distributor("High Fliers Films")
distributor_repository.save(high_fliers_films)

rio_bravo = Film("Rio Bravo",howard_hawks, warner_home_enertainment, 0, 3, 11)
film_repository.save(rio_bravo)
blue_velvet = Film("Blue Velvet", david_lnych, high_fliers_films, 3, 4, 12)
film_repository.save(blue_velvet)


big_sleep = Film("Big Sleep", howard_hawks, warner_home_enertainment, 9, 3,14)
film_repository.save(big_sleep)









