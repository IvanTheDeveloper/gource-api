import os
import tempfile
from flask import Blueprint, request, jsonify, send_file
from ..utils.gource_utils import clone_repo, generate_gource_video_file

gource_bp = Blueprint("gource", __name__)

@gource_bp.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "online"
    }), 200

@gource_bp.route("/<username>/<repo_name>", methods=["GET"])
def generate_video(username, repo_name):
    gource_params = request.args.get("gource_params", "")

    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = os.path.join(tmpdir, repo_name)
        output_path = os.path.join(tmpdir, f"gource-{username}-{repo_name}.mp4")
        
        clone_result = clone_repo(username, repo_name, repo_path)
        if clone_result is not None:
            return jsonify(clone_result), 400

        video_result = generate_gource_video_file(repo_path, output_path, gource_params)
        if video_result is not None:
            return jsonify(video_result), 500

        return send_file(output_path, mimetype="video/mp4")
