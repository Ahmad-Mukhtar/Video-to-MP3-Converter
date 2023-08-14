import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy.editor


def start(message, fs_videos, fs_mp3s, channel):
    msg = json.loads(message)

    tf = tempfile.NamedTemporaryFile()
    out = fs_videos.get(ObjectId(msg["video_fid"]))

    tf.write(out.read())
    audio = moviepy.editor.VideoFileClip(tf.name).audio
    tf.close()
    video_id=msg["video_fid"]
    tf_path = tempfile.gettempdir() + "/"+video_id+".mp3"
    audio.write_audiofile(tf_path)

    f = open(tf_path, "rb")
    data = f.read()
    fid = fs_mp3s.put(data)
    f.close()
    os.remove(tf_path)

    msg["mp3_fid"] = str(fid)
    try:
        channel.basic_publish(
            exchange="",
            routing_key=os.environ.get("MP3_QUEUE"),
            body=json.dumps(msg),
            properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
        )
    except Exception as err:
        fs_mp3s.delete(fid)
        return "failed to publish message"
