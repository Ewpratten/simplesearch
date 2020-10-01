# Interfaces for beginning web crawl jobs

from crawler.lib.crawltask import WebCrawlTask
from typing import List

# Queue of active tasks
_active_task_queue: List[WebCrawlTask] = []

def begin(url: str, max_depth: int, max_width: int) -> None:
    """Begin crawling from a base URL

    Args:
        url (str): URL to crawl
        max_depth (int): Max crawl depth
        max_width (int): Max crawl width
    """
    global _active_task_queue

    # Add the first crawl task
    _active_task_queue.append(WebCrawlTask(url, max_depth, max_width))

    # Build a list of seen URLs
    seen_urls = []

    # Handle every task in the queue
    task_run_count: int = 0
    for task in _active_task_queue:

        # If this is a repeat url, skip it
        if task.getURL() in seen_urls:
            _active_task_queue = _active_task_queue[1:]
            continue

        # Handle all possible subtasks
        for subtask in task.run():
            _active_task_queue.append(subtask)

        # Pop the running task off the queue
        _active_task_queue = _active_task_queue[1:]

        # Add to the task count
        task_run_count += 1
        seen_urls.append(task.getURL())

        print(f"Finished crawl task: {task_run_count}/{len(_active_task_queue)}")