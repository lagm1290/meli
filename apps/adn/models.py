from django.db import models

# Create your models here.
class DnaVerified(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    dna = models.TextField(verbose_name='dna')
    is_mutant = models.BooleanField(verbose_name='Is Mutant')

    def __str__(self):
        return self.dna

    class Meta:
        app_label = 'adn'
        db_table = 'adn_verified'
        verbose_name = 'Dna Verified'
        verbose_name_plural = 'Dnas Verified'
