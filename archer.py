##ARCHER
##create profiles for the main characters

class Archer:
    number_of_char = 0
    pay=0
    def __init__(self,name, post, voice, k_401):
        self.name=name
        self.post=post
        self.voice=voice
        self.k_401=k_401
        ##
        Archer.number_of_char+=1

    def full_profile(self):
        return '\nName-> '+self.name+'\nPost-> '+self.post+'\nVoice-> '\
               +self.voice+'\n401(k)-> '+f'{self.k_401:,d}'+'$'
    ##f-string used to split the number -> f'{self.k_401:,d}'


Sterling = Archer('Sterling Archer','Field Agent, Protagonist',
                  'H.Jon Benjamin',480810)
Lana = Archer('Lana Kane','Field Agent, Deuteragonist','Aisha Tyler',420675)
Malory = Archer('Malory Archer','CEO','Jessica Walter',2302725)
Ray = Archer('Ray Gillette','Analyst, Bomb Specialist, Case Officer, Field Agent',
             'Adam Reed',205188)
Cyril = Archer('Cyril Figgis','Comptroller','Chris Parnell',9059)
Pam = Archer('Pam Poovey','H.R. Director','Amber Nash',42424)
Cheryl = Archer('Cheryl Tunt','Secretary','Judy Greer',50390)
Krieger = Archer('Dr. Algernop Krieger','HOD - Applied Research',
                 'Lucky Yates',105526)

print(Lana.post)
print(Archer.number_of_char)
print(Krieger.name)
print(Malory.full_profile())