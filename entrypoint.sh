#!/bin/bash
set -e

if [ "$ENV" = "development" ]; then
    echo "[RUNTIME] Installing/updating dependencies for development..."
    pip install --no-cache-dir -r requirements.txt
fi

echo "[RUNTIME] Container running on port $CONTAINER_PORT with command: $@"
exec "$@"
