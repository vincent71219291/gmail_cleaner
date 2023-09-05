from auth import authenticate
from messages import mark_as_read, move_to_trash
from task import Task

tasks = [
    Task(
        query="from:alerts@welcometothejungle.com older_than:2d",
        actions=[mark_as_read, move_to_trash],
    ),
    Task(
        query="from:alert@indeed.com older_than:2d",
        actions=[mark_as_read, move_to_trash],
    ),
    Task(
        query="from:jobalerts-noreply@linkedin.com older_than:2d",
        actions=[mark_as_read, move_to_trash],
    ),
    Task(
        query="from:notification@emails.hellowork.com older_than:2d",
        actions=[mark_as_read, move_to_trash],
    ),
    Task(
        query="is:unread older_than:14d",
        actions=[mark_as_read],
    ),
    Task(
        query="older_than:7d",
        label_ids=["CATEGORY_SOCIAL", "CATEGORY_PROMOTIONS"],
        actions=[mark_as_read, move_to_trash],
    ),
]


def main():
    service = authenticate()
    for task in tasks:
        print(f"Query: {task.query}")
        if task.label_ids:
            print(f"Labels: {task.label_ids}")
        task.execute(service)


if __name__ == "__main__":
    main()
