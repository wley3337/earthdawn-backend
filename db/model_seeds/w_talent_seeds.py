talent_seeds_w = [
    {
        "id":
        "TW1",
        "name":
        "Warp Missile",
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
        "discipline_talent": ["weaponsmith"],
        "description":
        """The Warp Missile talent allows a character to reduce the effectiveness of an opponent's missile weapon. The character makes a Warp Missile Test against the Spell Defense of the missile weapon or the firer, whichever is higher. If the test is successful, reduce the Damage step of every missile fired from that weapon by the character's rank in Warp Missile. For example, Rank 2 Warp Missile reduces the missile Damage Tests for each attack by 2 steps. The effects of Warp Missile last a number of rounds equal to the character's Warp Missile Rank."""
    },
    {
        "id":
        "TW2",
        "name":
        "Weapon History",
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
        "discipline_talent": ["weaponsmith"],
        "description":
        """The Weapon History talent allows a character to learn the history of a weapon, either enchanted or mundane. The character must carry the weapon on his person for at least a week, studying it carefully for one hour each night. At the end of seven nights of study, the character makes a Weapon History Test against the Spell Defense of the weapon. The success level determines the amount of knowledge gained.An Average success reveals one of the weapon's Key Knowledges from its history. A Good success provides two Key Knowledges from its history, an Excellent succcess reveals three Key Knowledges, and an Extraordinary success reveals four Key Knowledges from the history of the weapon. The Weapon History talent can be used multiple times on the same weapon, each time after a week of study. On each subsequent effort to learn additional information about a weapon, the test result represents the number of additional Key Knowledges from the weapon's history the character discovers.The character's rank in Weapon History is the maximum number of Key Knowledges that a character can learn through this talent. Once he increases his rank in Weapon History, he can then learn more Key Knowledges. The rank of Weapon History is also the maximum thread rank of any Key Knowledge that can be learned from a weapon.
Example: Thom Hammerblade, a dwarven Weaponsmith, has devoted some weeks of study to a weapon known as Grag's Battle-axe. His previous studies have revealed to Thom three Key Knowledges from the weapon's history. On his latest attempt, Thom gets an Excellent success, earning him knowledge of 3 more Key Knowledges from the axe's past. This means Thom now knows 6 Key Knowledges from the history of Grag's Battle-axe. But because Thom has only Rank 5 in Weapon History, he can only learn up to 5 of the Key Knowledges.
As a character learns pieces of a weapon's history, he also learns the Pattern Knowledge of the weapon. The character may use this knowledge to weave a thread to the weapon. The character may tell other characters the Pattern Knowledge, and they also may use it to weave a thread to the weapon. The maximum rank thread a character can weave to a weapon equals the number of Key Knowledges he has learned. See The Workings of Magic section for more information regarding threads and Pattern Knowledge."""
    },
    {
        "id":
        "TW3",
        "name":
        "Wheeling Attack",
        "attribute":
        "dexterity",
        "base_modifier":
        0,
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        True,
        "strain":
        0,
        "discipline_talent": [],
        "description":
        """The Wheeling Attack talent allows a character to make a mounted attack and move away a distance equal to a Full Movement. When making an Attack Test while using this talent, a character substitutes the Wheeling Attack step for the Melee Weapons or Missile Weapons step. Wheeling Attack may be used with the Charge talent."""
    },
    {
        "id":
        "TW4",
        "name":
        "Wheeling Defense",
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
        "discipline_talent": ["cavalryman"],
        "description":
        """The Wheeling Defense talent increases the Physical Defense of a rider and his mount. The character urges his mount into a whirling circle, confusing his attackers with the moving, shifting targets. Make a Wheeling Defense Test, and increase the Physical Defense of the mount and character by the character's rank in Wheeling Defense for a number of rounds equal to the test result."""
    },
    {
        "id":
        "TW5",
        "name":
        "Willforce",
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
        """The Willforce talent provides the punch for spells. Because Willforce has a Default Attribute, a character does not need Willforce to cast a spell. However, spells cast by characters with this talent are usually more effective. Each rank of Willforce talent increases the effect of spells cast by the character. The character may substitute the Willforce step for the Willpower step to resist any effect targeted against his or her Spell Defense."""
    },
    {
        "id":
        "TW6",
        "name":
        "Wind Catcher",
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
        0,
        "discipline_talent": [],
        "description":
        """The Wind Catcher talent gives a character a chance to control his fall from a height. The character makes a Wind Catcher Test, using the test result to determine what effect the talent had on his or her descent. A result of 6 - 12 allows a character to land safely and take no falling damage. A result of 13 or more allows the character to direct his descent, though his landing point cannot be farther from his natural landing site than the distance he fell. For example, a character who falls 50 yards could use Wind Catcher talent to land up to 50 yards away from where he would have landed unassisted. A single use of the Wind Catcher talent can protect a character from a fall of 100 x the character's rank in Wind Catcher in yards. Falling 100 yards takes one Combat Round (10 seconds). Elite Sky Raiders use the Wind Catcher talent to make precise assaults on enemy positions."""
    },
    {
        "id":
        "TW7",
        "name":
        "Winning Smile",
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
        0,
        "discipline_talent": [],
        "description":
        """The Winning Smile talent causes a character to appear more attractive to members of the opposite sex. The character makes a Winning Smile Test against the Social Defense of the target. A successful result means the target finds the character's appearance very pleasing, and for the next 24 hours, the character using the talent receives a step bonus equal to his rank in Winning Smile for tests against the target's Social Defense.
A character may attempt to use Winning Smile against any single target a maximum of three times in one 24-hour period. After the third attempt, the character must wait 24 hours before trying to use the talent again on the same target.
Though effective most often against members of the same race, characters can use the Winning Smile talent successfully on members of other races. The gamemaster should judge such attempts to be either Hard or Very Hard on the Success Level Table (see Gamemastering Earthdawn), using the target's Social Defense as the Average Difficulty. For example, a human trying to impress a dwarf of Social Defense 7 might be thought of as attempting a Hard task, increasing the Difficulty Number to 12. That same human attempting to impress a t'skrang would have a Very Hard task, raising a Social Defense of 7 to a Difficulty Number of 15. See Gamemastering Earthdawn for more information on Interaction Tests."""
    },
    {
        "id":
        "TW8",
        "name":
        "Wood Skin",
        "attribute":
        "toughness",
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
        "discipline_talent": ["warrior"],
        "description":
        """The Wood Skin talent increases a character's resistance to physical damage by causing the character's skin, and portions of the muscles and ligaments, to become tougher. When using this talent, the character's skin takes on the appearance of wood or bark.
The character must use one of his available Recovery Tests for Wood Skin each day the talent is used. The character can only use the Wood Skin talent once per day, but the effect lasts for a full 24 hours, or until the character ends it. The character makes a Wood Skin Test, adding the test result to both her Death Rating and Unconsciousness Rating. The character can now take more damage before dying or falling unconscious."""
    },
    {
        "id":
        "TW9",
        "name":
        "Wound Balance",
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
        "discipline_talent": ["warrior"],
        "description":
        """The Wood Skin talent increases a character's resistance to physical damage by causing the character's skin, and portions of the muscles and ligaments, to become tougher. When using this talent, the character's skin takes on the appearance of wood or bark.
The character must use one of his available Recovery Tests for Wood Skin each day the talent is used. The character can only use the Wood Skin talent once per day, but the effect lasts for a full 24 hours, or until the character ends it. The character makes a Wood Skin Test, adding the test result to both her Death Rating and Unconsciousness Rating. The character can now take more damage before dying or falling unconscious."""
    },
    {
        "id":
        "TW10",
        "name":
        "Wound Balance",
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
        "discipline_talent": [],
        "description":
        """The Wound Balance talent improves a character's ability to resist knockdown. The character uses the Wound Balance step in place of the Strength step when making a Knockdown Test after taking a Wound."""
    },
]
