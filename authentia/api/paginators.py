import os
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = os.getenv('PAGE_NUMBER_PAGINATION')
    page_size_query_param = 'page_size'
