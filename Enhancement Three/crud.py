from pymongo import MongoClient


class AnimalRescue:
    """
    CRUD operations for Animal collection in MongoDB with RBAC.
    """

    def __init__(self, username, password, host="127.0.0.1", port=27017, database="AnimalDB", collection="Animals"):
        """
        initialize the MongoDB connection with authentication.
        """
        try:
            # connect to MongoDB with username and password
            uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=AnimalDB"
            self.client = MongoClient(uri)
            self.database = self.client[database]
            self.collection = self.database[collection]
            print(f"Connected to MongoDB database '{database}' and collection '{collection}'.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    @staticmethod
    def check_permissions(role, operation):
        """
        check if a given role is allowed to perform an operation.
        """
        permissions = {
            "dataViewer": ["read"],
            "dataManager": ["create", "read", "update", "delete"]
        }
        return operation in permissions.get(role, [])

    def create(self, data, role):
        """
        insert a single document into the collection.
        """
        if not self.check_permissions(role, "create"):
            raise PermissionError("You do not have permission to perform this operation.")
        try:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False

    def read(self, query, role):
        """
        retrieve documents matching the query.
        """
        if not self.check_permissions(role, "read"):
            raise PermissionError("You do not have permission to perform this operation.")
        try:
            return list(self.collection.find(query))
        except Exception as e:
            print(f"Error reading documents: {e}")
            return []

    def update(self, query, update_data, role):
        """
        update a document matching the query.
        """
        if not self.check_permissions(role, "update"):
            raise PermissionError("You do not have permission to perform this operation.")
        try:
            result = self.collection.update_one(query, {"$set": update_data})
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating document: {e}")
            return False

    def delete(self, query, role):
        """
        delete a document matching the query.
        """
        if not self.check_permissions(role, "delete"):
            raise PermissionError("You do not have permission to perform this operation.")
        try:
            result = self.collection.delete_one(query)
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting document: {e}")
            return False
