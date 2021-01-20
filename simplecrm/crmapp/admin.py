from django.contrib import admin
from .models import Account
from .models import Activity
from .models import ActivityStatus
from .models import Contact
from .models import ContactSource
from .models import ContactStatus

admin.site.register(ActivityStatus),
admin.site.register(Account),
admin.site.register(Activity),
admin.site.register(Contact),
admin.site.register(ContactSource),
admin.site.register(ContactStatus)

# Register your models here.
