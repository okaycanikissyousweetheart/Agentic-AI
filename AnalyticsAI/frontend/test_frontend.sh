#!/bin/bash

set -e

echo "Installing npm dependencies..."
npm install

echo "Starting React dev server in background..."
npm start &

SERVER_PID=$!

echo "Waiting for server to start..."
sleep 10

echo "Testing frontend homepage..."
RESPONSE=$(curl -s http://localhost:3000)
if [[ "$RESPONSE" == *"AnalyticsAI"* ]]; then
  echo "✅ Frontend test passed."
else
  echo "❌ Frontend test failed."
  kill $SERVER_PID
  exit 1
fi

kill $SERVER_PID