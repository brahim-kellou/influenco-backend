import requests
import json

INSTAGRAM_URL = "https://www.instagram.com"


def calc_engagement(user):
    total_interactions = 0
    followers = user["edge_followed_by"]["count"]
    posts = user["edge_owner_to_timeline_media"]["edges"]
    post_start = 1
    post_end = 11
    for i in range(post_start, post_end):
        post = posts[i]["node"]
        count_comments = post["edge_media_to_comment"]["count"]
        count_likes = post["edge_liked_by"]["count"]
        total_interactions = total_interactions + count_comments + count_likes
    avg_likes_cmt = total_interactions / (post_end - post_start)
    engagement = avg_likes_cmt/followers*100

    return engagement


def construct_user(user):
    profile_pic_url = user["profile_pic_url_hd"].replace("\u0026", "&")
    engagement = calc_engagement(user)

    new_user = {
        "id": user["id"],
        "username": user["username"],
        "fullname": user["full_name"],
        "bio": user["biography"],
        "has_channel": user["has_channel"],
        "is_business_account": user["is_business_account"],
        "business_category_name": user["business_category_name"],
        "is_verified": user["is_verified"],
        "profile_pic_url": profile_pic_url,
        "followers": user["edge_followed_by"]["count"],
        "following": user["edge_follow"]["count"],
        "posts": user["edge_owner_to_timeline_media"]["count"],
        "engagement": engagement,
    }

    return new_user


def get_user(username):
    new_user = dict()
    url = INSTAGRAM_URL + "/" + username + "/?__a=1"

    response = requests.get(url)
    response_json = json.loads(response.text)

    user_json = response_json["graphql"]["user"]
    is_private = response_json["graphql"]["user"]["is_private"]
    if not is_private and user_json["edge_owner_to_timeline_media"]["count"] >= 12:
        new_user = construct_user(user_json)

    return new_user
