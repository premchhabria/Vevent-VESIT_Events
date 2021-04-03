from django.db import models
from time import strftime
import datetime
from datetime import timezone,datetime
from django.core.exceptions import ValidationError


# Create your models here.
class Events(models.Model):
    def validate_date(value):
        x=datetime.today()
        value_date_=int(value.strftime("%Y")+value.strftime("%m")+value.strftime("%d"))
        date_=int(x.strftime("%Y")+x.strftime("%m")+x.strftime("%d")) 
        if value_date_<date_:
            raise ValidationError("The date cannot be in past!")
        else:
            return value


    class organizers(models.TextChoices):
        IIC='IIC'
        Exam_Dept='Exam_Dept'
        Code_cell='CodeCell'
        CSI='CSI'
        IEEE='IEEE'
        ISTE='ISTE'
        ISA='ISA'
        E_cell='E_cell'
        Cultural_Event='Cultural'
        Sports_Event='Sports'
        Sort_Event='Sort'
        Others='Others'
        
    class eventtype(models.TextChoices):
        Institute_level='Institute_level'
        Department_level='Department_level'
        Student_body='Student_body'
    
    
    event_name = models.CharField(max_length=100)

    event_datetime = models.DateTimeField(validators=[validate_date])

    event_add_datetime = models.DateTimeField(auto_now_add=True)

    event_duration = models.IntegerField()

    event_organizer = models.CharField(max_length=100,choices=organizers.choices)

    # event_details = models.FileField(upload_to ='uploads/', blank=True)
    event_details = models.URLField(blank=True)

    event_description = models.TextField()

    event_gformlink = models.URLField()

    event_status = models.BooleanField(editable=False, default=False)

    event_type = models.CharField(max_length=100,choices=eventtype.choices,default="Student_body")

    def __str__(self):
        return self.event_name