from django.db import models, IntegrityError, DataError


class Author(models.Model):
    name = models.CharField(blank=True, max_length=25)
    surname = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):
       return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
        }
