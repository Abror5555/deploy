from modeltranslation.translator import TranslationOptions, register
from portfolio.models import Portfolio_Category, PortfolioCount, Portfolio_Project


@register(Portfolio_Category)
class Portfolio_CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(PortfolioCount)
class PortfolioCountTranslationOptions(TranslationOptions):
    fields = ('title', 'projects')

@register(Portfolio_Project)
class Portfolio_ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'button', 'button1', 'created_time')