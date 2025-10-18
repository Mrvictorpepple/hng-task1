import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timezone

class MeView(APIView):
    def get(self, request):
        try:
            fetch_cat_fact = requests.get('https://catfact.ninja/fact', timeout=3)
            fetch_cat_fact.raise_for_status()
            cat_fact = fetch_cat_fact.json().get('fact', 'Oops...No fact available right now.')
        except Exception:
            cat_fact = "Can't fetch fact right now"

        timestamp = datetime.now(timezone.utc).isoformat()
        data = {
            'status': 'success',
            'profile': {
                'email': 'mrvictorpepple@gmail.com',
                'name': 'Victor Pepple',
                'stack': 'Python/Django',
            },
            'timestamp': timestamp,
            'fact': cat_fact,
        }
        return Response(data, content_type='application/json')