##ARCHER
##create profiles for the main characters

class Archer:
    number_of_char = 0
    #pay=0
    def __init__(self,name, post, voice, k_401,special_trait):
        self.name=name
        self.post=post
        self.voice=voice
        self.k_401=k_401
        self.special_trait=special_trait

        ##
        Archer.number_of_char+=1

    def weapon(self,weapon):
        self.weapon=weapon
        return 'Weapn'+self.weapon

    def full_profile(self):
        message = '\nName-> '+self.name+'\nPost-> '+self.post+'\nVoice-> '\
                   +self.voice+'\n401(k)-> '+f'{self.k_401:,d}'+'$'+'\nSpecial_trait -> '\
                  +self.special_trait
        return message
    ##f-string used to split the number -> f'{self.k_401:,d}'


class Field_Agent(Archer):
    def __init__(self, name,post,voice,k_401,weapon,special_trait):
        super().__init__(name,post, voice,k_401,special_trait)
        self.weapon=weapon
    def prof(self):
        return Archer.full_profile(self)+'\nWeapon -> '+self.weapon



Sterling = Field_Agent('Sterling Archer','Field Agent, Protagonist',
                  'H.Jon Benjamin',480810,'Walther PPK','Tinnitus')
Lana = Field_Agent('Lana Kane','Field Agent, Deuteragonist','Aisha Tyler',420675,'TEC-9','Big hands')
Malory = Archer('Malory Archer','CEO','Jessica Walter',2302725,'Micro-management')
Ray = Archer('Ray Gillette','Analyst, Bomb Specialist, Case Officer, Field Agent',
             'Adam Reed',205188,'Bionic legs')
Cyril = Archer('Cyril Figgis','Comptroller','Chris Parnell',9059,'Sex-addict')
Pam = Archer('Pam Poovey','H.R. Director','Amber Nash',42424,'Farm-Girl')
Cheryl = Archer('Cheryl Tunt','Secretary','Judy Greer',50390,'Snot Gum, Choking')
Krieger = Archer('Dr. Algernop Krieger','HOD - Applied Research',
                 'Lucky Yates',105526,'Hitler\'s Clone')


print(Cheryl.post)
print(Archer.number_of_char)
print(Krieger.full_profile())
print(Malory.full_profile())
print(Lana.prof())

print('\n',Sterling.name,'-',Sterling.weapon)

