import gridfs
import json
import pika
from flask import Flask, request, send_file
from flask_pymongo import PyMongo

from auth import validate
from auth_svc import access
from storage import util
from bson.objectid import ObjectId

server = Flask(__name__)

mongo_video = PyMongo(server, uri="mongodb://host.minikube.internal:27017/videos")
mongo_mp3 = PyMongo(server, uri="mongodb://host.minikube.internal:27017/mp3s")

fs_videos = gridfs.GridFS(mongo_video.db)
fs_mp3s = gridfs.GridFS(mongo_mp3.db)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

channel = connection.channel()


@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)
    if not err:
        return token
    else:
        return err


@server.route("/upload", methods=["POST"])
def upload():
    access_tok, err = validate.token(request)
    if err:
        return err
    access_tok = json.loads(access_tok)

    if access_tok["admin"]:
        if len(request.files) > 1 or len(request.files) < 1:
            return "exactly one file required", 400

        for _, f in request.files.items():
            err = util.upload(f, fs_videos, channel, access_tok)
            if err:
                return err

        return "success", 200
    else:
        return "not authorized", 401


@server.route("/download", methods=["GET"])
def download():
    access_tok, err = validate.token(request)
    if err:
        return err
    access_tok = json.loads(access_tok)

    if access_tok["admin"]:
        fid_string=request.args.get("fid")

        if not fid_string:
            return "fid is require",400
        try:
            out=fs_mp3s.get(ObjectId(fid_string))
            return send_file(out,download_name=f'{fid_string}.mp3')
        except Exception as err:
            print(err)
            return "inetrnal server error",500



    return "not authorized",401



if __name__ == '__main__':
    server.run(host="0.0.0.0", port=8080)
