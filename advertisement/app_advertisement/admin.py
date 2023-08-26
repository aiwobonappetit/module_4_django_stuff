from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "auction", "created_date", "updated_date"]
    list_filter = ["created", "auction"]
    actions = ["auction_toggle_off", "auction_toggle_on"]
    fieldsets = (
        (
            "Общее",
            {"fields" : ("title", "description")}
        ),
        (
            "Финансы",
            {"fields" : ("price", "auction"),
             "classes" : ["collapse"]}
        )
    )

    @admin.display(description="Убрать возможность торга")
    def auction_toggle_off(self, request, queryset):
        queryset.update(auction=False)

    @admin.display(description="Добавить возможность торга")
    def auction_toggle_on(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)