from django.db import models


class Movie(models.Model):

    name = models.CharField(max_length=200, unique=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Projection(models.Model):

    movie_id = models.ForeignKey(Movie)
    movie_type = models.CharField(max_length=200)
    date = models.DateField('projection date')
    time = models.TimeField('time of projection')

    def __str__(self):
        return '{} - {} - {}'.format(self.movie_id, self.movie_type, self.date)


class Reservation(models.Model):

    username = models.CharField(max_length=200)
    projection_id = models.ForeignKey(Projection)
    row = models.IntegerField()
    col = models.IntegerField()

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.username, self.projection_id.movie_id, self.row, self.col)
