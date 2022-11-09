from random import *

def nahodna_veta():
    kto = choice(('Kamarát','Spolužiak','Andrej','Roman'))#nahodny vyber
    corobil = choice(('videl','prezradil','povedal','napísal','zistil','nakreslil'))#nahodny vyber
    ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé'))#nahodny vyber
    co = choice(('tajomstvo','prekvapenie','predsavzatie'))#nahodny vyber
    kde = choice(('v zahrade','doma','v skole','v praci'))#nahodny vyber
    spojene = kto +' '+corobil+' '+ake+' '+co+' '+kde+'.'
    print(spojene)#vykreslenie v shelli
for i in range(1,21):
    nahodna_veta() #privolanie funkcie

