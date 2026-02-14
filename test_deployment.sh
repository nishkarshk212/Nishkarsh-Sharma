#!/bin/bash
# Test script for deployed bot

echo "=== Message Delete Bot Deployment Test ==="
echo

# Check if required environment variables are set
if [ -z "$BOT_TOKEN" ]; then
    echo "❌ BOT_TOKEN is not set"
    echo "Please set BOT_TOKEN environment variable"
    exit 1
fi

if [ -z "$WEBHOOK_URL" ]; then
    echo "❌ WEBHOOK_URL is not set"
    echo "Please set WEBHOOK_URL environment variable"
    exit 1
fi

echo "✅ Environment variables check passed"
echo "Bot Token: ${BOT_TOKEN:0:10}..."
echo "Webhook URL: $WEBHOOK_URL"
echo

# Test webhook endpoint
echo "=== Testing Webhook Endpoint ==="
curl -s "$WEBHOOK_URL/set_webhook" | jq '.'
echo
echo

# Test health endpoint
echo "=== Testing Health Check ==="
curl -s "$WEBHOOK_URL/health" | jq '.'
echo
echo

# Test root endpoint
echo "=== Testing Root Endpoint ==="
curl -s "$WEBHOOK_URL/" | jq '.'
echo
echo

echo "=== Deployment Test Complete ==="
echo "If all tests passed, your bot should be working!"
echo "Test the bot by sending /start command on Telegram"