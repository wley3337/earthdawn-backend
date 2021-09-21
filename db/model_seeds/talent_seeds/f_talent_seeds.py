talent_seeds_f = [
    {
        "id":
        "TF1",
        "name":
        "False Sight",
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
        "discipline_talent": ["illusionist"],
        "description":
        """The False Sight talent allows a character to intensify his illusions, making them more difficult for observing characters to penetrate. A character can use False Sight only on illusions he creates himself, not on those cast by other characters. The character using this talent must be able to see his target for False Sight to work. The character makes a Talent Test against the target's Spell Defense. If using False Sight against multiple targets, make a test against the highest Spell Defense in the group +1 for each additional target character. A successful test result increases the Difficulty Number for characters attempting to penetrate, Sense, or Dispel the illusion by a number of points equal to the character's rank in False Sight. This increase only applies to the actions of the target character, and it lasts for a number of minutes equal to the character's rank in False Sight."""
    },
    {
        "id":
        "TF2",
        "name":
        "Fast Hand",
        "attribute":
        "perception",
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
        """The Fast Hand talent lets a character move items from one place to another or to switch items between one character and another without being observed. All target items and characters must be within 2 yards of the character using the talent. The target items must measure 6 inches or less along their longest dimension. For his Talent Test, the character adds the number of items switched to the highest Spell Defense among his targets to find the Difficulty Number.
Example: Callera wants to switch the purses of 3 merchants, so that each merchant ends up with another merchant's purse. The merchants have Spell Defenses of 4, 6, and 5, respectively. The highest is 6, + 3 for the number of items being switched, resulting in a Difficulty Number of 9."""
    },
    {
        "id":
        "TF3",
        "name":
        "Fearsome Charge",
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
        2,
        "discipline_talent": ["calvalryman"],
        "description":
        """The Fearsome Charge talent allows a character to intimidate an opponent when making a charging attack. Fearsome Charge can also make opponents flee in fear. Only a mounted character may use Fearsome Charge.
A character using the talent transforms when he is charging. His eyes grow larger or glow, his teeth become pointed or the canines become longer, and his hair stands away from his head in a wild tangle. The character makes a Fearsome Charge Test against the Social Defense of his opponent. On an Average success, the opponent is frozen with fear and cannot move. On a Good success or better, the opponent flees at his fastest movement rate. The Fearsome Charge talent works against all opponents who see the charge. Compare the result of the Fearsome Charge Test to the Social Defense of any other characters who witness the charge (as above) to determine their actions.
An opponent affected by Fearsome Charge may overcome its effects on any subsequent round. The opponent must make a Willpower (or other fear-resisting talent) Test against the character's Fearsome Charge step number. A successful test means the opponent overcomes his fear in that round."""
    },
    {
        "id":
        "TF4",
        "name":
        "Fence",
        "attribute":
        "charisma",
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
        "discipline_talent": ["thief"],
        "description":
        """The Fence talent helps a character get a better price for stolen or illegal goods. Shady merchants usually buy stolen or illegal goods for 10 percent of their cost (see Goods and Services). If the character can make a successful Talent Test against the merchant's Social Defense, it raises the price the merchant will pay by 5 percentage points of the cost. The character may continue to make additional Fence Tests until one fails. If that happens, the merchant drops the last negotiated price by 5 percent of the cost, and negotiations are over. The merchant never offers less than 10 percent of the cost, and so the character has nothing to lose by making the first Fence Test. The maximum number of Fence Tests a character can make for any transaction is equal to his talent rank. The Fence talent can only be used for one transaction per day against any one character."""
    },
    {
        "id":
        "TF5",
        "name":
        "Fireblood",
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
        "discipline_talent": ["sky_raider"],
        "description":
        """The Fireblood talent allows the character to make one of his available Recovery Tests in the middle of a Combat Round, substituting the Fireblood step for his Toughness step in the test. The character cannot make an attack in the same round he uses the Fireblood talent, but he may also still be engaged on the field of battle. Fireblood makes the blood oozing from a character's scratches, cuts, and wounds bubble and hiss; during the round in which Fireblood is used, the blood steams, cleaning and partially healing the character's damage."""
    },
    {
        "id":
        "TF6",
        "name":
        "Fire Heal",
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
        "discipline_talent": ["elementalist"],
        "description":
        """The Fire Heal talent poses certain risks for low-Circle magicians, who generally begin with relatively low Wound Thresholds and Death Ratings. Successful use of the Fire Heal talent grants a character extra Recovery Tests. A failed Fire Heal Test burns the character. To use the Fire Heal talent, the character must build an open fire large enough to completely engulf him or her.
The character declares how many extra Recovery Tests he is attempting to gain with this talent. Fire Heal requires 30 minutes for each additional Recovery Test the character desires. He or she must attempt to gain at least 2 Recovery Tests. The character makes a Fire Heal Test using a Difficulty Number determined by the gamemaster. Then the gamemaster rolls 1D6 for each Recovery Test the character attempts to gain. If the character's Fire Heal Test is equal to or higher than the gamemaster's dice roll for the fire, the character earns the Recovery Tests and makes them normally. The Recovery Tests remain available for 24 hours after the successful Fire Heal Test. If the gamemaster's dice result is greater, the character automatically takes a Wound, plus a number of Damage Points equal to the difference between the Fire Attack Test and the Fire Heal Test. This damage can result in a second Wound.
The Fire Heal talent requires that the character be in full contact with the elemental power of fire. If a spell or item protects the character from fire, the Fire Heal Talent has no effect."""
    },
    {
        "id":
        "TF7",
        "name":
        "First Impression",
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
        0,
        "discipline_talent": [],
        "description":
        """The First Impression talent helps a character to favorably impress characters he or she has just met. The character makes a First Impression Test against the target's Social Defense. A successful First Impression Test gains the character a bonus equal to his rank in First Impression for all Charisma Tests. For example, a character with Rank 3 First Impression adds a +3 step bonus to all Charisma Tests made against a favorably impressed character. The effects of First Impression last a number of days equal to the amount by which the First Impression Test exceeded the target's Social Defense. The First Impression talent may only be used once against any one character."""
    },
    {
        "id":
        "TF8",
        "name":
        "Flame Arrow",
        "attribute":
        "willpower",
        "base_modifier":
        3,
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        2,
        "discipline_talent": ["archer"],
        "description":
        """The Flame Arrow talent allows a character to create a flaming arrow from a normal one, transforming his arrow into a missile of fire. This process destroys the arrow. Use the Flame Arrow step number when making the Damage Test for this talent. Add the Karma dice to the Damage Test."""
    },
    {
        "id":
        "TF9",
        "name":
        "Forge Blade",
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
        "discipline_talent": ["weaponsmith"],
        "description":
        """With the Forge Blade talent, a character can improve the Damage step of any melee weapon. To use this talent, the character must spend at least 1 week working on the weapon at a blacksmith's forge. At the end of that time, he makes a Forge Blade Test against the weapon's Damage step (see Goods and Services). A broadsword with Damage Step 5, for example, would have a Difficulty Number of 5. If the test is successful, increase the Damage step of the weapon by +1. In the case of the above broadsword, the Damage would increase to Step 6. A character may use Forge Blade on a single weapon a number of times equal to his rank in Forge Blade. This limit includes failed uses of the talent on that weapon.
Characters with this talent often charge others for the time they spend using it. The base rate to forge a special weapon is 50 x a number of silver pieces equal to the character's talent rank per week. This charge is in addition to the actual cost of the weapon. For example, a character with Rank 3 Forge Blade would charge 150 silver pieces a week to forge a weapon. Buying a broadsword that such a character improved by 2 Damage steps would cost at least 325 silver pieces.
Despite its name, the Forge Blade talent may be used to improve any melee weapon, not just bladed weapons. The name came because people with this talent originally made their reputations by forging swords and daggers."""
    },
    {
        "id":
        "TF10",
        "name":
        "Frighten",
        "attribute":
        "willpower",
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
        """The Frighten talent allows a character to scare another character. Stepping in front of his target, the character stares silently at the target character for 1 round. For the talent to have effect, the character must see the eyes of his target or else the target must be able to see the character's eyes. In the next round, the character using Frighten makes a Talent Test against the Spell Defense of the target. If the test is successful, the target character stays away from the frightening character for a number of rounds equal to the character's talent rank. If Frightened characters are not able to completely escape from the immediate area, they will at least move as far away as possible."""
    },
    {
        "id":
        "TF11",
        "name":
        "Frighten Animal Servants",
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
        "discipline_talent": ["beastmaster", "calvalryman"],
        "description":
        """The Frighten Animal Servants talent allows a character to terrorize servant animals. The talent focuses magic through the animals' master, making him the source of the animals' fear. The character makes a Talent Test against the highest Social Defense among the target animals. A successful test means all animal servants of a particular master flee from him or her in terror. Hounds will desert a hunter, a mount will throw its rider, guard tigers will flee from their ward. The effect lasts for a number of rounds equal to the character's rank in Frighten Animal Servants."""
    },
]
