from rest_framework.pagination import LimitOffsetPagination


class MaximumLimitPagination(LimitOffsetPagination):
    max_limit = 20
