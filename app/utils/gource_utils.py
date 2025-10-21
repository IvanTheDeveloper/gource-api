import subprocess
import os

def clone_repo(username, repo_name, repo_path):
    repo_url = f"https://github.com/{username}/{repo_name}.git"
    try:
        subprocess.run(
            ["git", "clone", "--bare", repo_url, f"{repo_path}/.git"],  #   --filter=blob:none
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        return {
            "error": "Could not clone repository, make sure it existe and is public",
            "details": e.stderr.decode()
        }
    return None

def generate_gource_video_file(repo_path, output_path, gource_params):
    gource_cmd = f"xvfb-run -a gource {repo_path} {gource_params} -1280x720 --seconds-per-day 1 -o -"

    ffmpeg_cmd = ('ffmpeg -y -r 30 -f image2pipe -vcodec ppm -i - -vcodec libx264 '
        f'-preset ultrafast -pix_fmt yuv420p -crf 18 -threads 0 -bf 0 "{output_path}"')
    
    piped_cmd = f"{gource_cmd} | {ffmpeg_cmd}"

    try:
        subprocess.run(["bash", "-c", piped_cmd], check=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {
            "error": "Error running Gource or FFmpeg",
            "details": e.stderr.decode()
        }
    return None
