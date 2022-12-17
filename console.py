import pdb

from models.director import Director

import repositories.director_repository as director_repository



howard_hawks = Director("Howard Hawks")
director_repository.save(howard_hawks)

