# Render Deployment Guide

## Prerequisites
- A Telegram bot token (get from @BotFather)
- A GitHub account
- A Render account (free tier available)

## Step-by-Step Deployment

### 1. Prepare Your Repository
1. Fork or clone this repository
2. Make sure all files are present:
   - `web.py` (main webhook application)
   - `bot.py` (local development version)
   - `config.py` (configuration)
   - `requirements.txt` (dependencies)
   - `Procfile` (Render startup command)
   - `render.yaml` (Render configuration)
   - `.env` (environment variables - don't commit this!)

### 2. Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up for a free account
3. Verify your email

### 3. Deploy to Render

#### Option A: Using render.yaml (Recommended)
1. Push your code to GitHub
2. On Render Dashboard, click "New+" → "Web Service"
3. Connect your GitHub account
4. Select your repository
5. Render will automatically detect `render.yaml` and configure everything
6. Add environment variables (see step 4 below)
7. Click "Create Web Service"

#### Option B: Manual Configuration
1. On Render Dashboard, click "New+" → "Web Service"
2. Choose "Build and deploy from a Git repository"
3. Connect your GitHub repository
4. Configure settings:
   - **Name:** message-delete-bot (or your preferred name)
   - **Region:** Choose closest to your users
   - **Branch:** main (or your default branch)
   - **Root Directory:** Leave empty
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python web.py`

### 4. Configure Environment Variables
In your Render service settings, add these environment variables:

```
BOT_TOKEN=your_actual_telegram_bot_token_here
WEBHOOK_URL=https://your-service-name.onrender.com
DEBUG=False
```

**Important Notes:**
- Replace `your_actual_telegram_bot_token_here` with your real bot token from @BotFather
- Replace `your-service-name` with your actual Render service name
- The WEBHOOK_URL will be: `https://your-render-app-name.onrender.com`

### 5. Set the Webhook
After deployment is complete:

1. Visit your app URL: `https://your-app-name.onrender.com/set_webhook`
2. You should see a success message confirming the webhook is set
3. If you get an error, check your BOT_TOKEN and try again

### 6. Test Your Bot
1. Start a chat with your bot on Telegram
2. Send `/start` command
3. The bot should respond with the welcome message

### 7. Add to Groups
1. Use the "Add to Group" button in the welcome message
2. Make the bot an admin with "Delete messages" permission
3. Test message deletion functionality

## Troubleshooting

### Common Issues:

**Webhook Not Setting:**
- Check that BOT_TOKEN is correct
- Ensure your Render app is running
- Visit the `/set_webhook` endpoint manually

**Bot Not Responding:**
- Check Render logs for errors
- Verify the bot has proper permissions in groups
- Ensure only one instance is running

**Messages Not Deleting:**
- Confirm bot has admin permissions with delete rights
- Check that timer is not set to "off"
- Verify the bot is active and running

**Application Crashes:**
- Check Render logs for specific error messages
- Ensure all required environment variables are set
- Verify requirements.txt dependencies are installed

## Useful Render Endpoints

- **Health Check:** `https://your-app-name.onrender.com/health`
- **Set Webhook:** `https://your-app-name.onrender.com/set_webhook`
- **Root:** `https://your-app-name.onrender.com/` (shows status)

## Monitoring

- Check logs in Render Dashboard → Your Service → Logs
- Set up notifications in Render for deployment status
- Monitor uptime and performance metrics

## Updating Your Bot

1. Make changes to your code
2. Commit and push to GitHub
3. Render will automatically deploy the new version
4. If you changed the bot logic, you may need to reset the webhook

## Cost

- Render free tier includes:
  - 1 web service
  - 512 MB RAM
  - 100 GB bandwidth/month
  - 15 minutes of sleep time after inactivity
- For production use, consider upgrading to a paid plan

## Best Practices

1. **Environment Variables:** Never commit `.env` files to GitHub
2. **Security:** Use strong, unique bot tokens
3. **Monitoring:** Regularly check Render logs
4. **Backups:** Keep your code in version control
5. **Testing:** Test thoroughly before deploying updates