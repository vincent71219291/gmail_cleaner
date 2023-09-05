def search_messages(
    service, query: str, label_ids: list[str] | None = None
) -> list[dict[str, str]]:
    if label_ids is None:
        label_ids = []
    results = (
        service.users()
        .messages()
        .list(userId="me", q=query, labelIds=label_ids)
        .execute()
    )
    messages = []
    if "messages" in results:
        messages += results["messages"]
    while "nextPageToken" in results:
        page_token = results["nextPageToken"]
        results = (
            service.users()
            .messages()
            .list(userId="me", q=query, pageToken=page_token)
            .execute()
        )
        messages += results["messages"]
    print(f"{len(messages)} message(s) found.")
    return messages


def move_to_trash(service, messages: list[dict[str, str]]):
    service.users().messages().batchModify(
        userId="me",
        body={
            "ids": [msg["id"] for msg in messages],
            "addLabelIds": ["TRASH"],
        },
    ).execute()


def delete_permanently(service, messages: list[dict[str, str]]):
    service.users().messages().batchDelete(
        userId="me", body={"ids": [message["id"] for message in messages]}
    ).execute()


def mark_as_read(service, messages: dict):
    service.users().messages().batchModify(
        userId="me",
        body={
            "ids": [msg["id"] for msg in messages],
            "removeLabelIds": ["UNREAD"],
        },
    ).execute()
