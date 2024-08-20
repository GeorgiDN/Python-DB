from django.db import models


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return (self.annotate(missions_count=models.Count('astronauts_missions'))
                .order_by('-missions_count', 'phone_number'))
