from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    # issued_to = models.CharField(max_length=200)
    number_of_copies = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# class Borrower(models.Model):
#     # bookname = models.ForeignKey(Book, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     issue_date = models.DateTimeField()
#     return_date = models.DateTimeField()

#     def __str__(self):
#         return self.name