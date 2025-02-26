from mastodon import Mastodon

mastodon=Mastodon(access_token="KWl9FMZqdJ9KKgP3XumnICmLF2U80_jAPswLQix7ITE",api_base_url="https://mastodon.social")


def post(content):
    status=mastodon.status_post(content)
    return status['id']

def retrieve(id):
    status=mastodon.status(id)
    return status['content']

def delete(id):
    status=mastodon.status_delete(id)
    return status['content']
