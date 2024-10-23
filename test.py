# Seperate file for simple testing
import asyncio
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

async def notif():
    await notifier.send(title = "test notif", message = "test notif")

def main():
    asyncio.run(notif())
    