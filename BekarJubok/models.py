from django.db import models

class JobCategory(models.Model):
    category_name = models.CharField(max_length=100,null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

#class CategoryField(models.Model):
 #   jobcategory = models.ForeignKey(JobCategory,on_delete=models.CASCADE)
 #   position = models.CharField(max_length=130)
 #   date = models.DateTimeField(auto_now_add=True)

  #  def __str__(self):
   #     return self.position

class JObDescription(models.Model):
    company = models.CharField(max_length=200,default="Google")
    jobcategory = models.ForeignKey(JobCategory,related_name='category',on_delete=models.CASCADE)
    position = models.CharField(max_length=200,default="Software Engineer")
    desc = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    app_dedline = models.TextField()
    published = models.DateTimeField()

    def __str__(self):
        return self.company

class Employee(models.Model):
    name = models.CharField(max_length=100,null=False)
    occupation = models.CharField(max_length=200,null=False)
    email = models.EmailField()
    profile_pic = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name




