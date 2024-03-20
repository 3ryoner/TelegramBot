

class SubscriptionNotificationsRepo:
    def __init__(self):
        self.subscriptions: list[int] = []

    async def get_subscriptions(self) -> list[int]:
        return self.subscriptions

    async def add_subscription(self, chat_id: int):
        if chat_id not in self.subscriptions:
            self.subscriptions.append(chat_id)

    async def remove_subscription(self, chat_id: int):
        if chat_id in self.subscriptions:
            self.subscriptions.remove(chat_id)