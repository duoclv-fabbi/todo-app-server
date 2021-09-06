from django.db import models
import datetime
# Create your models here.

class TaskModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(null=True, blank=True, default=False)
    content = models.CharField(max_length=500, default="")

    class Meta:
        db_table = 'tbl_task'
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        super(TaskModel, self).save(*args, **kwargs)