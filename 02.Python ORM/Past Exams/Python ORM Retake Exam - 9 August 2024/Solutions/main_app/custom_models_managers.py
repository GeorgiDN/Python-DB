from django.db import models


class HouseManager(models.Manager):
    def get_houses_by_dragons_count(self):
        return self.annotate(num_of_dragons=models.Count('house_dragons')).order_by('-num_of_dragons', 'name')
