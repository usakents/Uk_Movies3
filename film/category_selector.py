from.models import(Category)

def get_category():
    return Category.objects.all()

def get_categ(categ_id):
    return Category.get(pk=categ_id)