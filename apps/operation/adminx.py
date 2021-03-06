import xadmin
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


# Register your models here.

class UserAskAdmin(object):
    list_display = (
        'name',
        'mobile',
        'course_name',
        'add_time',
    )


class CourseCommentsAdmin(object):
    list_display = (
        'user',
        'course',
        'comments',
        'add_time',
    )


class UserFavoriteAdmin(object):
    list_display = (
        'user',
        'fav_id',
        'fav_type',
        'add_time',
    )


class UserMessageAdmin(object):
    list_display = (
        'user',
        'message',
        'has_read',
        'add_time',
    )


class UserCourseAdmin(object):
    list_display = ('user', 'course', 'add_time',)


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
