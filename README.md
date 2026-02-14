# Message-SelfDestruct Bot

A Telegram bot that automatically deletes messages in groups after a customizable time period.

## Features

- 🗑️ Auto-delete messages after set time intervals
- ⏱️ Customizable timer with button interface (10s to 1h)
- 🤖 Easy-to-use commands
- 📊 Status checking
- 🔧 Configurable time options
- ☁️ Ready for cloud deployment (Render, Heroku, etc.)

## Setup

### Local Development

1. **Create a Telegram Bot:**
   - Talk to [@BotFather](https://t.me/BotFather) on Telegram
   - Use `/newbot` command to create a new bot
   - Copy the bot token

2. **Install Dependencies:**
   ```bash
   # Using the setup script (recommended)
   ./setup.sh
   
   # Or manually:
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure the Bot:**
   - Edit `.env` file
   - Replace `your_bot_token_here` with your actual bot token

4. **Run the Bot:**
   ```bash
   # For local development (polling mode)
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   python bot.py
   
   # For web deployment (webhook mode)
   python web.py
   ```

## Deployment on Render

### Method 1: Using render.yaml (Recommended)

1. **Fork this repository** to your GitHub account

2. **Create a new Web Service on Render:**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New+" → "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` file

3. **Configure Environment Variables:**
   In the Render dashboard, add these environment variables:
   ```
   BOT_TOKEN=your_telegram_bot_token_here
   WEBHOOK_URL=https://your-app-name.onrender.com
   DEBUG=False
   ```

4. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your bot

### Method 2: Manual Setup on Render

1. **Create a new Web Service:**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New+" → "Web Service"
   - Connect your repository or use manual deployment

2. **Configure Build Settings:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python web.py`
   - **Environment:** Python

3. **Add Environment Variables:**
   ```
   BOT_TOKEN=your_telegram_bot_token_here
   WEBHOOK_URL=https://your-app-name.onrender.com
   DEBUG=False
   ```

4. **Deploy and Set Webhook:**
   After deployment, visit:
   `https://your-app-name.onrender.com/set_webhook`
   
   This will automatically set the webhook for your bot.

## Usage

### Commands:
- `/start` - Start the bot and show welcome message with "Add to Group" button
- `/timer` - Open timer selection menu
- `/status` - Check current timer settings
- `/help` - Show help information

### Welcome Message Features:
- 🆕 **Add to Group button** - Direct link to add bot to any group
- 💬 **Join Our Chat button** - Direct link to https://t.me/last_promise_chatting_212
- 🕐 **Set Timer button** - Quick access to timer settings

### Timer Selection Features:
- ⚙️ **Custom Timer** - Set precise time with +/- buttons for hours, minutes, seconds
- 🎯 **Preset Options** - Quick select from 10s, 30s, 1m, 5m, 10m, 30m, 1h, off

### Timer Options:
- `10s` - 10 seconds
- `30s` - 30 seconds
- `1m` - 1 minute
- `5m` - 5 minutes
- `10m` - 10 minutes
- `30m` - 30 minutes
- `1h` - 1 hour
- `off` - Disable auto-deletion

## Group Setup

1. Add the bot to your Telegram group
2. Make the bot an **admin** with "Delete messages" permission
3. The bot will automatically start monitoring and deleting messages

## Configuration

Edit `config.py` to customize:
- Default deletion time
- Available time options
- Logging settings
- Webhook configuration

## How It Works

1. The bot monitors all messages in the group
2. When a message is sent, it schedules deletion based on current timer setting
3. Messages are deleted automatically after the specified time
4. Users can change the timer using the `/timer` command

## Requirements

- Python 3.7+
- python-telegram-bot 20.7+
- python-dotenv 1.0.0+
- Flask 2.3.3+ (for webhook deployment)

## Note

- The bot needs admin permissions to delete messages
- For production use, consider using a database instead of in-memory storage
- Bot will only work in groups where it has proper permissions
- Make sure only one instance of the bot is running to avoid conflicts
- When deployed on Render, the bot uses webhooks instead of polling for better performance

## Troubleshooting

**Webhook not working:**
- Visit `https://your-app-name.onrender.com/set_webhook` to manually set the webhook
- Check Render logs for any errors
- Ensure your BOT_TOKEN is correct

**Bot not responding:**
- Check if the bot has admin permissions in the group
- Verify the webhook is properly set
- Check Render application logs

**Messages not deleting:**
- Ensure the bot has "Delete messages" permission
- Check if the timer is not set to "off"
- Verify the bot is running without errors