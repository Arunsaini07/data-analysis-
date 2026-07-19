import subprocess
import time
import random


def send_notification():
    subprocess.run(
        [
            "terminal-notifier",
            "-title",
            "Maggie 🫀❤️‍🩹<𝟑", 
            "-message",
            "Meri yad nhi aa rhi h, jaana🎀💗👀!",
            "-group",
            str(random.randint(1000, 999999))
        ]
    )


def maggie_reminder(interval_seconds=10, iterations=5):#iteration means how many times the notification will be sent, you can change it as per your need
    count = 0

    while count < iterations:
        send_notification()

        count += 1  
        time.sleep(interval_seconds)


if __name__ == "__main__":
    maggie_reminder()