from pymongo import MongoClient
# import requests
import simplejson as json
import datetime
from random import randint
from django.utils.text import slugify

# Connecting to MongoDB
MONGO_HOST = 'mongodb://localhost:27017'
mongo_client = MongoClient(MONGO_HOST)
db = mongo_client["social_media_db"]
db_influencers = db.influencers_instagramuser

instagram_url = "https://www.instagram.com"

if __name__ == "__main__":
    print(slugify("Brahim Kellou"))
    cursor = db_influencers.find({})
    minutes_cpt = 0
    days_cpt = 8
    for doc in cursor:
        if doc['business_category_name'] == "none": 
            db_influencers.update_one({"_id": doc['_id']}, {"$set": {"business_category_name": None}})
        # if len(doc['user_status']) < 9:
        #     print(doc)
        #     minutes_cpt += 1
        #     minutes_cpt = minutes_cpt % 60
        #     user_status = doc['user_status']
        #     new_user_status = {}

        #     followers = user_status[-1]['followers']
        #     following = user_status[-1]['following']
        #     posts = user_status[-1]['posts']
        #     engagement = user_status[-1]['engagement']
        #     date = user_status[-1]['date']

        #     new_user_status['version'] = 9
        #     new_user_status['followers'] = int(followers*(1 + engagement/1500 )) + randint(-int(followers*(engagement/2000 )), int(followers*(engagement/2000 )))
        #     new_user_status['following'] = following + randint(0, 10)
        #     new_user_status['posts'] = int(user_status[-1]['posts']*(1 + 0.5/100))
        #     new_user_status['engagement'] = engagement*(1 + randint(-20, 15) / 100)
        #     new_user_status['date'] = date + datetime.timedelta(days=days_cpt, minutes=minutes_cpt, seconds=randint(0, 60))
        #     new_user_status['predicted'] = True

        #     user_status.append(new_user_status)
        #     db_influencers.update_one({"_id": doc['_id']}, {"$set": {"user_status": user_status}})
            