from .fake_employees import create_fake_employees


class DBManager:
    def __init__(self, client, database, collection):
        self.client = client
        self.db = self.client[database]
        self.coll = self.db[collection]

    # ----- EMPLOYEES ----- #

    def get_employee_directory(self):  # DONE
        return self.coll.find({})

    def get_employee_by_empid(self, empid):  # DONE
        return self.coll.find({'empid': empid})

    def post_new_employee(self, employee):
        # Add next empid from database to new employee
        employee.update({'empid': self.retrieve_next_empid()})
        result = self.coll.insert_one(employee)
        _id = result.inserted_id
        return self.coll.find({'_id': _id})

    def put_update_employee_by_empid(self, empid, **updated_kwargs):
        query = {'empid': empid}
        update_data = {'$set': {**updated_kwargs}}
        self.coll.update_one(query, update_data)

    def delete_employee_by_empid(self, empid):
        self.coll.delete_one({'empid': empid})

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

    def get_aggregated_roles(self):
        return self.coll.aggregate([{'$group': {'_id': '$role', 'emps': {'$sum': 1}}}])

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

    def get_aggregated_departments(self):
        return self.coll.aggregate(
            [{'$group': {'_id': '$department', 'emps': {'$sum': 1}}}]
        )

    # ----- MISC ----- #

    def retrieve_next_empid(self):
        try:
            last_emp_doc = list(self.coll.find({}, {'empid'}).sort('empid', -1).limit(1))
            last_id = last_emp_doc[0]['empid']
            new_id = last_id + 1
            return new_id
        except IndexError:
            return 1

    def insert_test_values(self, qty):  # DONE
        '''Only for testing of database'''
        fakes = create_fake_employees(qty)
        next_emp_id = self.retrieve_next_empid()
        for employee in fakes:
            employee.update({'empid': next_emp_id})
            next_emp_id += 1
        self.coll.insert_many(fakes)

    def generic_update(self, field, id, **updated_kwargs):
        query = {field: id}
        update_data = {'$set': {**updated_kwargs}}
        self.coll.update_one(query, update_data)

    def _delete_all(self):
        '''ONLY for testing of database!!'''
        self.coll.delete_many({})
