#!/usr/bin/env python3
"""
Smart startup script that detects environment and runs appropriate bot version
"""
import os
import sys

def main():
    # Check if we're running on Render
    if os.environ.get('RENDER'):
        print("=== Render Deployment ===")
        print("Running on Render environment")
        
        # Verify required environment variables
        bot_token = os.environ.get('BOT_TOKEN')
        webhook_url = os.environ.get('WEBHOOK_URL')
        
        if not bot_token:
            print("❌ ERROR: BOT_TOKEN is not set")
            print("Please set BOT_TOKEN in Render environment variables")
            sys.exit(1)
        
        if not webhook_url:
            print("❌ ERROR: WEBHOOK_URL is not set")
            print("Please set WEBHOOK_URL in Render environment variables")
            sys.exit(1)
        
        print("✅ Environment variables verified")
        print(f"BOT_TOKEN: {bot_token[:10]}...")
        print(f"WEBHOOK_URL: {webhook_url}")
        
        # Run the webhook version
        print("🚀 Starting webhook bot...")
        os.execv(sys.executable, [sys.executable, 'web.py'])
    
    else:
        print("=== Local Development ===")
        print("Running in local development environment")
        print("Starting polling bot for local testing...")
        os.execv(sys.executable, [sys.executable, 'bot.py'])

if __name__ == "__main__":
    main()