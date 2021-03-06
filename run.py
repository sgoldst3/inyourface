import os
import sys
import click
import pprint
import inyourface.effect
from inyourface import EffectOrchestrator


import click
@click.command()
@click.option('--url', required=True, multiple=True, help='Url of the input image to be manipulated')
@click.option('--effect', '-e', required=True, multiple=True, help='The effect to apply, can specify multiple with -e effect1 -e effect2')

@click.option('--google_credentials', default='./google-credentials.json', help='Location of google API credentials json file.')
@click.option('--image_directory', default='./', help='Where to put finished images.')
@click.option('--cache_dir', default=False, help='Directory in which to place a cache of face detection results')

# TODO: implement --list
#@click.option('--list', help='List available effects')

def run(url, effect, google_credentials, image_directory, cache_dir):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_credentials

    effect = list(filter((lambda x: is_effect(x)), effect))

    if (len(effect) == 0):
        print "You must specify some effects!"
        exit()
    elif (len(effect) == 1):
        effect_module = getattr(inyourface.effect, effect[0][0].upper() + effect[0][1:])
        gif = effect_module.EffectAnimator(url, image_directory, cache_dir)
        print gif.gif()
    else:
        gif = EffectOrchestrator(url, image_directory, cache_dir, effect)
        print gif.gif()

def is_effect(e):
    try:
        effect_module = getattr(inyourface.effect, e[0].upper() + e[1:])
        return True
    except Exception as ex:
        return False


if __name__ == '__main__':
    run()
