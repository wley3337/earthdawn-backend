talent_seeds_t = [
    {
        "id":
        "TT1",
        "name":
        "Taunt",
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
        "discipline_talent": [],
        "description":
        """The Taunt talent allows a character to enrage an opponent, thereby distracting him. The character makes a Taunt Test that round rather than an attack, using an opponent's Social Defense as the Difficulty Number. A successful Taunt Test means the opponent is so angered that he must reduce all his dice steps by a number equal to the character's Taunt Rank, for a number of rounds also equal to the rank. Only one Taunt can affect a character at any time."""
    },
    {
        "id":
        "TT2",
        "name":
        "Temper Other",
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
        "discipline_talent": ["weaponsmith"],
        "description":
        """The Temper Other talent allows a character to toughen another character, making him more resistant to physical attacks. The character draws forth icy ether from astral space, rolling the chilling substance over the recipient character. This ritual requires one half-hour of intense meditation by both the character and the target character. The character using the talent makes a Temper Other Test against the target's Toughness step. If the character makes a successful Talent Test, the recipient's Death Rating, Wound Threshold, and Unconsciousness Ratings all increase by the character's rank in Temper Other. Temper Other lasts for 24 hours from the end of the ritual.
If the Temper Other Test fails, the target automatically takes a number of Damage Points equal to his Wound Threshold, taking both the Damage Points and a Wound. Physical armor does not protect against this damage, and the character can suffer knockdown."""
    },
    {
        "id":
        "TT3",
        "name":
        "Temper Self",
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
        "discipline_talent": ["weaponsmith"],
        "description":
        """The Temper Self talent allows a character to toughen himself and become more resistant to physical attacks. The character draws icy ether from astral space and rolls the chilling substance over himself. This ritual requires one half-hour of intense meditation. The character makes a Temper Self Test using his own Toughness step as the Difficulty Number. A successful test increases the character's Death Rating, Wound Threshold, and Unconsciousness Ratings by the character's rank in Temper Self. Temper Self lasts for 24 hours from the end of the ritual.
If the Temper Self test fails, the character automatically takes a number of Damage Points equal to his Wound Threshold, taking both the Wound and the damage. Physical armor does not protect against this damage, and the character can be knocked down."""
    },
    {
        "id":
        "TT4",
        "name":
        "Temperature",
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
        "discipline_talent": ["elementalist"],
        "description":
        """The Temperature talent allows a character to control the temperature within a room or small shelter, up to 10 by 10 by 8 feet in size. For each rank of the Temperature talent, the character can raise or lower the temperature by 10 degrees Fahrenheit. The character makes a Temperature Test against the Spell Defense of the room (minimum of 2). The effects of Temperature last for a number of hours equal to the Temperature Test result. The character may cancel the effect any time he is in or adjacent to the room."""
    },
    {
        "id":
        "TT5",
        "name":
        "Thread Weaving",
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
        0,
        "discipline_talent": ["all"],
        "description":
        """Characters use the Thread Weaving talent to create and weave magical threads. A character can only have a number of threads active equal to his Thread Weaving Rank. For example, a character with Rank 3 Thread Weaving could have 3 threads active at once. This limit does not apply to threads woven into spell patterns. See the Workings of Magic section for more information about threads and spell patterns.
Each Discipline has a unique variation of the Thread Weaving talent, as listed below.

Discipline: Thread Weaving Talent
Archer Arrow:  Weaving
Beastmaster: Beast Weaving
Cavalryman: Rider Weaving
Elementalist: Elementalism
Illusionist: Illusion
Nethermancer: Nethermancy
Sky Raider: Sky Weaving
Swordmaster: Blade Weaving
Thief: Thief Weaving
Troubadour: Story Weaving
Warrior: War Weaving
Weaponsmith: Thread Smithing
Wizard: Wizardry

Record the appropriate Thread Weaving talent on the Character Record Sheet. For example, the Character Record Sheet for an Archer would list Arrow Weaving.
The Thread Weaving talent also gives characters a limited version of the Astral Sight talent. The astral sight provided by Thread Weaving allows characters only enough vision to see threads and patterns. See the Workings of Magic section for more information on threads, thread weaving, and True Patterns.
Using the Versatility talent, human characters may purchase ranks in Thread Weaving talents other than the one listed for their Discipline. These talent ranks cost the same as normal for Thread Weaving."""
    },
    {
        "id":
        "TT6",
        "name":
        "Throwing Weapons",
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
        "discipline_talent": ["thief"],
        "description":
        """A character uses the Throwing Weapons talent to attack with rocks, daggers, spears, and other thrown weapons. The character makes a Throwing Weapons Test against the Physical Defense of the target. A successful test result means the attack hits the target."""
    },
    {
        "id":
        "TT7",
        "name":
        "Tiger Spring",
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
        """The Tiger Spring talent allows a character to react more quickly than normal in combat situations. The character may add her Tiger Spring Rank to her Initiative step. For example, Rank 3 Tiger Spring would add 3 steps to a character's Initiative step. Tiger Spring can be used with other talents that increase Initiative, such as Air Dance."""
    },
    {
        "id":
        "TT8",
        "name":
        "Tracking",
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
        "discipline_talent": ["beastmaster"],
        "description":
        """The Tracking talent allows a character to track people and animals across great distances using her keen senses and divination magic. To use the Tracking talent, the character touches a visible track and makes a Tracking Test against the target's Spell Defense. If the trail is more than a day old, increase the target's Spell Defense by +3. If the trail is more than a week old, add 10 to the target's Spell Defense. A successful test imprints faint, luminous images of the tracks on the pupils of the character using the talent. The character sees these same luminescent prints on the ground, allowing him to follow the tracks of the target, even those obliterated by the weather. The effect lasts for a number of hours equal to the character's rank in Tracking."""
    },
    {
        "id":
        "TT9",
        "name":
        "Trap Initiative",
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
        1,
        "discipline_talent": ["thief"],
        "description":
        """Note: May cause 2 strain. See description below.
The Trap Initiative talent allows a character to react more quickly to traps. When a character with this talent accidentally triggers a trap, the character makes a Trap Initiative Test against the Initiative of the trap. If the character's Initiative is higher than the trap's, he can react before it goes off, perhaps avoiding the effect of the trap. The Trap Initiative talent can be used against both mechanical and magical traps.During combat, if the character triggers a trap after his normal Initiative, this talent allows the character to make an additional Initiative Test to see if he can avoid the trap. Using Trap Initiative in this way causes 1 additional point of Strain to the character.
Example: Marcon is a Thiefwith Rank 2 Trap Initiative. While investigating an old kaer, Marcon and his companions encounter a group of ghouls. Opting to flee, Marcon runs down a corridor, declaring Full Movement as his combat action, which will allow him to get as far away from the ghouls as possible. While running, Marcon triggers a pit trap located in the corridor. Though Marcon has already taken his action for the round, he can use Trap Initiative to try and avoid the pit trap. Marcon makes a Trap Initiative Test with a result of 12. The trap has an Initiative of 14. Poor Marcon falls into the trap, thinking he might have been better off with the ghouls."""
    },
    {
        "id":
        "TT10",
        "name":
        "Trick Riding",
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
        """The Trick Riding talent allows a character to perform acrobatics on his mount. The character may use this talent instead of the Avoid Blow talent to defend either himself or his mount from an attack, and may also use Trick Riding to jump fences, chasms, flames, or other obstacles. The character makes a Trick Riding Test against a Difficulty Number determined by the gamemaster, based on the maneuver attempted. Jumping a short fence would be a Difficulty of 4, while jumping over a 10-foot-wide chasm would have a Difficulty Number of 12. If any of these acrobatics require a Dexterity Test, substitute the Trick Riding result for the mount's Dexterity step."""
    },
    {
        "id":
        "TT11",
        "name":
        "True Shot",
        "attribute":
        "dexterity",
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
        """The True Shot talent allows a character to make a very accurate missile attack. The character makes an Attack Test using the True Shot step instead of the Missile Weapons step. The character must spend at least 1 Karma Point on the Attack Test, and may spend a total number of Karma Points equal to her rank in True Shot on the Attack Test. When using this talent, a character must continue to spend Karma Points, 1 at a time, until the Attack Test result is higher than the target's Physical Defense Rating, or until the character can spend no more points. Once the attack hits, the character cannot spend additional Karma Points to increase the success level of the test."""
    },
    {
        "id":
        "TT12",
        "name":
        "True Sight",
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
        "discipline_talent": ["illusionist"],
        "description":
        """The True Sight talent allows a character to penetrate illusions. The character makes a True Sight Test using the illusion's Sensing/Disbelief Difficulty (see the Spell Magic section). A successful test result allows the character to penetrate the illusion."""
    },
]
