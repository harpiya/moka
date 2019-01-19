# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-11T15:59:34+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: exceptions.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T01:29:50+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri

from colander import Invalid


class MokaError(Exception):

    """Base class for connection and response errors."""


class MokaConnectionError(MokaError):

    """Error communicating with the Authorize.net API."""


class MokaResponseError(MokaError):

    """Error response code returned from API."""

    def __init__(self, errorCode, status, full_response):
        self.ResultCode = ResultCode
        self.ResultMessage = ResultMessage
        self.full_response = full_response

    def __str__(self):
        return '%s: %s' % (self.ResultCode, self.ResultMessage)


class MokaInvalidError(MokaError, Invalid):

    def __init__(self, invalid):
        self.node = invalid.node
        self.msg = invalid.msg
        self.value = invalid.value
        self.children = invalid.children
