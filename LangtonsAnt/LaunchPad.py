from midiutil import MIDIFile

	#C		#Cm	      #C7		#C9		      
Notes = [[[60, 64, 67], [60, 63, 67], [60, 64, 67, 70], [60, 64, 67, 70, 74],
          #Csus2	#Cdim	      #Cm7[b5]	        #C13
          [60, 62, 67], [60, 63, 66], [60, 63, 66, 70], [60, 64, 67, 70, 74, 77, 81]],

         
        #D		#m	      #7		#9
         [[62, 66, 69], [62, 65, 69], [62, 66, 69, 72], [62, 66, 69, 72, 76],
          #sus2	        #dim	      #m7[b5]	        #13
          [62, 64, 69], [62, 65, 68], [62, 65, 68, 72], [62, 66, 69, 72, 76, 79, 83]],

         
        #E		#m	      #7		#9
         [[64, 68, 71], [64, 67, 71], [64, 68, 71, 74], [64, 68, 71, 74, 78],
          #sus2	        #dim	      #m7[b5]	        #13
          [64, 66, 71], [64, 67, 70], [64, 67, 70, 74], [64, 68, 71, 74, 78, 81, 85]],

         
        #F		#m	      #7		#9
         [[65, 69, 72], [65, 68, 72], [65, 69, 72, 75], [65, 69, 72, 75, 79],
          #sus2	        #dim	      #m7[b5]	        #13
          [65, 67, 72], [65, 68, 71], [65, 68, 71, 75], [65, 69, 72, 75, 79, 82, 86]],

         
        #G		#m	      #7		#9
         [[67, 71, 74], [67, 70, 74], [67, 71, 74, 77], [67, 71, 74, 77, 81],
          #sus2	        #dim	      #m7[b5]	        #13
          [67, 69, 74], [67, 70, 73], [67, 70, 73, 77], [67, 71, 74, 77, 81, 84, 88]],

         
        #A		#m	      #7		#9
         [[69, 73, 76], [69, 72, 76], [69, 73, 76, 79], [69, 73, 76, 79, 83],
          #sus2	        #dim	      #m7[b5]	        #13
          [69, 71, 76], [69, 72, 75], [69, 72, 75, 79], [69, 73, 76, 79, 83, 86, 90]],

         
        #B		#m	      #7		#9
         [[71, 75, 78], [71, 74, 78], [71, 75, 78, 81], [71, 75, 79, 81, 85],
          #sus2	        #dim	      #m7[b5]	        #13
          [71, 73, 78], [71, 74, 77], [71, 74, 77, 81], [71, 75, 79, 81, 85, 88, 92]],

         
        #High C		#m	      #7		#9
         [[72, 76, 79], [72, 75, 79], [72, 76, 79, 82], [72, 76, 80, 82, 86],
          #sus2	        #dim	      #m7[b5]	        #13
          [72, 74, 79], [72, 75, 78], [72, 75, 78, 82], [72, 76, 80, 82, 86, 89, 93]]]

Drums = {}
Percussion = 35
for xNote in range(0,8):
    for yNote in range(0,8):
        if Percussion == 82:
            Percussion = 35
        Drums[(xNote,yNote)] = Percussion
        Percussion += 1
track    = 0     
count    = 0    # 1 + 2 + 3 + 4 +
duration = 0.25    # In beats
tempo    = 500  # BPM
volume   = 127  # 0-127, as per the MIDI standard

midi = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)

midi.addTempo(track, count, tempo)
midi.addTrackName(track, count, "Langton's Launch Jams.")
midi.addProgramChange(track, 0, count, 107)

def writeMidi(ant):
    x, y = (ant.curpos['x']/64), (ant.curpos['y']/64)
    chord = Notes[int(x)][int(y)]
    for i in chord:
        midi.addNote(track, 0, i, ant.turns, 2, volume)
    if ant.turns == 250:
        with open("Langtons_Launch_Jams3.mid", "wb") as output_file:
            midi.writeFile(output_file)
            
midi.addProgramChange(track, 1, count, 116)
def writeMidi2(ant):
    x, y = (ant.curpos['x']/64), (ant.curpos['y']/64)
    chord = Notes[int(x)][int(y)]
    for i in chord:
        midi.addNote(track, 1, i, ant.turns, 3, volume)
    if ant.turns == 250:
        with open("Langtons_Launch_Jams3.mid", "wb") as output_file:
            midi.writeFile(output_file)

midi.addProgramChange(track, 2, count, 105)
def writeMidi3(ant):
    x, y = (ant.curpos['x']/64), (ant.curpos['y']/64)
    chord = Notes[int(x)][int(y)]
    for i in chord:
        midi.addNote(track, 1, i, ant.turns, duration, volume)
    if ant.turns == 1000:
        with open("Langtons_Launch_Jams3.mid", "wb") as output_file:
            midi.writeFile(output_file)
            
def writeDrums(ant):
    x, y = (ant.curpos['x']/64), (ant.curpos['y']/64)
    note = Drums[(x,y)]
    midi.addNote(track,1,note, ant.turns, 0.5, volume)
    if ant.turns == 5000:
        with open("AntJams.mid", "wb") as output_file:
            midi.writeFile(output_file)
