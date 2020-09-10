from pymongo import MongoClient
import requests
import simplejson as json

# Connecting to MongoDB
MONGO_HOST = 'mongodb://localhost:27017'
mongo_client = MongoClient(MONGO_HOST)
db = mongo_client["social_media_db"]

instagram_url = "https://www.instagram.com"

if __name__ == "__main__":
    
    # cursor = db.influencers_instagramuser.find({})
    # for document in cursor:
        
    #     # else:
    #     #     print("username: ", document["username"], " , engagement: ", document["engagement"])
    #     #     db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"class": "user"}})
    #     # db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"followers": document['user_status'][-1]['followers']}})
    #     # db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"following": document['user_status'][-1]['following']}})
    #     # db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"posts": document['user_status'][-1]['posts']}})
    #     # db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"engagement": document['user_status'][-1]['engagement']}})
    #     # print(document['username'])

    cursor = db.influencers_instagrampost.find({})
    for document in cursor:
        try:
            if document["class_influence"] == "micro-influencer":
                username = document["username"]
                url = instagram_url + "/" + username + "/?__a=1"
                print(username)
                response = requests.get(url)
                response_json = json.loads(response.text)
                user_json = response_json["graphql"]["user"]
                profile_pic_url = user_json["profile_pic_url_hd"].replace("\u0026", "&")
                db.influencers_instagramuser.update_one({"_id": document["_id"]}, {"$set": {"profile_pic_url": profile_pic_url}})
                print("done")
        except:
            pass