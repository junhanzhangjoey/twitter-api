from mastodon import Mastodon
#create a mastodon instance
mastodon=Mastodon(access_token="KWl9FMZqdJ9KKgP3XumnICmLF2U80_jAPswLQix7ITE",api_base_url="https://mastodon.social")

#use status_post() function from mastodon API to post data
def post(content):
    status=mastodon.status_post(content)
    return status['id']
#use status() function from mastodon API to retrieve data
def retrieve(id):
    status=mastodon.status(id)
    return status['content']
#use status_delete function from mastodon API to delete data
def delete(id):
    status=mastodon.status_delete(id)
    return status['content']
