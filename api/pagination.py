from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )



class WatchListLimitOffsetPagination(LimitOffsetPagination):
    defaul_limit = 2
    max_limit = 20



    # https://www.youtube.com/watch?v=p4B8zFVRmHI&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&t=0s&index=14