from pymongo import MongoClient

# Connecting to MongoDB
MONGO_HOST = 'mongodb://localhost:27017'
mongo_client = MongoClient(MONGO_HOST)
db = mongo_client["social_media_db"]

if __name__ == "__main__":
    cursor = db.influencers_instagramuser.find({})
    for document in cursor:
        db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"followers": document['user_status'][-1]['followers']}})
        db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"following": document['user_status'][-1]['following']}})
        db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"posts": document['user_status'][-1]['posts']}})
        db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"engagement": document['user_status'][-1]['engagement']}})
        print(document['username'])