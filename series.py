##ARCHER
##create profiles for the main characters

class Character:
    number_of_char = 0

    # pay=0
    def __init__(self, name, post, voice, k_401, special_trait):
        self.name = name
        self.post = post
        self.voice = voice
        self.k_401 = k_401
        self.special_trait = special_trait

        ##
        Character.number_of_char += 1

    # def weapon(self,weapon):
    #     self.weapon=weapon
    #     return 'Weapon'+self.weapon

    def full_profile(self):
        message = f'\nName - > {self.name}\nPost -> {self.post}\nVoice -> {self.voice}\n' \
                  f'401(k) -> {self.k_401:,d}$\nSpecial trait -> {self.special_trait}'
        return message
    ##f-string used to split the number -> f'{self.k_401:,d}'


class Field_Agent(Character):
    def __init__(self, name, post, voice, k_401, weapon, special_trait):
        super().__init__(name, post, voice, k_401, special_trait)
        self.weapon = weapon

    def prof(self):
        return f'{Character.full_profile(self)}\nWeapon -> {self.weapon}\n'


##number of seasons and episodes
##seasons=9: 1,7 -> 10,2-6 -> 13, 8-9 -> 8
class Season:
    # so that you can show the episodes in every season
    # and can show the exact episode's name---has a bug
    number_of_seasons = 0
    episode_dict = {}

    # episodes to be inputed as a list hence the episodes=[]
    def __init__(self, number, name, no_of_episodes, episodes=[]):
        self.number = number
        self.name = name
        self.no_of_episodes = no_of_episodes
        self.episodes = episodes
        Season.number_of_seasons += 1

    def episode_number_and_name(self):
        # add and assign all episodes to the numbers
        try:
            for i in range(self.no_of_episodes):
                Season.episode_dict[i + 1] = self.episodes[i]
            return Season.episode_dict
        except IndexError:
            return f'Number of episodes NOT equal to episodes'

    # show episode name of the ep number
    def display_episode(self, e_number):
        return self.episodes[e_number - 1]

    def show_season_details(self):
        return f'Season -> {self.number}: {self.name}\nNo. of episodes -> {self.no_of_episodes}' \
               f'\n{Season.episode_number_and_name(self)}\n'


# Archer

Sterling = Field_Agent('Sterling Archer', 'Field Agent, Protagonist',
                       'H.Jon Benjamin', 480810, 'Walther PPK', 'Tinnitus')
Lana = Field_Agent('Lana Kane', 'Field Agent, Deuteragonist', 'Aisha Tyler', 420675, 'TEC-9', 'Big hands')
Malory = Character('Malory Archer', 'CEO', 'Jessica Walter', 2302725, 'Micro-management')
Ray = Character('Ray Gillette', 'Analyst, Bomb Specialist, Case Officer, Field Agent',
                'Adam Reed', 205188, 'Bionic legs')
Cyril = Character('Cyril Figgis', 'Comptroller', 'Chris Parnell', 9059, 'Sex-addict')
Pam = Character('Pam Poovey', 'H.R. Director', 'Amber Nash', 42424, 'Farm-Girl')
Cheryl = Character('Cheryl Tunt', 'Secretary', 'Judy Greer', 50390, 'Snot Gum, Choking')
Krieger = Character('Dr. Algernop Krieger', 'HOD - Applied Research',
                    'Lucky Yates', 105526, 'Hitler\'s Clone')

# Season class

Season_1 = Season(1, 'Archer', 10, ['Mole hunt', 'Training Day', 'Diversity Hire',
                                    'Killing Utne', 'Hooneypot', 'Skorpio', 'Skytanic',
                                    'The Rock', 'Job Offer', 'Dial M for Mother'])

Season_2 = Season(2, 'Archer 2', 13, ['Swiss Miss', 'A Going Concern', 'Blood Test',
                                      'Pipeline Fever', 'The Double Deuce', 'Tragical History',
                                      'Movie Star', 'Stage Two', 'Placebo Effect', 'El Secuestro',
                                      'Jeu Monegasque', 'White Nights', 'Double Trouble'])

Season_3 = Season(3, 'Archer 3', 13, ['Heart of Archness: Part I', 'Heart of Archness: Part II',
                                      'Heart of Archness: Part III', 'The Man from Jupiter',
                                      'El Contador', 'The Limited', 'Drift Problem', 'Lo Scandalo',
                                      'Bloody Ferlin', 'Crossing Over', 'Skin Game',
                                      'Space Race: Part I', 'Space Race: Part II'])

Season_4 = Season(4, 'Archer 4', 13, ['Fugue and Riffs', 'The Wind Cries Mary', 'Legs', 'Midnight Ron',
                                      'Viscous Coupling', 'Once Bitten', 'Live and Let Dine',
                                      'Coyote Lovely', 'The Honeymooners', 'Un Chien Tangerine',
                                      'The Papal Chase', 'Sea Turnt: Part I', 'Sea Turnt: Part II'])

Season_5 = Season(5, 'Archer Vice', 13, ['White Elephant', 'A Kiss While Dying', 'A Debt of Honor',
                                         'House Call', 'Southbound and Down', 'Baby Shower',
                                         'Smugglers\' Blues', 'The Rules of Extraction', 'On the Carpet',
                                         'Palace Intrigue: Part I', 'Palace Intrigue: Part II',
                                         'Filibuster', 'Arrival/Departure'])
Season_6 = Season(6, 'Archer 6', 13, ['The Holdout', 'Three to Tango', 'The Archer Sanction',
                                      'Edie\'s Wedding', 'Vision Quest', 'Sitting', 'Nellis', 'The Kanes',
                                      'Pocket Listing', 'Reignition Sequence', 'Achub Y Morfilod',
                                      'Drastic Voyage: Part I', 'Drastic Voyage: Part II'])
Season_7 = Season(7, 'Archer 7/P.I', 10, ['The Figgis Agency', 'The Handoff', 'Deadly Prep',
                                          'Motherless Child', 'Bel Panto: Part I', 'Bel Panto: Part II',
                                          'Double Indecency', 'Liquid Lunch', 'Deadly Velvet: Part I',
                                          'Deadly Velvet: Part II'])
Season_8 = Season(8, 'Archer Dreamland', 8, ['No Good Deed', 'Berenice', 'Jane Doe', 'Ladyfingers',
                                             'Sleepers Wake', 'Waxing Gibbous', 'Gramercy, Halberg',
                                             'Auflosung'])
Season_9 = Season(9, 'Archer Danger Island', 8, ['Strange Island', 'Disheartening Situation',
                                                 'Different Modes of Preparing Fruit', 'A Warrior in Costume',
                                                 'Strange Doings in the Taboo Groves', 'Some Remarks on Cannibalism',
                                                 'Comparative Wickedness of Civilized and Unenlightened Peoples',
                                                 'A Discovery'])

# Archer class
print(Cheryl.post)
print(Character.number_of_char)
print(Krieger.full_profile())
print(Malory.full_profile())
print(Lana.prof())
print(f'{Sterling.name}-{Sterling.weapon}')

# Season class
print(Season_7.show_season_details())
print(Season_2.show_season_details())
print(Season.number_of_seasons)

# Episode
print(Season_9.display_episode(3))
print(Season_5.display_episode(7))
