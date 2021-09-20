talent_seeds_s = [
    {
        "id":
        "TS1",
        "name":
        "Safe Path",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        0,
        "discipline_talent": [],
        "description":
        """The Safe Path talent allows a character to determine the safest path through unfamiliar territory by contacting an elemental spirit. (The character does not conjure the elemental, only establishes mental contact with it.) Sometimes the elemental animates a part of the landscape nearby, making its conversation audible to other characters. The character using the talent rolls his Safe Path dice. The result is the number of miles of safe pathway the elemental can predict. The elemental tells the character which is the safest path to take and what possible elemental dangers and/or natural beasts might lie ahead. For example, a dice roll of 21 means the elemental can direct your character to the safest route in the direction your character wants to go for at least the next 21 miles. If an obstacle lurks at mile 25, or even 22, the elemental will not be able to give your character even a hint about it. Keep in mind that what an elemental considers dangerous is probably vastly different than what poses danger to an adventurer. An elemental's knowledge of an area is also limited by its type. Earth elementals probably know nothing of flying or swimming dangers, but may be able to describe exactly the kinds of arms and armor nearby groups carry. Even that information cannot indicate the intentions of these other groups."""
    },
    {
        "id":
        "TS2",
        "name":
        "Second Attack",
        "attribute":
        "dexterity",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        True,
        "requires_karma":
        True,
        "strain":
        1,
        "discipline_talent": ["swordmaster"],
        "description":
        """The Second Attack talent allows a character to make a second attack in a round. For the second attack, the character makes a Second Attack Test for the same weapon he used in the first attack. The Second Attack talent cannot be used in the same round as another talent that gives a character an additional attack, such as Momentum Attack or Second Weapon. The damage of a Second Attack is the same as for a normal Attack Test."""
    },
    {
        "id":
        "TS3",
        "name":
        "Second Weapon",
        "attribute":
        "dexterity",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["swordmaster"],
        "description":
        """The Second Weapon talent allows a character to attack with two different weapons in the same round. To use this talent, the character holds one weapon in each hand. The Second Weapon must be at least one size smaller than the character's primary weapon (see the Goods and Services Table). The character must be able to wield either weapon with only one hand. When attacking using the Second Weapon talent, the character uses the Second Weapon step number for the Attack Test but determines damage normally."""
    },
    {
        "id":
        "TS4",
        "name":
        "Sense Poison",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["beastmaster"],
        "description":
        """The Sense Poison talent detects poisons in food, drink, and even the air. A character must be able to sniff the target substance to use the Sense Poison talent. The character makes a Sense Poison Test against the poison's Spell Defense; in the case of a poison stinger or poisoned weapon, he rolls against the Spell Defense of the creature or character. A successful test result means the character detects poison on the target substance, object, or character. The range at which the character can detect the poison equals the character's Sense Poison Rank x 10 yards. If the target carries the poison in a tightly sealed container such as a vial, or if the poison comprises a natural part of an animal, such as venom in a spider, increase the Difficulty Number to sense the poison by +5."""
    },
    {
        "id":
        "TS5",
        "name":
        "Shield Charge",
        "attribute":
        "strength",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["sky_raider"],
        "description":
        """The Shield Charge talent allows a character to make an attack using his shield. The character makes a standard Attack Test using the Melee Weapons Talent (p. 111) to hit. The character uses the Shield Charge dice for damage, rather than making a normal Damage Test. A successful attack with Shield Charge does normal damage, but increases the Knockdown Number by +7 (see Make Knockdown Test in the Combat section).
Example: Targ Boneslicer uses the Shield Charge talent to attack an espargra. He hits the creature, and then rolls the Shield Charge dice for a total of 25, modified to 18 points of damage by the espargra's armor. The creature's Wound Threshold is 7, giving it a Knockdown Number of 14. Because Targ used Shield Charge, the espargra must make a successful Knockdown Test against a Difficulty Number of 21."""
    },
    {
        "id":
        "TS6",
        "name":
        "Silent Walk",
        "attribute":
        "dexterity",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["thief"],
        "description":
        """The Silent Walk talent combines fluid movement with magical effects to dampen the sound of a character's movement, including footsteps and other means of travel, such as the sound of a windling's flight. The character rolls the Silent Walk dice to avoid detection. Use the result as the Difficulty Number for any characters attempting to detect the character via a Perception Test or other ability.A character using Silent Walk can move a maximum distance equal to his or her Combat Movement."""
    },
    {
        "id":
        "TS7",
        "name":
        "Speak Language",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        1,
        "discipline_talent": ["troubadour"],
        "description":
        """The Speak Language talent allows a character to magically and permanently learn to speak a new language. Each rank of the talent allows the character to learn one new language. If the character has a rank of Speak Language available, he can the learn the new language. Once a rank is assigned to a language, it cannot be used to learn any other language. To learn a language, the character must hear 1 minute of conversation in the language. The character makes a Speak Language Test against the Difficulty Number shown below. (The Difficulty Numbers refer to the standard languages. Each racial language has many variations. If a character is attempting to learn a variation of a language, add +2 to the Difficulty Number.) A successful test means the character can now speak and understand the language. The player should record which languages his character speaks on the Character Record Sheet.
Language/Difficulty
Dwarven 5
Elvish (Sperethiel) 6
Human 6
Obsidimen 7
Ork 6
Troll 6
T'skrang 7
Windling 7
When speaking or listening to the new language, the character makes a Speak Language Test to see how well he or she is communicating. The dice result determines the level of communication. Simple sentences or ideas, such as "Which way to the sheriff?" only require a result of 2. Normal conversation that includes idioms or jargon requires a result of 6. Technical conversations or other discussions filled with specialized jargon require a result of 10. Conversations about philosophical topics or other abstract ideas require a result of 13. One Speak Language Test allows the character to communicate for a number of minutes equal to his or her Speak Language rank."""
    },
    {
        "id":
        "TS8",
        "name":
        "Spellcasting",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent":
        ["elementalist", "illusionist", "nethermancer", "wizard"],
        "description":
        """A character uses the Spellcasting talent to cast spells. The character makes a Spellcasting Test. If the result is equal to or greater than the target's Spell Defense Rating, the Spellcasting Test succeeds."""
    },
    {
        "id":
        "TS9",
        "name":
        "Spell Matrix",
        "attribute":
        "",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": [],
        "description":
        """A Spell Matrix is an astral construct that allows magicians to cast spells without interference from the denizens of astral space. A magician may only use a spell after he or she places it into a Spell Matrix. Each Spell Matrix represents a separate talent with its own rank. See the Circle summary of a magician's Discipline to determine how many Spell Matrices he or she may hold at a given time. For example, a First Circle Wizard can have up to two Spell Matrices. The player purchases ranks for Spell Matrices in the same way as for other talents. The rank of each Spell Matrix determines the Circle of spells it can hold. A Rank 1 Spell Matrix can hold only First Circle spells. See the Spell Magic section for more details on Spell Matrices."""
    },
    {
        "id":
        "TS10",
        "name":
        "Spirit Dodge",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["nethermancer"],
        "description":
        """Note: 1 strain per role.
Using the Spirit Dodge talent, the character conjures a spirit that protects him in combat. The character rolls the Spirit Dodge dice, automatically conjuring the spirit. The spirit rests within the character for a number of hours equal to the dice result or until dismissed by the character.When the character using the talent engages in combat, the spirit conjured by Spirit Dodge automatically tries to avoid any blow that would otherwise strike the character.
When an opponent hits the character with an attack, the character makes a Spirit Dodge Test and compares the result to the opponent's Attack Test. If the character's test result is greater than the attacker's, the attack misses. Each time the character makes a Spirit Dodge Test to avoid a blow, the Strain causes 1 point of damage. However, the Spirit Dodge does not count as the character's Action; he remains free to cast a spell, fight, or take some other Action."""
    },
    {
        "id":
        "TS11",
        "name":
        "Spirit Hold",
        "attribute":
        "willpower",
        "base_modifier":
        5,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["nethermancer"],
        "description":
        """The Spirit Hold talent allows a character to root a restless spirit or entity to one spot, preventing it from moving or taking any Action other than communicating. Spirit Hold works on any creature from astral space and undead creatures. The spirit must be within 10 yards of the character using the Spirit Hold talent. The character must boldly face the spirit, order it to halt, then make a Spirit Hold Test against the Spell Defense of the spirit. If the test is successful, the spirit is held for a number of rounds equal to the character's Spirit Hold Rank. During this time, the character must concentrate to hold the spirit. He cannot move, cast spells, or take any action other than communication. """
    },
    {
        "id":
        "TS12",
        "name":
        "Spirit Mount",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["cavalryman"],
        "description":
        """The Spirit Mount talent allows a character to conjure a mount to ride. The character makes a Spirit Mount Test against a Conjuring Difficulty Number of 8. A successful test conjures a spirit mount "whose eyes are fire and whose skin is all summer lightning and fog." Spirit mounts usually take the form of horses or unicorns, but sages have recorded other shapes. Spirit mounts can walk or gallop on air when unburdened, but cannot carry riders in the air. They can sink 6 inches into the earth, allowing the mount and character to pass through corridors too short for a standard horse and rider.
No one but the conjuring character may ride the spirit mount; the spirit mount dissolves rather than obey the commands of another. A spirit mount remains in this world for a number of minutes equal to the result of the Spirit Mount Test, then melts into mist. (See Creatures for an explanation of the game statistics given below.)

Spirit Mount
DEX: 5   STR: 4   TOU: 5
PER: 4   WIL: 6   CHA: 2

Physical Defense: 8, Spell Defense: 8, Social Defense: 9

Combat Movement: 75
Full Movement: 150

Initiative: 7
Number of Attacks: 1
Attack: 5
Damage: 4
Armor: 0, Mystic Armor: 3
Knockdown: 7

Death Rating: 24
Unconsciousness Rating: 16
Wound Threshold: 6
Recovery Tests: 2
Experience Award: 20
    """
    },
    {
        "id":
        "TS13",
        "name":
        "Spirit Strike",
        "attribute":
        "willpower",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["sky_raider", "warrior"],
        "description":
        """The Spirit Strike talent allows a character to at strike at opponents from astral space. The character must have either the Astral Sight talent or a Thread Weaving talent in order to use Spirit Strike. The character uses the Spirit Strike step number to make an Attack Test against the Spell Defense of the target. A successful hit causes the normal damage for an attack of that type. The target's physical armor, if any, still provides protection. The character's weapon disappears from view as it enters astral space and then reemerges trailing cold green wisps of mist. Defensive talents like Avoid Blow and Riposte cannot be used against attacks made with Spirit Strike."""
    },
    {
        "id":
        "TS14",
        "name":
        "Spirit Talk",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["nethermancer"],
        "description":
        """The Spirit Talk talent allows a character to talk to spirits and entities, including those who do not speak his language and those who do not normally communicate verbally. The character makes a Spirit Talk Test against the Spell Defense of the spirit. A successful result means the character may talk to the spirit. The effect lasts a number of minutes equal to the character's rank in Spirit Talk. This talent does not compel the spirit to talk to the character, but merely makes verbal communication possible."""
    },
    {
        "id":
        "TS15",
        "name":
        "Spot Armor Flaw",
        "attribute":
        "perception",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["weaponsmith"],
        "description":
        """The Spot Armor Flaw talent allows a character to identify flaws in an opponent's armor. The character makes a Spot Armor Flaw Test against the Spell Defense of the opponent or the opponent's armor, whichever is higher. If the test is successful, the character sees chinks in his opponent's armor. Add a Damage step bonus equal to the character's rank in Spot Armor Flaw to all Attack Tests the character makes against that opponent. The effects of Spot Armor Flaw last for a number of rounds equal to the character's Spot Armor Flaw Rank."""
    },
    {
        "id":
        "TS16",
        "name":
        "Sprint",
        "attribute":
        "",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": [],
        "description":
        """The Sprint talent allows a character to temporarily increase his movement rate. Magic infuses the character with speed; each rank of Sprint increases the character's Full Movement by 20 yards per round, and his Combat Movement by 10 yards per round. The Sprint talent can be used in the same round as an Attack Test."""
    },
    {
        "id":
        "TS17",
        "name":
        "Steel Thought",
        "attribute":
        "willpower",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": [],
        "description":
        """The Steel Thought talent allows a character to increase his Mystic Armor. The character firms his resolve, figuratively forging his thoughts into tougher, more resilient patterns. The character then rolls the Steel Thought dice and substitutes the result for his Mystic Armor for a number of rounds equal to his Steel Thought Rank. The character must use this test result, even if his normal Mystic Armor Rating is higher."""
    },
    {
        "id":
        "TS18",
        "name":
        "Stopping Aim",
        "attribute":
        "charisma",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["archer"],
        "description":
        """The Stopping Aim talent allows a character to stop an opponent dead in his tracks. This talent can only be used with a bow or crossbow. The character spends a round aiming at a target within line of sight. At the end of the round, the character makes a Stopping Aim Test against the target's Social Defense. A successful test makes a small mark appear on the target, and the target stops dead in his tracks for fear of being skewered by the arrow. The target remains transfixed until the Archer moves his aim or until the target makes a successful Willpower Test against the result of the Stopping Aim Test. The effect lasts for a number of rounds equal to the Stopping Aim result."""
    },
    {
        "id":
        "TS19",
        "name":
        "Sure Mount",
        "attribute":
        "strength",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["cavalryman"],
        "description":
        """The Sure Mount talent helps a character stay on his mount during combat. The character makes a Sure Mount Test in place of any Knockdown Tests required during combat or any other time he might be knocked from the mount. The Sure Mount Talent also helps the character control a mount panicked by natural or magical events. To use this talent to control a mount, the character makes a Sure Mount Test against the Strength step of the mount. A successful test means the character gains control over his mount and magically calms the beast. """
    },
    {
        "id":
        "TS20",
        "name":
        "Surprise Strike",
        "attribute":
        "dexterity",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        Yes,
        "strain":
        0,
        "discipline_talent": ["thief"],
        "description":
        """The Surprise Strike talent allows characters to take advantage of the element of surprise. When using this talent, characters use the Surprise Strike step for the Attack Test. Surprise Strike may only be used once on any one target in one encounter. Add 7 steps to the damage step for the Damage Test. The Karma dice apply to the Surprise Strike Test, not the Damage Test."""
    },
    {
        "id":
        "TS21",
        "name":
        "Swift Kick",
        "attribute":
        "dexterity",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["warrior"],
        "description":
        """The Swift Kick talent grants the character an extra attack when using Unarmed Combat if his Initiative comes before that of his opponent. If the character wins Initiative, he may choose to make a Swift Kick attack in addition to his normal attack. The character makes a Swift Kick Test as the additional Attack Test. Use the character's Strength step as the Damage step for the Swift Kick attack. The t'skrang may make this attack with their tails."""
    },
]
