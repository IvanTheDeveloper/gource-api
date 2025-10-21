#!/bin/bash
set -e

if [ "$FLASK_ENV" = "development" ] || [ "$FLASK_DEBUG" = "1" ]; then
    echo "[INFO] Installing/updating dependencies for development..."
    pip install --no-cache-dir -r requirements.txt
fi

echo "[INFO] Running: $@"
exec "$@"
