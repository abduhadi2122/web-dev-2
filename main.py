from flask import Flask, render_template, request, redirect, url_for, make_response

from handlers.auth import auth_handlers
from handlers.topic import topic_handlers
from handlers.comment import comment_handlers

from models.settings import db
from models.user import User
from models.topic import Topic

import hashlib
import uuid
import os
import smartninja_redis

redis = smartninja_redis.from_url(os.environ.get("REDIS_URL"))

app = Flask(__name__)
app.register_blueprint(auth_handlers)
app.register_blueprint(topic_handlers)
app.register_blueprint(comment_handlers)

db.create_all()






if __name__ == '__main__':
    app.run()