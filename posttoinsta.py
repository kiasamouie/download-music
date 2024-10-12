from instabot import Bot

# Initialize a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username="doeestepp", password="WQe8AZtJ8wgf79P*DPTBn")

# Upload a story
bot.upload_story_photo("img.jpg", caption="Your story caption")

# Logout from your Instagram account
bot.logout()