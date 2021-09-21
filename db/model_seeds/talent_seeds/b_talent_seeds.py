talent_seeds_b = [
    {
        "id":
        "TB1",
        "name":
        "Bank Shot",
        "attribute":
        "dexterity",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["archer", "thief"],
        "description":
        """The Bank Shot talent allows a character to ricochet missile and thrown weapons off obstacles on the way to their target. A character need not have line of sight to the target in the round during which he uses Bank Shot, but must have had line of sight to the target during his last action. The character points out the objects off which he intends to ricochet his shots, then uses his Bank Shot step to make the Attack Test. If successful, his shot makes a number of banks equals to the character's rank in Bank Shot. A failed Attack Test using Bank Shot means the missile flies completely off target. A bank shot destroys arrows and bolts used to make the shot. Though the bank shot nicks and scratches daggers and other throwing weapons, these remain usable."""
    },
    {
        "id":
        "TB2",
        "name":
        "Battle Beloow",
        "attribute":
        "charisma",
        "action":
        False,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["sky_raider"],
        "description":
        """The Battle Bellow talent allows a character to intimidate his foes and inspire his companions. The character makes a Battle Bellow Test against the Social Defense of the target. If the character is attempting to use Battle Bellow against more than one target, add 1 to the highest Social Defense Rating in the group for each additional target character. The character using Battle Bellow must be involved in combat or threatening to engage in combat. Battle Bellow may be used in the same round as an Attack Test.
A successful test reduces all the target's steps for 1 round by a number equal to the character's rank in Battle Bellow. Rank 4 Battle Bellow, for example, reduces all the target's tests by -4 steps. A target can only be affected by one Battle Bellow at a time.A character can also use Battle Bellow to inspire his companions. If the character rolls a Good success or better in the Battle Bellow Test, it also adds a positive modifier to any Battle Shout Tests by all friendly Sky Raiders within a distance of the Battle Bellow Rank x 10 yards of the character. The bonus is equal to the character's Battle Bellow Rank; a Rank 3 Battle Bellow, for example, adds 3 steps to all Battle Shout Tests."""
    },
    {
        "id":
        "TB3",
        "name":
        "Battle Shout",
        "attribute":
        "charisma",
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
        """The Battle Shout talent allows a character to intimidate foes. The character makes a Battle Shout Test against the Social Defense of the target character. If the character is attempting to use Battle Shout against more than one target, add +1 to the highest Social Defense Rating in the group (the Difficulty Number) for each additional target character.
        A troll uses Battle Shout against a group of 6 soldiers, one of whom is a sergeant. The sergeant's Social Defense is highest, so it becomes the Social Defense for the group. Because the troll is also targeting 5 additional characters, he adds the +5 to the sergeant's Social Defense to get the Difficulty Number for the Battle Shout Test. The character must be involved in combat or threatening to engage in combat in order to use Battle Shout. Battle Shout may be used in the same round as an Attack Test.
        The character must roll a Good success or better for Battle Shout to succeed. A successful test reduces all the target's steps by a number equal to the character's Battle Shout Rank for a period of 1 round. A Rank 4 Battle Shout, for example, would reduce the steps for all the opponents' tests by 4 steps. A character may be affected by only one Battle Shout at a time."""
    },
    {
        "id":
        "TB4",
        "name":
        "Blood Share",
        "attribute":
        "toughness",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["cavalryman"],
        "description":
        """The Blood Share talent allows a character to transfer damage between his mount and himself. First, the character makes a small cut somewhere on himself and on his mount, then touches the two cuts together. Then he makes a Blood Share Test. The result is the number of Damage Points that can be transferred between himself and his mount. Depending on the situation, the character might want to transfer the full number of Damage Points or transfer only a portion. Again, depending on the situation, he will transfer the damage either from his mount to himself or vice versa. For example, a character might decide to transfer only 7 Damage Points on a test result of 10, or he might choose to use the whole number. Transferring only 7 points from his mount to himself, for example, would reduce the mount's damage by only 7 points, not the full 10. Transferred damage never causes a Wound, but if the transferred damage sends either the character's or the mount's (whichever is taking the transfer of damage) Current Damage higher than his Death Rating, the affected character or mount still dies.
Blood Share talent normally does not require the character to spend Karma, but if a Cavalryman wants to use this talent on another willing character, he can do so by spending 1 Karma Point. Roll the Karma dice at the same time as the Blood Share Test is made, as normal. Using Blood Share in this way requires that deep trust exist between the character and his volunteering comrade. Members of the Cavalryman Discipline almost universally honor this trust, and have coined the term "blood betrayer" to refer to anyone who uses Blood Share to transfer so much damage to another character that the second character dies. Other Cavalrymen shun blood betrayers."""
    },
    {
        "id":
        "TB5",
        "name":
        "Book Memory",
        "attribute":
        "willpower",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        True,
        "strain":
        0,
        "discipline_talent": ["wizard"],
        "description":
        """The Book Memory talent allows a character to memorize knowledge from a book. The character need make only one Book Memory Test per book, using the book's Spell Defense as the Difficulty Number. The Spell Defense of most grimoires is at least equal to the Casting Difficulty of the highest-ranking spell it contains. For the purposes of using Book Memory, one grimoire equals one book. Normal books have a Spell Defense of 5 against memorization.
The character can memorize a number of pages per round equal to his Book Memory Rank. The character must memorize the entire book at one sitting. If he or she performs any other action while memorizing, the character's concentration breaks and the memorization is lost. The character need not be able to read the language to memorize a book.
The knowledge of a memorized book stays in the character's memory for a year and a day before fading. A character can use the Book Recall talent to retrieve this knowledge later. The maximum number of books the character can hold in memory at any one time equals the character's Book Memory Rank. A character may voluntarily discard memorized knowledge in order to memorize new knowledge."""
    },
    {
        "id":
        "TB6",
        "name":
        "Book Recall",
        "attribute":
        "perception",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        1,
        "discipline_talent": ["wizard"],
        "description":
        """The Book Recall talent retrieves information a character once memorized via the Book Memory talent but which subsequently faded. The Difficulty Number for remembering the information after the passage of a year and a day is based on the number of books the character currently has memorized, as follows:
Books Memorized / Difficulty Number for Remembering
1 / 7
2 / 8
3 / 9
4 / 10
5 / 11

For every book more than 5 add 1

Using the Book Recall talent takes 1 round. An Average success on a Book Recall Test retrieves one page of information. For each success level beyond Average, the character remembers the information on an additional page.

Example: Jerreck, an elven Wizard with Rank 3 Book Recall, is attempting to recall some information from a grimoire that he had previously memorized. Jerreck currently has a total of 5 books memorized, which the above table indicates as a Difficulty Number 11. Jerreck's player rolls an 18 on his Book Recall Test. Because this is a Good success, Jerreck can recall 2 pages from the book.

Once he retrieves the information, the character can write it down using either the Read and Write Languages talent or skill, or the Read and Write Magic talent, as appropriate. The information retrieved fades after 24 hours or whenever the character uses Book Recall again, whichever comes first. """
    },
    {
        "id":
        "TB7",
        "name":
        "Borrow Sense",
        "attribute":
        "willpower",
        "action":
        True,
        "skill_use":
        False,
        "requires_karma":
        False,
        "strain":
        0,
        "discipline_talent": ["beastmaster"],
        "description":
        """Using the Borrow Sense talent, a character temporarily takes one of an animal's five senses of touch, taste, hearing, smell, or sight for use as his own. The animal loses that sense for the duration of that borrowing. For this reason, only animals loyal to the character or those under the effect of a spell or the Dominate Beast talent will submit to Borrow Sense. The Beastmaster makes a Borrow Sense Test against the animal's Spell Defense. If the character tries to take a sense from an unwilling animal, increase the creature's Spell Defense by +5. Successful use of Borrow Sense earns the character all the benefits of the borrowed sense. The effect lasts a number of minutes equal to the character's Borrow Sense Rank."""
    },
]
