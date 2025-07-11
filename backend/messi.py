
import random

messi_images = [
    "https://assets.goal.com/images/v3/blt29f72e9312da0948/GOAL%20-%20Multiple%20Images%20-%203%20x%204.jpg?auto=webp&format=pjpg&width=640&quality=80",
    "https://assets.goal.com/images/v3/blt637754176b365589/Lionel%20Messi%20Inter%20Miami%202023.jpg?auto=webp&format=pjpg&width=640&quality=80",
    "https://b.fssta.com/uploads/application/soccer/headshots/886.vresize.350.350.medium.14.png",
]

def get_random_messi_image():
    return random.choice(messi_images)
