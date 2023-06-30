#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Posts """
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/posts', methods=['GET'], strict_slashes=False)
def get_posts():
    """
    Retrieves the sorted list of all Post objects
    """
    def get_upvotes(element):
        upvotes = element['upvotes']
        return len(upvotes)
    all_posts = storage.all(Post).values()
    list_posts = []
    for post in all_posts:
        list_posts.append(post.to_dict())
    list_posts.sort(key=get_upvotes, reverse=True)
    return jsonify(list_posts)
