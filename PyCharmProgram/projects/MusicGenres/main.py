import nltk
from nltk.tokenize import RegexpTokenizer

def getSongGenre(file,genre):
    metal = open('metal.list', 'r') #Datei mit Metal-Cliches aufmachen
    metal_list = metal.read().split(',') #Datei mit Metal-Cliches auslesen und eine Liste bauen
    metal.close() #Datei mit Metal-Cliches zumachen
    pop = open('pop.list', 'r') #Datei mit Pop-Cliches aufmachen
    pop_list = pop.read().split(',') #Datei mit Pop-Cliches auslesen und eine Liste bauen
    pop.close() #Datei mit Pop-Cliches zumachen
    rap = open('rap.list', 'r') #Datei mit Rap-Cliches aufmachen
    rap_list = rap.read().split(',') #Datei mit Rap-Cliches auslesen und eine Liste bauen
    rap.close() #Datei mit Rap-Cliches zumachen
    song = open('songs/'+file, 'r') #Liedtext aufmachen
    text = song.read() #Liedtext auslesen
    text_lower = text.lower()  #nur Kleinbuchstaben fuer das praezise Vergleichen
    tokenizer = RegexpTokenizer(r'\w+')  #RE als Muster angeben
    words_list = tokenizer.tokenize(text_lower) #Liste der Woerter im Liedtext
    metal_index = 0 #Metal-Cliches Zaehler
    pop_index = 0 #Pop-Cliches Zaehler
    rap_index = 0 #Rap-Cliches Zaehler
    for x in words_list: #Liedtext durchgehen
        metal_match = [i for i in metal_list if x == i] #Metal-Cliche finden
        pop_match = [i for i in pop_list if x == i] #Pop-Cliche finden
        rap_match = [i for i in rap_list if x == i] #Rap-Cliche finden
        if metal_match: #+1 Falls Metal-Cliche
            metal_index += 1
        if pop_match: #+1 Falls Pop-Cliche
            pop_index += 1
        if rap_match: #+1 Falls Rap-Cliche
            rap_index += 1
    cliches = metal_index+pop_index+rap_index #Anzahl Cliches
    metal_tendency = metal_index/cliches*100 #Prozent Metal-Cliches
    pop_tendency = pop_index/cliches*100 #Prozent Pop-Cliches
    rap_tendency = rap_index/cliches*100 #Prozent Rap-Cliches
    print(file,'('+genre+')')
    print('Cliches found:',cliches)
    print('Metal cliches:',metal_index,'('+str(round(metal_tendency,2))+'%)')
    print('Pop cliches:', pop_index, '(' + str(round(pop_tendency, 2)) + '%)')
    print('Rap cliches:', rap_index, '(' + str(round(rap_tendency, 2)) + '%)')

getSongGenre('Manowar - March For Revenge','metal')
getSongGenre('Marduk - Baptism By Fire','metal')
getSongGenre('Katy Perry - Teenage Dream','pop')
getSongGenre('Britney Spears - Baby One More Time','pop')
getSongGenre('Snoop Dogg - Lollipop','rap')
getSongGenre('Ice Cube - The Wrong Nigga To Fuck With','rap')