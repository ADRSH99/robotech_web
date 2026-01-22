from django.urls import get_resolver
from django.http import JsonResponse

def list_endpoints(request):
    resolver = get_resolver()
    urls = []

    for pattern in resolver.url_patterns:
        try:
            urls.append({
                "pattern": str(pattern.pattern),
                "name": pattern.name,
                "lookup_str": pattern.lookup_str,
            })
        except Exception:
            pass

    return JsonResponse({"endpoints": urls})
