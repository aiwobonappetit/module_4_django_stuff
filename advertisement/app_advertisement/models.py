from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

class Advertisement(models.Model):
    class Meta:
        db_table = "advertisement"

    def __str__(self):
        return f"id = {self.id}, title = {self.title}, price = {self.price}"

    title = models.CharField(
        max_length = 80,
        verbose_name = "Название"
    )

    description = models.TextField(
        verbose_name = "Описание"
    )

    price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        verbose_name = "Цена"
    )

    auction = models.BooleanField(
        verbose_name = "Торг",
        default = False
    )

    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Дата публикации"
    )

    updated = models.DateTimeField(
        auto_now = True,
        verbose_name = "Дата обновления"
    )

    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created.date() == timezone.now().date():
            created_time = self.created.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time
            )
        else:
            return self.created.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Дата обновления")
    def updated_date(self):
        if self.updated.date() == timezone.now().date():
            updated_time = self.updated.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: dodgerblue; font-weight: bold;'>Сегодня в {}</span>", updated_time
            )
        else:
            return self.updated.strftime("%d.%m.%Y в %H:%M:%S")