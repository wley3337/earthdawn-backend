talent_seeds_l = [
    {
        "id":
        "TL1",
        "name":
        "Lasting Impression",
        "attribute":
        "charisma",
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
        """The Lasting Impression talent allows a character to impress a group of onlookers. A character can only use Lasting Impression when he first meets a group of characters or when he prepares to leave a group of characters and will not return for at least 24 hours. This talent imprints a dramatic image of the character in the minds of those affected. The character chooses the characters upon whom he wants to leave a Lasting Impression; he must choose these characters before making the Talent Test. The maximum number of characters he can impress is equal to his rank in Lasting Impression. The character must strike a dramatic pose, then make a Lasting Impression Test and compare the result to the Social Defense of each target he wants to impress. If his test result is equal to or higher than the Social Defense, the character adds a positive modifier equal to his rank in Lasting Impression to all tests made against the target's Social Defense within a certain time. The effects of Lasting Impression last for a year and a day. All the impressed characters and the character who used the talent should record the Lasting Impression effect on their Character Record Sheets for easy reference."""
    },
    {
        "id":
        "TL2",
        "name":
        "Life Check",
        "attribute":
        "toughness",
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
        "discipline_talent": ["warrior"],
        "description":
        """The Life Check talent gives the character a chance to save himself from death. A character immediately makes a Life Check Test as soon as his Current Damage is higher than his Death Rating. Each use of the Life Check talent uses up one of the character's Recovery Tests. If the character does not have a Recovery Test available, he cannot use Life Check. The character rolls his Life Check dice and reduces his Current Damage by the result. If the Current Damage is now less than the character's Death Rating, the character remains alive. If the Damage is now less than the character's Unconsciousness Rating, the character regains consciousness."""
    },
    {
        "id":
        "TL3",
        "name":
        "Lifesight",
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
        "discipline_talent": ["nethermancer"],
        "description":
        """The Lifesight talent gives a character the ability to see the strength and composition of a character's life force. The character learns qualitative information, not quantitative. A strong, healthy life force appears as a strong but delicate latticework of light and opalescent force. Weaker life forces are dimmer, and parts of the latticework may be warped or broken. The life force of a character near death shows almost no visible latticework, just a few disconnected bright spots, one or more of which is fading. Each use of Life Sight requires 1 minute. Lifesight has a range of 5 yards per rank of Lifesight.
The character makes a Lifesight Test and compares the result to the Spell Defense of each character within range. Anytime his dice result is higher than that number, the character can see a target's life force.
A character can use Lifesight to view a target's life force through solid, non-living objects. For example, a character could see the life forces of people hiding behind a brick wall, but not someone hiding in a hollow giant redwood tree. Once seen by Lifesight, the life forces remain visible as long as the targets stay in range."""
    },
    {
        "id":
        "TL4",
        "name":
        "Lion Heart",
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
        "discipline_talent": ["beastmaster"],
        "description":
        """The Lion Heart talent helps a character resist fear and intimidation. Substitute the Lion Heart step for the character's Willpower step when making tests to resist fear or intimidation effects."""
    },
    {
        "id":
        "TL5",
        "name":
        "Lip Reading",
        "attribute":
        "charisma",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        True,
        "strain":
        1,
        "discipline_talent": ["thief"],
        "description":
        """The Lip Reading talent gives a character a discreet method of eavesdropping on a conversation. The character must be able to see a speaker's lips and understand his language in order to use Lip Reading. The character makes a Lip Reading Test against the speaker's Social Defense. If the test is a success the character can understand the speaker's words. The effect lasts for a number of minutes equal to the character's rank in Lip Reading, and has a maximum range of 50 yards."""
    },
    {
        "id":
        "TL6",
        "name":
        "Lizard Leap",
        "attribute":
        "strength",
        "base_modifier":
        0,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        0,
        "discipline_talent": ["beastmaster"],
        "description":
        """The Lizard Leap talent enables a character to leap a great distance straight up. To determine how high, the character rolls his Lizard Leap dice; the result is the number of yards he may leap straight up. The character may also make a horizontal jump a number of yards up to twice the Lizard Leap dice result. Lizard Leap may be used in the same round as an Attack Test. A character may use the Lizard Leap Talent to engage an opponent and cause extra damage for one attack. The character rolls his Lizard Leap dice, then makes his Attack Test. Increase the Damage step of a successful Melee Weapons or Unarmed Combat attack by a number equal to the character's rank in Lizard Leap. In addition, increase his Physical Defense by +2 to reflect the increased difficulty of hitting a target while using Lizard Leap."""
    },
    {
        "id":
        "TL7",
        "name":
        "Lock Pick",
        "attribute":
        "dexterity",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["thief"],
        "description":
        """A character uses the Lock Pick talent to open locks. This magical talent conjures a pale blue telekinetic "lock pick." The pick may be used to open ordinary locks or magical locks. The character makes a Lock Pick Test against a Difficulty Number determined by the gamemaster, or against the lock's Spell Defense when picking magical locks. A successful test means the lock opens. The maximum number of times a character may attempt to open any one lock is equal to his rank in Lock Pick. If a character attempts and fails to open a lock the maximum times allowed, he may not try to pick the lock again until he gains another rank in the Lock Pick talent."""
    },
    {
        "id":
        "TL8",
        "name":
        "Lock Sense",
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
        "discipline_talent": ["thief"],
        "description":
        """The Lock Sense talent detects ordinary or magical traps placed on locks or that are triggered by someone opening the lock. This talent also allows a character to detect hidden locks like those found on secret doors. The character makes a Lock Sense Test against a Difficulty Number determined by the gamemaster for mundane locks or against the Spell Defense for magical doors or locks. The character must be within 3 feet of a lock to use Lock Sense. Each use of Lock Sense lasts only long enough to sense one door or object."""
    },
]
