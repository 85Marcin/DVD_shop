import pdb

from models.director import Director

import repositories.director_repository as director_repository



director_repository.delete_all()

howard_hawks = Director("Howard Hawks")
director_repository.save(howard_hawks)

director_repository.select_all()


