import pymongo
from bson.objectid import ObjectId
from .plugins import mongo
from .exceptions import ObjectAlreadyExists, ObjectNotFound


class Database:
    def __init__(self, collection_name):
        self.collection_name = collection_name

    @property
    def collection(self):
        return getattr(mongo.db, self.collection_name)

    def uid(self, object_uid):
        if not isinstance(object_uid, ObjectId):
            object_uid = ObjectId(object_uid)
        return object_uid

    def get(self, filters):
        item = self.collection.find_one(filters)
        if item is None:
            raise ObjectNotFound(error="%s with criterias '%s' not found"%(self.collection_name, filters))
        return item

    def get_by_uid(self, object_uid):
        item = self.collection.find_one({"_id": self.uid(object_uid)})
        if item is None:
            raise ObjectNotFound(error="%s with uid '%s' not found"%(self.collection_name, object_uid))
        return item

    def search(self, filters=None):
        if filters is None:
            filters = {}
        return [item for item in self.collection.find(filters)]

    def create(self, pydantic_object):
        try:
            # TODO: Add unique constraint on table and handle duplicates error
            operation = self.collection.insert_one(pydantic_object.dict(exclude={"_id"}))
            return self.get_by_uid(operation.inserted_id)
        except pymongo.errors.DuplicateKeyError as e:
            raise ObjectAlreadyExists(
                error="%s already exists."%self.collection_name,
                cause=e.details["errmsg"])

    def update(self, object_uid, pydantic_object):        
        operation = self.collection.update_one(
            {'_id': self.uid(object_uid)}, 
            {"$set": pydantic_object.dict(exclude={"_id"})},
            upsert=False)

        updated_item = self.get_by_uid(object_uid)
        return updated_item

    def delete(self, object_uid):
        item = self.get_by_uid(object_uid)
        self.collection.delete_one({"_id": self.uid(object_uid)})
        return item