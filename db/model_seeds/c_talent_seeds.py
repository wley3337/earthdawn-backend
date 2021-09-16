talent_seeds_c = [
    {
        "id":
        "TC1",
        "name":
        "Call Arrow",
        "attribute":
        "perception",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["archer"],
        "description":
        """The Call Arrow talent allows a character to retrieve fired arrows by spending 1 round to call back arrows he has fired. The talent works on any arrows the character fired that remain within 100 yards of him or her. The called arrows fly toward the character, tumbling and rotating into proper position, then drop into the quiver. Call Arrow only retrieves the arrows; the character cannot also tie or attach the called arrows to another object in an attempt to retrieve that object. Call Arrow also extracts arrows from targets and returns them to the character. To use this talent, the character makes a Call Arrow Test; the result is the maximum number of arrows returned. If the character fired fewer arrows than that number, he or she simply gets back all the arrows she fired."""
    },
    {
        "id":
        "TC2",
        "name":
        "Called Shot",
        "attribute":
        "dexterity",
        "action":
        True,
        "skill_use":
        Yes,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["archer", "swordmaster"],
        "description":
        """A character can use the Called Shot talent to impress onlookers with a display of targeting accuracy. The character announces his attack aloud, naming his target and roughly where the shot will strike. The character makes a Called Shot Test instead of a standard Attack Test. A successful test means the shot hit in approximately the called spot. Opponents who see this display of skill are suitably impressed. A successful test affects a number of characters equal to the character's Called Shot talent, modifying the next test the onlookers make by -1 step. For example, if a character engaged in combat successfully calls a shot, the opponents preparing to attack his companions would make their next Attack Test at -1 step. The character using the talent chooses the characters to be affected. The affected characters must understand the language the character is speaking in order to be affected by a successful Called Shot. Called Shot can only impress opponents; the talent does not increase the damage from an attack."""
    },
    {
        "id":
        "TC3",
        "name":
        "Cat's Paw",
        "attribute":
        "dexterity",
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
        """The Cat's Paw talent permits a character to move quietly. Make a Cat's Paw Test, then use the result as the Difficulty Number for tests by anyone else attempting to detect the character. Because Cat's Paw makes a target even harder to detect than normal, a detecting character must roll a Good success or better to discern a character using the Cat's Paw."""
    },
    {
        "id":
        "TC4",
        "name":
        "Charge",
        "attribute":
        "strength",
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
        """The Charge talent increases the damage of a mounted attack (see Mounted Combat). The attacker must spend the preceding round riding toward the target to build momentum. The magic fueling the talent increases the damage for any type of physical attack, be it by spear, club, sword, fist, and so on. Use the Charge step in place of the Strength step to make the Damage Test. Add the Charge steps to the Strength dice of the mount or the rider, whichever is greater. The spell can also help a character stay on his mount (see Combat)."""
    },
    {
        "id":
        "TC5",
        "name":
        "Claw Frenzy",
        "attribute":
        "dexterity",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        0,
        "discipline_talent": ["beastmaster"],
        "description":
        """Using the Claw Frenzy talent, a character can make more effective, and possibly, multiple attacks using the Claw Shape talent . When using Claw Frenzy to attack with Claw Shape, the character uses the Claw Frenzy talent instead of Unarmed Combat.In one round, a character may attack using Claw Shape a number of times equal to his rank in Claw Frenzy. For example, Rank 3 Claw Frenzy would give the character 3 Claw Shape Attack Tests. The character must spend the Karma Point required to use Claw Frenzy on the first Attack Test. He may spend an additional Karma Point on each subsequent Claw Frenzy Test, and may also spend Karma on the Claw Shape Damage Tests. For each Claw Shape attack made during Claw Frenzy, use the Claw Shape damage step (see Claw Shape) to make the Damage Tests. """
    },
    {
        "id":
        "TC6",
        "name":
        "Claw Shape",
        "attribute":
        "strength",
        "base_modifier":
        3,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["beastmaster"],
        "description":
        """The Claw Shape talent changes a character's dominant hand into a fearsome clawed weapon. The character uses his Unarmed Combat talent or skill to make Attack Tests with Claw Shape. Make the Damage Test using the Claw Shape step, plus the required Karma dice. If using Claw Shape with Claw Frenzy, the character may use a Karma Point for each Damage Test. Claw Shape lasts until it does damage, then immediately fades away."""
    },
    {
        "id":
        "TC7",
        "name":
        "Climbing",
        "attribute":
        "dexterity",
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": [],
        "description":
        """The Climbing talent allows a character to climb up the sides of various surfaces and objects. A character makes a Climbing Test against the climb's difficulty, a number determined by the gamemaster (see Adventuring in Earthdawn ). If the result is equal to or higher than the Difficulty Number, the character climbs successfully. A character can climb at a rate of (3 + Climbing Rank) yards per round, i.e., a character with Rank 2 Climbing Talent could climb 5 yards a round."""
    },
    {
        "id":
        "TC8",
        "name":
        "Cobra Strike",
        "attribute":
        "dexterity",
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["warrior"],
        "description":
        """The Cobra Strike talent allows a character to make incredibly quick attacks in the first round of combat. Cobra Strike only works for the first round of combat against any one opponent. Make a Cobra Strike Test instead of a standard Initiative Test for that one round. The magic powering the Cobra Strike Talent overcomes Initiative modifiers based on armor or shields. Ignore any applicable Initiative step decreases when using Cobra Strike. Cobra Strike can be used in the same round as an Attack Test. A character may also add a number of steps equal to his or her rank in Cobra Strike talent to one Attack Test during the round in which it is used. Cobra Strike cannot be used with other talents that augment Initiative."""
    },
    {
        "id":
        "TC9",
        "name":
        "Cold Purify",
        "attribute":
        "willpower",
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["elementalist"],
        "description":
        """The Cold Purify talent stops the effects of poison. Using this talent requires access to ice, snow, or chilled water. The character packs the ice (or cold material) around a poisoned character's wound. After one minute of concentration, the character makes a Cold Purify Test against the poison's step number. A successful test stops the effect of the poison, and the victim recovers a number of Damage Points equal to the difference between the Cold Purify result and the poison step number. The Cold Purify Talent only heals damage inflicted by poison."""
    },
    {
        "id":
        "TC10",
        "name":
        "Conceal Weapon",
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
        "discipline_talent": ["thief"],
        "description":
        """A character can use the Conceal Weapon talent to use sleight of hand and illusion to hide weapons somewhere on his or her body. The character makes a Conceal Weapon Test and subtracts the size of the weapon (see the Goods and Services table) from the result. That number becomes the Difficulty Number for tests by any character attempting to detect the weapon. The concealment lasts for 24 hours, but ends immediately if someone discovers the weapon or if the character removes the weapon from its hiding place.
As long as the weapon remains concealed, use of this talent gives the character an Initiative bonus equal to his rank in Conceal Weapon when drawing and striking with a concealed weapon."""
    },
    {
        "id":
        "TC11",
        "name":
        "Creature Analysis",
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
        "discipline_talent": ["beastmaster"],
        "description":
        """The Creature Analysis talent allows a character to use scholarship and divination magic to gain information about a creature he is observing. If the character makes a successful test against the creature's Spell Defense Rating, he may ask the gamemaster one specific question about the creature. For the purposes of this talent, the player can ask a specific question that would reveal one of the creature's game statistics or abilities. The gamemaster should, however, cheerfully disallow questions comparing more than one statistic, such as 'Is this beast tougher than I am?' or 'Which is higher, its Physical Defense or Spell Defense?'"""
    },
    {
        "id":
        "TC12",
        "name":
        "Crushing Blow",
        "attribute":
        "strength",
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        0,
        "discipline_talent": ["sky_raider"],
        "description":
        """The Crushing Blow talent is a fearsome attack used to inflict maximum damage. When a character uses Crushing Blow against an opponent, he uses his Crushing Blow step instead of his Strength step for the Damage Test. The required Karma die is spent on this Damage Test. The character must use Battle Shout in the same round against the target of the Crushing Blow. If the Battle Shout Test succeeds, add +3 steps to the step of the Damage Test. If the Battle Shout Test fails, the opponent takes standard Crushing Blow damage."""
    },
]
