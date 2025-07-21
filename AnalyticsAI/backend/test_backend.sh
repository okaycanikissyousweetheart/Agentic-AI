#!/bin/bash

set -e

echo "Creating virtual environment..."
python3 -m venv env
source env/bin/activate

echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting FastAPI server in background..."
uvicorn app.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!

sleep 3

echo "Testing /api/status endpoint..."
STATUS=$(curl -s http://127.0.0.1:8000/api/status)
echo "Response: $STATUS"

if [[ "$STATUS" == *"ok"* ]]; then
  echo "✅ Backend test passed."
else
  echo "❌ Backend test failed."
  kill $SERVER_PID
  exit 1
fi

kill $SERVER_PID
deactivate