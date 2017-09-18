from InstagramAPI.src.http.Response.Objects.Item import Item
from .Response import Response


class MediaCommentsResponse(Response):
    def __init__(self, response):
        self.item = None

        if self.STATUS_OK == response['status']:
            if 'media' in response and response['media']:
                self.item = Item(response['media'])

            if not response.get('comments_disabled', False):

                self.comments = response['comments']

                if response['has_more_comments']:
                    self.has_more = True
                    self.next_max_id = response['next_max_id']
                else:
                    self.has_more = False

            else:
                self.comments = []
                self.has_more = False

        else:
            self.setMessage(response['message'])
        self.setStatus(response['status'])

    def getItem(self):
        return self.taken_at  # Unresolved reference attribute
