# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Blueprint, jsonify

from invenio_rest import ContentNegotiatedMethodView

blueprint = Blueprint(
    'b2share_users',
    __name__,
    url_prefix='/users'
)


def user_to_json_serializer(data, code=200, headers=None):
    """Build a json flask response using the given data.
    :Returns: A flask response with json data.
    :Returns Type: :py:class:`flask.Response`
    """
    response = jsonify(data)
    response.status_code = code
    if headers is not None:
        response.headers.extend(headers)
    # TODO: set location to seld
    # response.headers['location'] = ...
    # TODO: set etag
    # response.set_etag(...)
    return response


class UserList(ContentNegotiatedMethodView):

    view_name = 'users_list'

    def __init__(self, *args, **kwargs):
        """Constructor."""
        super(UserList, self).__init__(*args, **kwargs)
        self.serializers = {
            'application/json': user_to_json_serializer,
        }

    def get(self, **kwargs):
        """
        Search for users.
        """
        return None


class User(ContentNegotiatedMethodView):

    view_name = 'user_item'

    def __init__(self, *args, **kwargs):
        """Constructor."""
        super(User, self).__init__(*args, **kwargs)
        self.serializers = {
            'application/json': user_to_json_serializer,
        }

    def get(self, user_id, **kwargs):
        """
        Get a user profile information
        """
        return None


blueprint.add_url_rule('/',
                       view_func=UserList
                       .as_view(UserList.view_name))
blueprint.add_url_rule('/<int:user_id>',
                       view_func=User
                       .as_view(User.view_name))