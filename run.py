#!/usr/bin/env python3
"""
Universal Telegram Bot Runner
Automatically detects environment and runs correct version
"""
import os
import sys

def main():
    print("=== Telegram Bot Startup ===")
    
    # Always run web.py on Render (webhook version)
    if os.environ.get('RENDER'):
        print("🚀 Render environment detected")
        print("Starting webhook version...")
        os.execv(sys.executable, [sys.executable, 'web.py'])
    
    # Local development - run polling version
    else:
        print("💻 Local development environment")
        print("Starting polling version...")
        os.execv(sys.executable, [sys.executable, 'bot.py'])

if __name__ == "__main__":
    main()