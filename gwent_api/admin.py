from django.contrib import admin

from .models import Card, CardSet, Category, Rarity, Faction, Group, Position, Variation


admin.site.register(Card)
admin.site.register(CardSet)
admin.site.register(Category)
admin.site.register(Rarity)
admin.site.register(Faction)
admin.site.register(Group)
admin.site.register(Position)
admin.site.register(Variation)