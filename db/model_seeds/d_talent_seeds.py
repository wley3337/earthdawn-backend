talent_seeds_d = [
    {
        "id":
        "TD1",
        "name":
        "Dead Fall",
        "attribute":
        "willpower",
        "action":
        False,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["illusionist"],
        "description":
        """A character uses the Dead Fall talent to feign death. As the character collapses, he makes a Dead Fall Test against the highest Spell Defense of any character who sees him. If the test succeeds, he uses minor illusion magic to exaggerate the appearance of any wound, poison, or disease effect to persuade observers that he is really dead. The effect lasts for a number of rounds equal to the character's rank in Dead Fall. The Dead Fall talent may be used repeatedly by making additional Talent Tests to maintain the illusion each time the duration of the talent ends. If the character's Dead Fall Test is not successful, at least one observer realizes that the character is faking."""
    },
    {
        "id":
        "TD2",
        "name":
        "Detect Trap",
        "attribute":
        "perception",
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": [],
        "description":
        """The Detect Trap talent allows a character to uncover hidden traps, both mechanical and magical. The average Difficulty Number for mechanical traps is 5, though some may be as high as 9. The Difficulty Number for magical traps is equal to the trap's Spell Defense. A successful Detect Trap Test enables the character to notice some aspect of the trap, usually the trigger.
A better-than-Average success level provides the character with additional information about the trap. On a Good success, the character can pinpoint the trap's trigger and figure out how to avoid setting it off. An Excellent success tells the character what type of effect (i.e., crushing, smashing, poison, and so on) the trap uses. An Extraordinary success gives the character a step bonus equal to the character's rank in Detect Trap when disarming the trap. The character adds the bonus to any tests he or she makes when attempting to disarm the trap."""
    },
    {
        "id":
        "TD3",
        "name":
        "Detect Weapon",
        "attribute":
        "perception",
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": [],
        "description":
        """The Detect Weapon talent allows a character to notice hidden weapons, whether concealed by normal or magical means. The character makes a Detect Weapon Test against the weapon's Concealment Difficulty Number (see Conceal Weapon). With a successful test, the character spots the weapon and knows its type. The character cannot detect a weapon's magical abilities using this talent.
Once the character detects a weapon, he becomes alert to possible treachery. This alertness lasts for a number of minutes equal to the result of the Detect Weapon Test. If the character carrying the detected weapon tries to initiate combat, the alerted character has a first-round Initiative step bonus equal to his rank in Detect Weapon."""
    },
    {
        "id":
        "TD4",
        "name":
        "Direction Arrow",
        "attribute":
        "perception",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        4,
        "discipline_talent": ["archer"],
        "description":
        """Using the Direction Arrow talent, a character can locate another character or an object. The character must first possess a piece of clothing or a piece of wall from a building or something else directly connected to the person or object he seeks. The character fires an arrow straight up into the air. The arrow rises to its full height, then plummets to the earth. When it hits the ground, it shatters and sparks into an flaming arrow 1 yard long. The character makes a Direction Arrow Test against the Spell Defense of the person or object being sought. If the test succeeds, the arrow points in the right direction. Each success level beyond Average reduces the amount of Strain the character takes when using this talent. For example, a Good success reduces the Strain to 3 points, an Excellent success reduces the Strain to 2 points, and so on.
The person or object must be within a number of miles equal to the character's rank in Direction Arrow for the talent to work. Thus, a character with Rank 4 Direction Arrow could look for a person who is up to 4 miles away."""
    },
    {
        "id":
        "TD5",
        "name":
        "Disarm",
        "attribute":
        "dexterity",
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["swordmaster"],
        "description":
        """The Disarm talent uses a combination of flashing swordplay and instinctive levitation magic to help a character to knock the weapon from an opponent's hand. After first declaring that he intends to use the Disarm talent, the character makes his Attack Test using the Disarm talent step. A successful result sends the weapon spinning away from the opponent in the direction the Disarming character chooses. Make a Damage Test for the number of feet the weapon flies. The Disarm talent does not effect any weapon that is part of the defender, such as an animal's claws."""
    },
    {
        "id":
        "TD6",
        "name":
        "Disarm Mechanical Trap",
        "attribute":
        "dexterity",
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["thief"],
        "description":
        """Characters with the Disarm Mechanical Trap talent use deduction, dexterity, and a magical touch to render mechanical traps inoperative. The character makes a Talent Test against the trap's Difficulty Number (determined by the gamemaster when creating the trap; see Adventuring in Earthdawn for information about traps). A successful result disables the trap's trigger, preventing it from going off."""
    },
    {
        "id":
        "TD6",
        "name":
        "Disguise",
        "attribute":
        "perception",
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": [],
        "description":
        """The Disguise talent allows a character to use costumes and make-up to portray other people. The character needs make-up, clothing, jewelry, and other physical components of the disguise to use this talent. If the character is disguising himself as a specific individual, he must have seen a painting or other image of that individual. When using the disguise, the character makes a Disguise Test against the target's Spell Defense. If attempting to fool more than one character, use the highest Spell Defense of the group +1 for each additional character targeted. A successful test result means the targeted characters believe the disguise. The Disguise talent lasts for a number of hours equal to the character's rank in Disguise, but the character must pay the Strain cost each time he makes a Disguise Test to see if another character believes the disguise."""
    },
    {
        "id":
        "TD7",
        "name":
        "Disguise Self",
        "attribute":
        "perception",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        0,
        "discipline_talent": ["illusionist"],
        "description":
        """The Disguise Self talent allows a character to use illusion magic to disguise herself as any human-like being, within the limits of the talent. The disguised being can weigh up to twice the character's weight, but not less than half. The character may not vary the height, width, or length of any part of his body by more than 25 percent. For example, a human character trying to disguise himself as a t'skrang would have an awfully short tail.
The character makes a Disguise Self Test. The effect lasts for a number of hours equal to the result of the Disguise Self Test or until the character chooses to drop the disguise.
The required Karma Point is not spent for the Talent Test. Instead, the disguised character rolls the Karma dice and adds the result to the Sensing and Disbelief Difficulty Numbers of the illusion (see Spell Magic). For the purposes of Sensing and Disbelief Tests against the disguised character, consider the Disguise Self Talent a Circle 3 illusion spell."""
    },
    {
        "id":
        "TD8",
        "name":
        "Dominate Beast",
        "attribute":
        "charisma",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["beastmaster"],
        "description":
        """The Dominate Beast talent allows a character to temporarily subdue and control an animal, wild or trained. If the character makes a successful Dominate Beast Test against the animal's Spell Defense, he can establish dominance over the animal for a number of minutes equal to his or her rank in Dominate Beast. An animal under the effect of Dominate Beast will not take any hostile action against the character using the talent. The character may command the creature to perform one simple task that requires less time than the duration of Dominate Beast. The task cannot pose more danger to the animal than to the character."""
    },
    {
        "id":
        "TD9",
        "name":
        "Down Strike",
        "attribute":
        "strength",
        "base_modifier":
        3,
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
        """The Down Strike talent allows a character to inflict greater-than-normal damage on a target in combat. The character must be using the Gliding Stride Talent or using another talent to move at least 6 feet above the head of his opponent. The character must scream like a bird of prey as he drops onto his target. If he hits his opponent, the Down Strike step substitutes for the Strength step in the Damage Test, causing the blow to inflict extra damage."""
    },
    {
        "id":
        "TD10",
        "name":
        "Durability",
        "attribute":
        "",
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
        """Each rank of the Durability talent permanently increases a character's Death and Unconsciousness Ratings. The character's Discipline determines the amount of this increase. The list below gives each Discipline and the appropriate increase per Durability Rank listed as two numbers separated by a slash. The number to the left of the slash represents the increase to the character's Death Rating. The number to the right is the increase to the character's Unconsciousness Rating.
Discipline/Death/Unconsciousness
Archer 6/5
Beastmaster 7/6
Cavalryman 7/6
Elementalist 4/3
Illusionist 4/3
Nethermancer 4/3
Sky Raider 8/6
Swordmaster 7/6
Thief 5/4
Troubadour 6/5
Warrior 9/7
Weaponsmith 6/5
Wizard 4/3
List this talent on the character record sheet as "Discipline Name" Durability (i.e., Archer
Durability, Sky Raider Durability, and so on)."""
    },
    {
        "id":
        "TD11",
        "name":
        "Durability (Mount)",
        "attribute":
        "",
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
        """The Durability (Mount) talent is a variation of the Durability talent (see above). Each rank of Durability (Mount) increases a mount's Death Rating by 5 and its Unconsciousness Rating by 4. A character may transfer this talent from one mount to another, but only one mount at a time may benefit. The Durability (Mount) Talent only works for living mounts, not mechanical, undead, or spirit mounts."""
    },
]
