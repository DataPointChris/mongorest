import junkinserts


class DBManager:
    def __init__(self, client, database, collection):
        self.client = client
        self.db = self.client[database]
        self.coll = self.db[collection]

    def create_table(self):
        pass

    def insert_test(self):
        self.coll.insert_many(junkinserts.mongo_insertions)

    def get_all(self):
        return self.coll.find({})

    def get_by_id(self, id):
        return self.coll.find({'id': id})

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

    def get_projects(self):
        self.coll.distinct('project')
