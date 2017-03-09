from django.db import models
from django.contrib.auth.models import Permission, User

def submission_code(instance, code):
    return '/'.join(['media', str(instance.problem.pcode), code])


def problem_pinp(instance, pinp):
    return '/'.join(['media', str(instance.pcode), pinp])

def problem_pans(instance, pans):
    return '/'.join(['media', str(instance.pcode), pans])


class Problem(models.Model):
    user = models.ForeignKey(User, default=1)
    pcode = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=20, default='')
    pdesc = models.TextField()
    author = models.CharField(max_length=20)
    is_done = models.BooleanField(default=False)
    test_input = models.FileField(upload_to=problem_pinp)
    answer = models.FileField(upload_to=problem_pans)

    def __str__(self):
        return str(self.pcode)


class Submission(models.Model):
    user = models.ForeignKey(User, default=1)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=submission_code)


class Timer(models.Model):
    stime = models.DateTimeField()
    etime = models.DateTimeField()

    def __str__(self):
        return str(self.stime)
