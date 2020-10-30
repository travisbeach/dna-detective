import os
from django.conf import settings

from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from django_rq import job

from .models import Submission
from .jobs import Searcher

@job
def run_sequence_search(id, query):
    searcher = Searcher()
    name, index, protein, description = searcher.search_genbank(query)

    submission = Submission.objects.filter(id=id)[0]
    submission.status = 'COMPLETED'
    submission.name = name
    submission.index = index
    submission.description = description
    submission.protein = protein
    submission.save()

@csrf_exempt
def create(request):
    query = request.POST.get('query')
    submission = Submission()
    if query:
        submission.query = query
        submission.status = 'IN_PROGRESS'
        submission.save()

        #Add to protein lookup queue
        run_sequence_search.delay(id=submission.id, query=submission.query)

    return JsonResponse(serialize(submission))

def all(request):
    submissions = Submission.objects.all().order_by('-id')
    return JsonResponse([serialize(submission) for submission in submissions], safe=False)

def serialize(submission):
    return {
        "id": submission.id, 
        "status": submission.status, 
        "query":submission.query, 
        "name":submission.name, 
        "index": submission.index, 
        "description": submission.description, 
        "protein": submission.protein
        }

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    build`).
    """
    index_file_path = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')

    def get(self, request):
        try:
            with open(self.index_file_path) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead after
                running `yarn start` on the frontend/ directory
                """,
                status=501,
            )