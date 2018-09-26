from django.db import models


class DayOfWeek(models.Model):
    DAY_OF_WEEK_CHOICES = (
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота')
    )
    day = models.IntegerField(choices=DAY_OF_WEEK_CHOICES, verbose_name='день недели', unique=True)

    class Meta:
        verbose_name = 'день недели'
        verbose_name_plural = 'дни недели'
        ordering = ['day']

    def __str__(self):
        return self.get_day_display()


class Grade(models.Model):
    number = models.IntegerField(verbose_name='класс')

    def number_of_subjects(self):
        return len(self.subject_set.all())

    def get_timetable_list(self):
        ordered_list = []
        days = DayOfWeek.objects.filter(subject__grade__number=self.number).distinct()
        for cur_day in days:
            subjects_of_day = self.subject_set.filter(day__day=cur_day.day).order_by('time')
            ordered_list.append([len(subjects_of_day), cur_day.get_day_display, subjects_of_day])
        return ordered_list

    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'классы'
        ordering = ['number']

    def __str__(self):
        return str(self.number)


class Subject(models.Model):
    grade = models.ManyToManyField(Grade, verbose_name='класс')
    name = models.CharField(max_length=50, verbose_name='название')
    day = models.ForeignKey(DayOfWeek, verbose_name='день недели')
    room = models.CharField(max_length=10, verbose_name='аудитория')
    time = models.TimeField(verbose_name='время')

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
        ordering = ['name']

    def number_of_grades(self):
        return len(self.grade.all())

    def grades_as_string(self):
        grades = self.grade.order_by('number')
        is_first_grade = True
        grade_string = ''
        for grade in grades:
            if is_first_grade:
                is_first_grade = False
            else:
                grade_string += ', '
            grade_string += str(grade.number)
        return grade_string

    def __str__(self):
        return self.name+' – '+self.grades_as_string()
