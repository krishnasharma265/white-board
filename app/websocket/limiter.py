import time


class RateLimiter:

    def __init__(self):
        self.user_events = {}


    def is_allowed(
        self,
        username: str,  
        event_type: str,
        limit: int,
        seconds: int
    ):
        now = time.time()

        key = f"{username}:{event_type}"


        if key not in self.user_events:

            self.user_events[key] = []


        self.user_events[key] = [

            timestamp

            for timestamp in
            self.user_events[key]

            if now - timestamp < seconds
        ]


        if len(self.user_events[key]) >= limit:

            return False


        self.user_events[key].append(now)

        return True