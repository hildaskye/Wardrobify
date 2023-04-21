from django.db import models


class LocationVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True, null=True, blank=True)
    closet_name = models.CharField(max_length=100)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.closet_name}, section {self.section_number}"


class Hat(models.Model):
    fabric = models.CharField(max_length=200)
    style_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True)
    location = models.ForeignKey(
        LocationVO,
        related_name="hats",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.color} {self.style_name}"
