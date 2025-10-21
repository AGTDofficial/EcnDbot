"""
Cache Manager for EVE Corp Navigator Bot v1.0.0
Caches frequently accessed data to reduce database load
"""

from datetime import datetime, timedelta
from typing import Dict, Tuple, Any, Optional

class CacheManager:
    """Simple in-memory cache with TTL"""

    def __init__(self, ttl_seconds: int = 300):
        self.cache: Dict[str, Tuple[Any, datetime]] = {}
        self.ttl = timedelta(seconds=ttl_seconds)

    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired"""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if datetime.now() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any):
        """Set cache value with timestamp"""
        self.cache[key] = (value, datetime.now())

    def delete(self, key: str):
        """Delete cached value"""
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """Clear all cached values"""
        self.cache.clear()

    def cleanup_expired(self):
        """Remove expired entries"""
        now = datetime.now()
        expired = [
            key for key, (_, timestamp) in self.cache.items()
            if now - timestamp >= self.ttl
        ]
        for key in expired:
            del self.cache[key]
