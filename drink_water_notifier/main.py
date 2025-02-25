import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "The amount of water you should drink depends on your age, activity level, and other factors.Recommended daily fluid intake Men: About 15.5 cups (3.7 liters) Women: About 11.5 cups (2.7 liters)",
            app_icon = "icon.ico",
            timeout = 10
        )
        time.sleep(60*60)

