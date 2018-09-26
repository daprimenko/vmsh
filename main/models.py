from django.db import models


class AboutPost(models.Model):

    # def current_user(self):
    #     return self.request.user.id

    author = models.OneToOneField('auth.User',
                                  on_delete=models.CASCADE,
                                  verbose_name='автор',
                                  # default=current_user,
                                  unique=True)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'описание сайта'
        verbose_name_plural = 'описание сайта'

    def __str__(self):
        return 'Текст на странице /about'
