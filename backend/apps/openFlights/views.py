from time import sleep
from django.http import HttpResponse
from jobtastic import JobtasticTask

from backend.apps.openFlights.models import *

class AirportsUpdateTask(JobtasticTask):
    """
    Class to perform lazy airport update
    """
    # These are the Task kwargs that matter for caching purposes
    significant_kwargs = [
        ('numerators', str),
        ('denominators', str),
    ]
    # How long should we give a task before assuming it has failed?
    herd_avoidance_timeout = 60  # Shouldn't take more than 60 seconds
    # How long we want to cache results with identical ``significant_kwargs``
    cache_duration = 0  # Cache these results forever. Math is pretty stable.
    # Note: 0 means different things in different cache backends. RTFM for yours.

    def calculate_result(self, numerators, denominators, **kwargs):
        """
        MATH!!!
        """


def update_airports(request):

    flush = (request.GET.get('flush') is 'True' or request.GET.get('flush') is 'true')
    openFlights = OpenFlights.get_solo()

    if flush:
        openFlights.flush_airports()
    else:
        print "Updating airports database..."

    result = openFlights.update_airports()

    return HttpResponse(result, content_type="application/json")
