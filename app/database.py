
# Create MongoDB Connection
import pymongo
import config

def get_db():
    mongo_client = pymongo.MongoClient(config.MONGO_URL)
    db = mongo_client[config.DB_NAME]

    user_collection = db[config.USER_CRED_COLLECTION_NAME]
    testing_data_collection = db[config.TESTING_COLLECTION_NAME]
    return user_collection, testing_data_collection