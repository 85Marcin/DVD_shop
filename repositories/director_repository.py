from db.run_sql import run_sql

from models.director import Director

def save(director):
    sql = "INSERT INTO directors(name) VALUES ( %s) RETURNING id "
    values = [director.name]
    results = run_sql(sql, values)
    director.id = results [0]['id']
    return director
