import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    host = "0.0.0.0"    # 0.0.0.0 open, 127.0.0.1 closed.
    port = int(os.environ.get("CONTAINER_PORT"))    # 8080 http, 8443 https.
    app.run(host=host, port=port)
