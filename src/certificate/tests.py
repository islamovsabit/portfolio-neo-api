# from datetime import datetime
#
#
# def format_date(date_str):
#     # List of possible date formats
#     date_formats = ["%d.%m.%Y", "%Y.%m.%d", "%Y.%d.%m"]
#
#     # Attempt to parse the date with each format
#     for format in date_formats:
#         try:
#             date_obj = datetime.strptime(date_str, format)
#             formatted_date = date_obj.strftime("%d %B %Y")
#             return formatted_date
#         except ValueError:
#             continue
#
#     return "Invalid date format"
#
# # Test with different date strings
# date_str1 = "10.18.2022"
# date_str2 = "2022.12.25"
#
# formatted_date1 = format_date(date_str1)
# formatted_date2 = format_date(date_str2)
#
# print(formatted_date1)  # Output: "18 October 2022"
# print(formatted_date2)  # Output: "25 December 2022"


from urllib.parse import urlparse
from django.http import HttpRequest
from django.http import HttpResponse


def my_view(request):
    # Get the host name
    host_name = request.get_host()
    # Parse the host name to extract just the domain
    domain = urlparse(f'//{host_name}').hostname
    return HttpResponse(f'Domain: {domain}')