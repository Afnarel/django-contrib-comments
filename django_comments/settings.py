from django.conf import settings

ALLOW_DUPLICATES = getattr(settings, "COMMENTS_ALLOW_DUPLICATES", False)
