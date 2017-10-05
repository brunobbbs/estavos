from django import template

register = template.Library()

@register.filter('total')
def total(inscription):
    players = inscription.competitors.all().count()
    price = inscription.tournament.price
    return players * price
