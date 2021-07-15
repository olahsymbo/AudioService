import os
import sys
import inspect
import json
import logging
from api_response import api_response
from flask import Flask, request, jsonify
from table_models.models import Song, Podcast, AudioBook, db

app_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(app_path))

sys.path.insert(0, module_dir)

app = Flask(__name__)


@app.route("/create", methods=['POST'])
def create_audio():
    if request.method == 'POST':
        data = []
        try:
            file_type = request.form.get('audioFileType')
            metadata = json.loads(request.form.get('audioFileMetadata'))
            if file_type == 'song':
                data = Song(**metadata)
            elif file_type == 'audiobook':
                data = AudioBook(**metadata)
            elif file_type == 'podcast':
                if len(metadata['participants']) > 10:
                    metadata['participants'] = []
                data = Podcast(**metadata)

            db.session.add(data)
            db.session.commit()

            output = api_response(data.serialize())
            return jsonify(output.true_output()), 200
        except Exception as error:
            logging.error([error])
            output = api_response(data)
            return jsonify(output.error_output()), 400

    else:
        return jsonify(success=False), 500


@app.route("/delete/<audioFileType>/<audioFileID>", methods=['DELETE'])
def delete_audio(audioFileType, audioFileID):

    if request.method == 'DELETE':
        data = []
        try:
            if audioFileType == 'song':
                data = Song.query.get(audioFileID)
            elif audioFileType == 'audiobook':
                data = AudioBook.query.get(audioFileID)
            elif audioFileType == 'podcast':
                data = Podcast.query.get(audioFileID)

            db.session.delete(data)
            db.session.commit()

            return jsonify(success=True), 200
        except Exception as error:
            logging.error([error])
            return jsonify(success=False), 400

    else:
        return jsonify(success=False), 500


@app.route("/update/<audioFileType>/<audioFileID>", methods=['PUT'])
def update_audio(audioFileType, audioFileID):
    if request.method == 'PUT':
        metadata = []
        try:
            metadata = json.loads(request.form.get('audioFileMetadata'))
            if audioFileType == 'song':
                instance = Song.query.filter(Song.id == audioFileID)
                instance.update(dict(metadata))
            elif audioFileType == 'audiobook':
                instance = AudioBook.query.filter(AudioBook.id == audioFileID)
                instance.update(dict(metadata))
            elif audioFileType == 'podcast':
                instance = Podcast.query.filter(Podcast.id == audioFileID)
                if len(metadata['participants']) > 10:
                    metadata['participants'] = []
                instance.update(dict(metadata))

            db.session.commit()

            output = api_response(metadata)
            return jsonify(output.true_output()), 200
        except Exception as error:
            logging.error([error])
            output = api_response(metadata)
            return jsonify(output.error_output()), 400

    else:
        return jsonify(success=False), 500


@app.route("/get/<audioFileType>/<audioFileID>", methods=['GET'])
def get_audio(audioFileType, audioFileID):
    output = []
    if request.method == 'GET':
        instance = []
        try:
            if audioFileType == 'song':
                instance = Song.query.filter(Song.id == audioFileID).first()
            elif audioFileType == 'audiobook':
                instance = AudioBook.query.filter(AudioBook.id == audioFileID).first()
            elif audioFileType == 'podcast':
                instance = Podcast.query.filter(Podcast.id == audioFileID).first()

            output = api_response(instance.serialize())
            return jsonify(output.true_output()), 200
        except Exception as error:
            logging.error([error])
            output = api_response(instance)
            return jsonify(output.error_output()), 400

    else:
        return jsonify(success=False), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
