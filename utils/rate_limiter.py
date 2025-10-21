"""
Rate Limiter for EVE Corp Navigator Bot v1.0.0
Prevents abuse and ensures fair usage
"""

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List

class RateLimiter:
    """Per-user rate limiting"""

    def __init__(self, max_per_minute: int = 20):
        self.max_per_minute = max_per_minute
        self.user_requests: Dict[str, List[datetime]] = defaultdict(list)

    def is_rate_limited(self, user_id: str) -> bool:
        """Check if user is rate limited"""
        now = datetime.now()
        cutoff = now - timedelta(minutes=1)

        # Remove old requests
        self.user_requests[user_id] = [
            req_time for req_time in self.user_requests[user_id]
            if req_time > cutoff
        ]

        # Check limit
        if len(self.user_requests[user_id]) >= self.max_per_minute:
            return True

        # Add current request
        self.user_requests[user_id].append(now)
        return False

    def get_remaining(self, user_id: str) -> int:
        """Get remaining requests for user"""
        now = datetime.now()
        cutoff = now - timedelta(minutes=1)

        recent = [
            req_time for req_time in self.user_requests.get(user_id, [])
            if req_time > cutoff
        ]

        return max(0, self.max_per_minute - len(recent))
