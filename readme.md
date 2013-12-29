Coltrane project from Bennett, J. (2008). Practical Django Projects (Expert’s Voice in Web Development) (1 edition.). Apress.

Some modification were necessary in order to make the project work with Django 1.6, and others were choice:
- Prepopulated fields work differently. Implemented through admin.py and prepopulated_fields for each ModelAdmin.
- Used django-ckeditor-updated instead of markup. I totally prefer a full WYSIWYG with HTML.
- django-taggit to handle tags instead of what the book uses. Django-tagging seems to have died out.
- Date-based generic views work differently in Django 1.6.

Requirements:
Django==1.6.1
django-ckeditor-updated==4.2.6
django-tagging==0.3.1
psycopg2==2.5.1
wsgiref==0.1.2