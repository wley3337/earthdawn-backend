talent_seeds_m = [
    {
        "id":
        "TM1",
        "name":
        "Maneuver",
        "attribute":
        "dexterity",
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
        "discipline_talent": ["swordmaster"],
        "description":
        """When using the Maneuver talent, the character sacrifices his attack to try to avoid attacks made against him. The character must direct the Maneuver talent against one opponent. The character makes a Maneuver Action Test instead of an Attack Test, using the result of the test as his or her Physical Defense for the round even if the result is lower than his normal Physical Defense. If the character avoids all attacks during the round in which he uses Maneuver, in the next round he adds his rank in Maneuver talent to the result of the next Attack Test he makes against the opponent he out-maneuvered. If this attack hits, the character also adds his Maneuver Rank to the Damage Test result."""
    },
    {
        "id":
        "TM2",
        "name":
        "Melee Weapons",
        "attribute":
        "dexterity",
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
        "discipline_talent": ["sky_raider", "swordmaster", "warrior"],
        "description":
        """A character uses the Melee Weapons talent to hit a target using a hand-held weapon. The character makes a Melee Weapons Test against the Physical Defense of the target. A successful test means the attack hits the target."""
    },
    {
        "id":
        "TM3",
        "name":
        "Memorize Image",
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
        """The Memorize Image talent stores an image in a character's mind. The character can later recall the image to form the central image for an illusion. A character memorizes an image while watching a person or event. The character makes a Memorize Image Test and compares the result to the Learning Difficulty of the appropriate spell. The image can be used in an illusion spell whose Learning Difficulty is equal to or less than the Memorize Image Test result.
Example: Enyiat, an Illusionist, sees a spectacular river of fire near Death's Sea and decides to memorize the image. She makes a Memorize Image Test with a result of 12. Enyiat's player compares this result to the Spell Difficulty Table in the Spell Magic section, and sees that Enyiat has memorized the image well enough to use it as the basis for illusions of Circle 4 or less.
Increase the Difficulty Number for tests made to disbelieve illusions based on a memorized image by the character's rank in Memorize Image. The number of images a character may memorize at one time is equal to his talent rank. Characters may choose this talent more than once; high-ranking Illusionists often have 3 or 4 Memorize Image talents of various ranks, which allows them to store many images."""
    },
    {
        "id":
        "TM4",
        "name":
        "Metal Ward",
        "attribute":
        "perception",
        "base_modifier":
        5,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        2,
        "discipline_talent": ["elementalist"],
        "description":
        """The Metal Ward talent reduces damage from attacks made using any form of metal, including weapons, spikes in pit traps, and so on, by increasing a character's Physical Armor Rating by the Metal Ward Rank. To use Metal Ward, the character makes a Metal Ward Test. The effects of Metal Ward last a number of hours equal to the result"""
    },
    {
        "id":
        "TM5",
        "name":
        "Mimic Voice",
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
        "discipline_talent": ["troubadour"],
        "description":
        """The Mimic Voice talent gives a character the ability to mimic any voice he or she hears. A character uses the Mimic Voice talent both to learn the voice and to mimic it. When a character hears a voice he wants to mimic, he makes a Mimic Voice Test against the speaker's Spell Defense to learn the voice. A successful test means the character can mimic the voice any time during the next 24 hours.
When attempting to fool a target by mimicking the voice, the character makes a Mimic Voice Test against the Social Defense of the target. If the test is a success, the target believes he is hearing the person to whom the voice belongs, rather than the character. If the Mimic Voice talent is used against more than 1 target, make the Talent Test against the highest Social Defense among the target group + 1 for each additional character targeted. If the target characters have strong physical evidence that the voice is being mimicked, such as the character standing before them in his normal appearance while using the talent, they may make a Willpower Test against the result of the Mimic Voice Test to disbelieve the effect. If the test is successful, they reject the effect of Mimic Voice.
If the character does not understand the language of the person whose voice he is trying to mimic, Mimic Voice produces the equivalent of baby babble; the sounds are right, but the words don't mean much."""
    },
    {
        "id":
        "TM6",
        "name":
        "Mind Wave",
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
        "discipline_talent": ["illusionist"],
        "description":
        """The Mind Wave talent allows a character to confuse and confound a target. To use this talent, the character must win Initiative over his intended target. The character makes a Mind Wave Test against the target's Spell Defense. If the test is successful, it washes away all thoughts from the target's mind. He completely loses his train of thought, but the magic washing away his thoughts is a vaguely pleasant sensation. The effect lasts for a number of rounds equal to the character's rank in Mind Wave. A character using Mind Wave cannot take part in any social interactions, such as persuasion or intimidation. The range of this talent is 1 yard. Mind Wave cannot be used during combat."""
    },
    {
        "id":
        "TM7",
        "name":
        "Missile Weapons",
        "attribute":
        "dexterity",
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
        "discipline_talent": ["archer"],
        "description":
        """A character uses the Missile Weapons talent to fire bows, crossbows, and other ranged weapons. The character makes a Missile Weapons Test against the Physical Defense of the target. If the result is equal to or higher than the target's Physical Defense, the attack hits. The Missile Weapons talent cannot be used with thrown weapons such as daggers and knives."""
    },
    {
        "id":
        "TM8",
        "name":
        "Momentum Attack",
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
        "discipline_talent": ["sky_raider"],
        "description":
        """The Momentum Attack talent allows a character to make a second melee weapon attack against an opponent in the same round. The character makes a Melee Weapons Test. On an Extraordinary success, he may choose to make a Momentum Attack Test against the same opponent. Using Momentum Attack allows the character to make a second Attack while his opponent attempts to recover from the effects of the first blow. The character makes a Momentum Attack Test for the second attack, determining damage normally. Damage bonuses earned for the first attack do not carry over to the Momentum Attack; for example, if the character uses the Crushing Blow talent with the first attack, he does not add that damage on to the Momentum Attack."""
    },
    {
        "id":
        "TM9",
        "name":
        "Mount Attack",
        "attribute":
        "mount_strength",
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
        "discipline_talent": ["cavalryman"],
        "description":
        """The Mount Attack talent increases the strength of a mount for the purpose of determining damage. The character makes a Mount Attack Test against the Spell Defense of the mount. If the test is successful, add the rank of the Mount Attack talent to the mount's Strength step when making Damage Tests for the mount. If a mount does not normally make Attack Tests, this talent gives the animal one attack; use the mount's Dexterity step to make the attack. A single use of the Mount Attack talent lasts a number of rounds equal to the character's rank in Mount Attack."""
    },
    {
        "id":
        "TM10",
        "name":
        "Mystic Aim",
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
        "discipline_talent": ["archer"],
        "description":
        """The Mystic Aim talent allows a character to draw a steady aim on a target when using a missile weapon. The character spends a round aiming at a target within line-of-sight. The character makes a Mystic Aim Test against the target's Spell Defense. If the test is successful, a small visible mark appears on the target and the character adds a bonus equal to his Mystic Aim Rank to his Missile Weapons step. This bonus lasts until the character fires his weapon or until the target moves out of line-of-sight.
The mark created on the target by Mystic Aim is unique to the character using the talent. The mark may appear as plain white dots or as a symbol from the character's town or village."""
    },
]
