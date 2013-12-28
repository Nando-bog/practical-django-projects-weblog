
#utf-8
import datetime
from models import Category, Entry


def pop_categories():
    for n in range(10):
        category_title = "cat %s %s" % (n, datetime.datetime.now().strftime("%Y/%m/%d"))
        category_slug = category_title + ' slug'
        category_description = "Aenean erat felis, fermentum sit amet fringilla quis, porta eu dolor. Curabitur vel massa vel neque bibendum cursus non ac mi."
        new_cat = Category(title=category_title, slug=category_slug, description=category_description)
        new_cat.save()
        print('Saved %s to database.' % new_cat.title)

pop_categories()