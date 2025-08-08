from django import template

register = template.Library()

@register.filter
def get_product_image(product_name):
    """Map product names to their actual image filenames"""
    image_mapping = {
        'Atomic Habits': 'Atomic_Habits.jpg',
        'The Subtle Art of Not Giving a F*ck': 'The_Subtle_Art_of_Not_Giving_a_Fuck.jpg',
        'Coiling Dragon': 'Coiling_Dragon.jpeg',
        'Stellar Transformation': 'Stellar_Transformation.jpg',
        'How To Win Friends And Influence People': 'How_To_Win_Friends_And_Influence_People.jpg',
        'Lord of the Mysteries': 'LOTM.jpg',
        'Circle of Inevitability': 'COI.jpeg',
        'Embers Ad Infinitum': 'Embers_Ad_Infinitum.jpeg',
        'Google Pixel': 'google_pixel.webp',
        'iPhone': 'iphone.jpg',
    }
    return image_mapping.get(product_name, 'Atomic_Habits.jpg')
