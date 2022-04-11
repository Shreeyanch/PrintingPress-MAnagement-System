from django.contrib import admin
from .models import Image
from .models import services , faq , clien, order , distribution , paper,ink

# Register your models here.
admin.site.register(Image)
admin.site.register(services)

admin.site.register(faq)

admin.site.register(clien)
admin.site.register(order)
admin.site.register(distribution)
admin.site.register(paper)
admin.site.register(ink)