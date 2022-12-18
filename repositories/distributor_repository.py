from db.run_sql import run_sql

def save(distributor):
    sql = "INSERT INTO distributors(name) VALUES (%s) RETURNING id"
    values = [distributor.name]
    results = run_sql(sql, values)
    distributor.id = results[0]['id']
    return distributor

def delete_all():
    sql = "DELETE FROM distributors"
    run_sql(sql)