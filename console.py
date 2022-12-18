import pdb

from models.director import Director
from models.film import Film
from models.distributor import Distributor

import repositories.director_repository as director_repository
import repositories.film_repository as film_repository
import repositories.distributor_repository as distributor_repository

director_repository.delete_all()

howard_hawks = Director("Howard Hawks")
director_repository.save(howard_hawks)

warner_home_enertainment = Distributor("Warner Home Entertainment")
distributor_repository.save(warner_home_enertainment)


rio_bravo = Film("Rio Bravo",howard_hawks, warner_home_enertainment, 15, 3, 12)
film_repository.save(rio_bravo)




