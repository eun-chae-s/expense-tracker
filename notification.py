"""This file contains the code for creating a daily notification

Reference:
https://medium.com/analytics-vidhya/create-desktop-notifier-using-python-6dab0a1c348c
"""
from plyer import notification

title = 'Hey, are you saving your money?'
message = 'Please record your daily spends to the tracker!'

notification.notify(title=title,
                    message=message,
                    app_name='',
                    app_icon='',
                    timeout=10,
                    toast=False)
