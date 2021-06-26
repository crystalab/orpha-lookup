from django.contrib import admin

from orpha_lookup.apps.orpha.models import DisorderType, DisorderGroup, Frequency, Disorder, Hpo


@admin.register(DisorderType)
class DisorderTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(DisorderGroup)
class DisorderGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight')
    search_fields = ('name',)


@admin.register(Disorder)
class DisorderAdmin(admin.ModelAdmin):
    list_display = ('id', 'orpha_code', 'disorder_type', 'disorder_group')
    list_select_related = ('disorder_group', 'disorder_type')
    list_filter = ('disorder_group', 'disorder_type')
    search_fields = ('name', 'orpha_code')


@admin.register(Hpo)
class HpoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hpo_id', 'name']
    search_fields = ('name', 'hpo_id')
