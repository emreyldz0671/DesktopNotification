from plyer import notification

notification_title = 'SELAM DÜNYALI!'
notification_message = 'Bugün dünyada güzel bir gün. Günün güzel geçsin adamım..'

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)