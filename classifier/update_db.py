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
            