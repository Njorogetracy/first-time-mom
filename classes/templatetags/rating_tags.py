from django import template

register = template.Library()


@register.simple_tag
def rating_stars(avg_rating):
    if avg_rating is None:
        return ''
    avg_rating = round(avg_rating)
    full_stars = int(avg_rating)
    empty_stars = 5 - full_stars
    stars = '★' * full_stars + '☆' * empty_stars
    return stars
