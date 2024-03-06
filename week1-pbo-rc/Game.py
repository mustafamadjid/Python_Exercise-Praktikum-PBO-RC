class greekFight:
    def __init__(self,fighter_name, health, attack_power,armor):
        self.name = fighter_name
        self.health = health
        self.attack_power = attack_power
        self.armor = armor
        
    
    def show_fighter_info (self):
        print(f"Fighter Name  : {self.name}")
        print(f"Health        : [{self.health}]")
        print(f"Attack Power  : [{self.attack_power}]")
        print(f"Armor         : [{self.armor}]")
    
    
    def attack(self, enemy):
        print(f"{self.name} attacked {enemy.name}")
        
        enemy.health -= int((self.attack_power/enemy.armor))
        print(f"{enemy.name}'s Health  -{int(self.attack_power/enemy.armor)}")
        print(f"{enemy.name}'s Health[{enemy.health}] \n")
        
        enemy.counter_attack(self)    
    
    
    def counter_attack(self,enemy):
        print(f"{self.name} counter attacked {enemy.name}")
        
        enemy.health -= int((self.attack_power/enemy.armor))
        print(f"{enemy.name}'s Health  -{int(self.attack_power/enemy.armor)}")
        print(f"{enemy.name}'s Health[{enemy.health}]")
        
            
            
fighter_list = []

zeus = greekFight("ZEUS",1000,500,10)
ares = greekFight("ARES",500,250,5)
kratos = greekFight("KRATOS",760,320,6 )
poseidon = greekFight("POSEIDON",550,277,8)

fighter_list.append(zeus)
fighter_list.append(ares)
fighter_list.append(kratos)
fighter_list.append(poseidon)


print("=== FIGHTER LIST ===")
print()
for fighter in fighter_list:
   fighter.show_fighter_info()
   print()
    
choose_fighter = input("Choose your fighter (write down the fighter's name)   : ")
choose_enemy   = input("Choose your enemy (write down the enemy's name)       : ")

chosen_fighter = None
chosen_enemy = None

for fighter in fighter_list:
    if fighter.name.lower() == choose_fighter.lower():
        chosen_fighter = fighter
    if fighter.name.lower() == choose_enemy.lower():
        chosen_enemy = fighter 
print()


if chosen_fighter and chosen_enemy:
    print(f"You chose {chosen_fighter.name} as your fighter")
    print(f"You chose {chosen_enemy.name} as your enemy")
    print("Let's start !\n\n")
else:
    print("Invalid Fighter Or Enemy !")
    

winner = None
while (chosen_fighter.health > 0 ) and (chosen_enemy.health > 0):
    input_option = int(input("Press 1 to attack : "))
    
    print()
    if input_option == 1:
        chosen_fighter.attack(chosen_enemy)
        print()
    else:
        print("Invalid !")
        break
    
    if chosen_fighter.health == 0:
        winner = chosen_enemy
    else:
        winner = chosen_fighter


print(f"====THE WINNER IS====")
print(f"\t{winner.name}")

