from django.db import models



contactStatus = ((1,"Active"),(2,"Done"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default=" ")
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date  = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=contactStatus,default=1)



    def __str__(self):
        return str(self.id)+" / "+self.name+" "+self.email+" "+self.subject+" "+self.message

