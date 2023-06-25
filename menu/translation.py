from modeltranslation.translator import TranslationOptions, translator

from menu.models import Category,Product




class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)



class ProductTranslationOptions(TranslationOptions):
    fields = ('name','info')





translator.register(Category,CategoryTranslationOptions)
translator.register(Product,ProductTranslationOptions)