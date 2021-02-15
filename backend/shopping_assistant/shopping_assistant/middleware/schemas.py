from pydantic import BaseModel, BaseConfig, Field
from bson.objectid import ObjectId


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")


def serialize_object_id(oid):
    return str(oid)


class MongoModel(BaseModel):
    uid: OID = None

    class Config(BaseConfig):
        json_encoders = {
            ObjectId: serialize_object_id
        }
        fields = {'uid': '_id'}
