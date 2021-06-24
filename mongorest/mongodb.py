from .fake_employees import create_fake_employees


class DBManager:
    def __init__(self, client, database, collection):
        self.client = client
        self.db = self.client[database]
        self.coll = self.db[collection]

    # ----- EMPLOYEES ----- #

    def get_employee_directory(self):  # DONE
        return self.coll.find({})

    def get_employee_by_id(self, id):  # DONE
        return self.coll.find({'id': id})

    def post_new_employee(self, employee):
        self.coll.insert_one(employee)

    def put_update_employee_by_id(self, id, **updated_kwargs):
        query = {'id': id}
        update_data = {'$set': {**updated_kwargs}}
        self.coll.update_one(query, update_data)

    def delete_employee_by_id(self, id):
        self.coll.delete_one({'id': id})

    # ----- ROLES ----- #

    def get_role_list(self):  # DONE
        return self.coll.distinct('role')

    def put_edit_role_by_name(self, role, updated):
        query = {'role': role}
        updates = updated.get('updates')
        update_data = {'$set': {**updates}}
        self.coll.update_many(query, update_data)

    def get_employees_by_role(self, role):  # DONE
        return self.coll.find({'role': role})

    def get_departments_with_role(self, role):
        deptdict = self.coll.find({'role': role}, {'_id': 0, 'department': 1})
        depts = [d.get('department') for d in deptdict]
        return depts

    # ----- DEPARTMENTS ----- #

    def get_department_list(self):  # DONE
        return self.coll.distinct('department')

    def put_edit_department_by_name(self, name, updated):
        query = {'name': name}
        updates = updated.get('updates')
        update_data = {'$set': {**updates}}
        self.coll.update_many(query, update_data)

    def get_employees_in_department(self, dept):
        return self.coll.find({'department': dept})

    def get_roles_by_department(self, dept):  # DONE
        roledict = self.coll.find({'department': dept}, {'_id': 0, 'role': 1})
        roles = [d.get('role') for d in roledict]
        return roles

    # ----- MISC ----- #

    def insert_test_values(self, qty):  # DONE
        '''Only for testing of database'''
        self.coll.insert_many(create_fake_employees(qty))

    def generic_update(self, field, id, **updated_kwargs):
        query = {field: id}
        update_data = {'$set': {**updated_kwargs}}
        self.coll.update_one(query, update_data)

    def delete_all(self):
        '''ONLY for testing of database!!'''
        self.coll.delete_many({})
