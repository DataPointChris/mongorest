from .fake_employees import create_fake_employees


class DBManager:
    def __init__(self, client, database, collection):
        self.client = client
        self.db = self.client[database]
        self.coll = self.db[collection]

    def insert_test_values(self, qty): # DONE
        self.coll.insert_many(create_fake_employees(qty))

    def get_employee_list(self): # DONE
        return self.coll.find({})

    def get_employee_id(self, id): # DONE
        return self.coll.find({'id': id})

    def get_role_list(self): # DONE
        return self.coll.distinct('role')

    def get_role_employees(self, name):
        return self.coll.find({'role': name})

    def get_department_list(self): # DONE
        return self.coll.distinct('department')

    def get_roles_by_department(self, name): # DONE
        roledict = self.coll.find({'department': name}, {'_id': 0, 'role': 1})
        roles = [d.get('role')  for d in roledict]
        return roles

    def get_department_employees(self, name): # DONE
        peepdict = self.coll.find({'department': name}, {'_id': 0, 'firstname': 1, 'lastname': 1})
        people = [(f'{d.get("firstname")} {d.get("lastname")}') for d in peepdict]
        return people

    def insert(self, project, task, description):
        self.coll.insert_one(
            {'project': project, 'task': task, 'description': description}
        )

    def update(self, id, project, task, description):
        query = {'_id': id}
        update_data = {
            '$set': {'project': project, 'task': task, 'description': description}
        }
        self.coll.update_one(query, update_data)

    def delete(self, id):
        self.coll.delete_one({'_id': id})

    def delete_all(self):
        self.coll.delete_many({})
