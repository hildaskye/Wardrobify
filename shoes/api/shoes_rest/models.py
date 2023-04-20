from django.db import models


class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()
    import_href = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.closet_name} Bin {self.bin_number}"


class Shoe(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    picture_url = models.URLField(max_length=200)
    shoe_bin = models.ForeignKey(
        BinVO,
        related_name="shoe",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.color} {self.model_name}"
