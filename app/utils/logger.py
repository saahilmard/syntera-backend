import logging
import time
from functools import wraps
from typing import Callable
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("syntera")

def log_request(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request_id = str(uuid.uuid4())[:8]
        start_time = time.time()
        
        logger.info(f"[{request_id}] Starting {func.__name__}")
        try:
            result = await func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            logger.info(f"[{request_id}] Completed {func.__name__} in {elapsed_time:.2f}s")
            return result
        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(f"[{request_id}] Error in {func.__name__} after {elapsed_time:.2f}s: {str(e)}")
            raise
    
    return wrapper 