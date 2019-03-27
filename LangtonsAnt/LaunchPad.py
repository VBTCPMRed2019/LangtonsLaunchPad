from midiutil import MIDIFile #https://pypi.org/project/MIDIUtil/

#This is the module for writing the physical midi file in standart midi format.
#Ant.py will pass the Ant's current position to this module.
#This module has two seperate functions: one for writing chords, and one for writing percussion instruments to the midi file.


#The "Notes" variable is all of the chords we have choosen for our project.
#	Notes is used specifically for the writeMidi function
#Notes is layed out in an 8x8 array so it fits perfectly with the Launchpad graphic.
#We have choosen 8 notes and 8 chords for this project.
#The notes include: C, D, E, F, G, A, B, and High C.
#Based on those notes we chose the chords Major, Minor, Seventh, Ninth, Suspended Second, Diminished, Minor Seventh with a Flat Fifth, 
#and a Thirteenth, for each and every note.
#The numeralical values in this array represent the value of the note in midi notation.
	#C		#m	      #7		#9		      
Notes = [[[60, 64, 67], [60, 63, 67], [60, 64, 67, 70], [60, 64, 67, 70, 74],
          #sus2		#dim	      #m7[b5]	        #13
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

#The Drums dictionary is used specifically for the writeDrums function.
#The dictionary starts empty but is soon populated by 46 values in range of 35 to 81.
#At the end of the loop the dictionary will look something like this:
#Drums = {(0, 0) : 35, (0, 1) : 36, (0, 2) : 37, . . . 
#	(5, 5): 80, (5, 6): 81, (5, 7): 35, (6, 0): 36, . . . (7, 6): 50, (7, 7): 51}
#I only used numbers in between 35 and 81 because the channel used for percussion in midi format
#only allows for 46 values and for some reason those values were decided to  be placed on the 35 to 81 note values.
#This link can help explain if you are at all confused: https://www.midi.org/specifications-old/item/gm-level-1-sound-set
Drums = {}
Percussion = 35
for xNote in range(0,8):
    for yNote in range(0,8):
        if Percussion == 82:
            Percussion = 35
        Drums[(xNote,yNote)] = Percussion
        Percussion += 1
	
track 	 = 0    # Midi allows for multiple tracks to be written. 0 is one track, 1 is an additional track, and so on.
count    = 0    # This declares where the note will be placed based on beats.
duration = 1    # How long a note will last (in beats).
tempo    = 144  # Beats Per Minute (BPM)
volume   = 127  # 0-127, as per the MIDI standard

midi = MIDIFile(1)  #Calling of the midiutil module

midi.addTempo(track, count, tempo)
midi.addTrackName(track, count, "Langton's Launch Jams.") #Title of the midi file (can only be viewed in notation software)
midi.addProgramChange(track, 0, count, 107)

def writeMidi(ant): #Function to write the chords in the midi file
    x, y = (ant.curpos['x']/64), (ant.curpos['y']/64) #Takes the ant's current x and y position and divides both values by 64,
							#this is so because the ant's position increments 64 pixels at a time.
    chord = Notes[int(x)][int(y)] #finds the chord in Notes based on the x and y value of the ant
    for i in chord:
        midi.addNote(track, 0, i, ant.turns, 2, volume) #Function to add the note to the midi file.
	#midi.addnote(track, channel, pitch, time, duration, volume)
    if ant.turns == 5000: #Outputs the midi file after 5000 turns. This number can be changed to anything, beware that a bigger number
				#will cause a bigger midi file and may or may not be able to be open by a normal midi reader.
        with open("Langtons_Launch_Jams.mid", "wb") as output_file: #These two lines output the midi file to be read by a music
            midi.writeFile(output_file)					#player or notation software.
	
def writeDrums(ant):
    x, y = (ant.curpos['x']/64), (ant.curpos['y']/64)
    note = Drums[(x,y)]
    midi.addNote(track,0,note, ant.turns, 0.5, volume)
    if ant.turns == 5000:
        with open("AntJams.mid", "wb") as output_file:
            midi.writeFile(output_file)
