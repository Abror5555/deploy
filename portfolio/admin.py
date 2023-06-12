from django.contrib import admin
from portfolio.models import Portfolio_Category, PortfolioCount, Portfolio_Project, HitCount


# Register your models here.

class Portfolio_CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    @admin.display
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )

admin.site.register(Portfolio_Category, Portfolio_CategoryAdmin)
admin.site.register(PortfolioCount)



class Portfolio_ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Portfolio_Project, Portfolio_ProjectAdmin)

admin.site.register(HitCount)