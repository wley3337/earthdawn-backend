talent_seeds_i = [
    {
        "id":
        "TI1",
        "name":
        "Improve Blade",
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
        "discipline_talent": ["weaponsmith"],
        "description":
        """The Improve Blade talent allows a character to add a temporary bonus to the Damage step of a weapon. Improve Blade is a quick magic ritual based on the Forge Blade talent, so a character must have Forge Blade in order to use Improve Blade. To perform Improve Blade, the character needs a fire the size of a large campfire. Within the time limit of half an hour, he quickly runs through a mock forging of the weapon to be improved. The character makes an Improve Blade Test against the Damage step of the weapon (as in Forge Blade). If the test fails, the weapon shatters. If the test is successful, the Damage step of the weapon increases by +1 step. A character may improve a single blade a number of times equal to his rank in Improve Blade. The Improve Blade talent can also be used to improve non-blade weapons. Each increase provided by Improve Blade lasts for 24 hours from the end of the ritual."""
    },
    {
        "id":
        "TI2",
        "name":
        "Incite Mob",
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
        "discipline_talent": ["troubadour"],
        "description":
        """The Incite Mob talent allows a character to motivate a group to act against a specific target. The character must spend at least 1 minute shouting and encouraging a large group of sentient beings to act. The character must state a target, a grievance, and propose an action for the mob to take. The action may be peaceful or violent, constructive or destructive. The character makes an Incite Mob Test against the highest Social Defense among the members of the mob. The size of the mob determines the success level needed to motivate the mob:
Mob Size Success Level Needed
Rank x 10 Average
Rank x 25 Good
Rank x 50 Excellent
Rank x 100 Extraordinary
The mob follows the inciter's course of action for a number of hours equal to the character's rank in Incite Mob. Once motivated, the mob becomes largely uncontrollable. A character can only control the mob by making a second, equally successful Incite Mob Test."""
    },
    {
        "id":
        "TI3",
        "name":
        "Incite Stampede",
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
        "discipline_talent": ["beastmaster"],
        "description":
        """With the Incite Stampede talent a character can make a group of animals stampede in a specific direction. The character must first spend at least 1 minute running and screaming around the herd of animals he is trying to stampede. The character then makes an Incite Stampede Test against the highest Social Defense among the animals of the group. The number of animals in the herd determines the success level needed to start a stampede:
Herd Size Success Level Needed
Rank x 10 Average
Rank x 25 Good
Rank x 50 Excellent
Rank x 100 Extraordinary
If the test is successful, the animals stampede uncontrollably in the direction chosen by the character. The Incite Stampede talent can also stop a stampede, though the practical problem of screaming through a stampeding herd limits this use. The animals stampede for a number of hours equal to the character's rank in Incite Stampede, or until they are exhausted, or until they encounter a great enough danger or obstacle to break the stampede."""
    },
    {
        "id":
        "TI4",
        "name":
        "Item History",
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
        """The Item History talent allows a character to learn the history of an enchanted or mundane item. The character must carry the item on his or her person for at least one week, studying it carefully for one hour each night. As soon as he completes seven nights of study, the character makes an Item History Test using the Spell Defense of the item as the Difficulty Number. The success level determines the amount of knowledge gained. An Average success reveals one Key Knowledge from the item's history. A Good success provides two Key Knowledges from its history, an Excellent success reveals three Key Knowledges, and an Extraordinary success reveals four Key Knowledges from the history of the item. The Item History talent can be used multiple times on the same item, each time after a week of study. When a character studies an item multiple times, the level of success of each succeeding test indicates the number of additional Key Knowledges from the item's history the character discovers. The character's rank in Item History is the maximum number of Key Knowledges that a character can learn through his talent. Once he increases the rank of Item History, he can then learn more Key Knowledges. The rank of Item History is also the maximum thread rank of any Key Knowledge that can be learned from an item.
Example: Jerreck, an elven Wizard, is studying the Ring of Gorlianna. He has already learned three Key Knowledges from the ring's history. On his latest attempt to use his Item History talent, Jerreck gets an Excellent result, giving him knowledge of three more Key Knowledges from the ring's past. This means Jerreck would know six Key Knowledges from the history of the Ring of Gorlianna. But because Jerreck has only five ranks in Item History, he can only learn up to five of the Key Knowledges.
As a character learns Key Knowledges from the history of the item, he or she begins to learn the Pattern Knowledge of the item. The character can use the Pattern Knowledge to create a thread to the item. The character may reveal the Pattern Knowledge to other characters, who then may also weave threads to the item. The maximum rank of a thread woven to a item equals the number of known events from the item's history. See the Workings of Magic section for more information regarding threads and Pattern Knowledge. """
    },
]
