from db.run_sql import run_sql

from models.distributor import Distributor

def save(distributor):
    sql = "INSERT INTO distributors(name) VALUES (%s) RETURNING id"
    values = [distributor.name]
    results = run_sql(sql, values)
    distributor.id = results[0]['id']
    return distributor

def delete_all():
    sql = "DELETE FROM distributors"
    run_sql(sql)

def select(id):
    distributor = None
    sql = "SELECT * FROM distributors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        distributor = Distributor(result['name'], result['id'] )
    return distributor

def select_all():
    distributors = []
    sql = "SELECT * FROM distributors"
    results = run_sql(sql)

    for row in results:
        distributor = Distributor(row['name'], row['id'])
        distributors.append(distributor)
    return distributors




