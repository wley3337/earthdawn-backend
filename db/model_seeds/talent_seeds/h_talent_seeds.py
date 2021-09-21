talent_seeds_h = [
    {
        "id":
        "TH1",
        "name":
        "Haggle",
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
        "discipline_talent": ["weaponsmith"],
        "description":
        """The Haggle talent allows characters to drive a bargain when buying or selling. A character makes a Haggle Test against the customer's or merchant's Social Defense Rating. If he is successful, the price rises or falls by 5 percent of the cost in favor of the character. Merchants or customers with the Haggle Talent (or skill) can also make a Haggle Test; a successful result could adjust the price in their favor.
The character may continue to make additional Haggle Tests for the same deal as long as he continues to roll successes in each subsequent test. As soon as he fails a Haggle Test, he can no longer bargain for this transaction. The maximum number of Haggle Tests a character can make for any transaction is equal to his Haggle Rank."""
    },
    {
        "id":
        "TH2",
        "name":
        "Heal Animal Servant",
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
        "discipline_talent": ["beastmaster", "cavalryman"],
        "description":
        """A character with the Heal Animal Servant talent may heal any of his or her animal servants. The character spends 1 of his own Recovery Tests to use the talent, reducing the animal's Current Damage by the result of the dice roll. Only standard Recovery Tests can be used to Heal Animal Servant. The character cannot use other talents, such as Fireblood, with this talent."""
    },
    {
        "id":
        "TH3",
        "name":
        "Heartening Laugh",
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
        """The Heartening Laugh talent allows a character to support friendly characters against fear. The character spends a round directing a booming, mocking laugh at one opponent. The character makes a Heartening Laugh Test against the highest Social Defense among all of the opponents present. If the test is successful, all friendly characters who hear the character's laugh receive a step bonus equal to the character's Heartening Laugh Rank to all Willpower Tests to resist fear and fear-type effects generated by the opponent. The step bonus effect of Heartening Laugh lasts for a number of rounds equal to the character's rank in Heartening Laugh."""
    },
    {
        "id":
        "TH4",
        "name":
        "Hold Thread",
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
        "discipline_talent": ["wizard"],
        "description":
        """The Hold Thread talent allows a character to weave a thread to a spell (see Spell Magic) and to hold the spell ready until the magician is prepared to cast it. If the Thread Weaving Test is successful, the character makes a Hold Thread Test to keep the spell within its matrix. The Difficulty Number for the test is the Weaving Difficulty (Spell Magic) of the thread(s) being held. A successful result holds the spell for a number of rounds equal to the character's rank in Hold Thread. The character may cast the spell during any one of these rounds. In the final round, the character may make another Hold Thread Test. A successful result will let the character continue to hold the spell for the same number of rounds. A failed Hold Thread Test means the character immediately casts the spell. A magician cannot weave or cast another spell while using Hold Thread to hold a spell."""
    },
    {
        "id":
        "TH5",
        "name":
        "Hypnotize",
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
        "discipline_talent": ["illusionist"],
        "description":
        """The Hypnotize talent allows a character to mesmerize another character, making the target very susceptible to persuasion through Interaction Tests. The Hypnotize talent is a magical effect rather than an actual hypnosis process. A character can hypnotize any single target within 10 yards. The character must speak to use this talent. The target cannot be involved in physical conflict and must be able to understand the hypnotist. The character using the talent makes a Hypnotize Test against the Spell Defense of the target. A successful test improves the attitude of the target toward the character by one degree, to a maximum of friendly (see Gamemastering Earthdawn). While under the influence of the Hypnotize talent, the target remains placid unless attacked. The character has a maximum number of minutes equal to his Hypnotize Rank to make post-hypnotic suggestions. During this time, the character can make Interaction Tests against the target, using successful tests and success levels to persuade the target to perform desired actions. The target character will perform any actions to which he or she agreed while under the effects of the Hypnotize talent, as long as the actions can be performed within a number of hours of the Hypnotize session equal to the character's rank in Hypnotize.
Example: While in a tavern, Poorht the Thief hypnotizes an off-duty private guard. Poorht improves the guard's attitude and uses a little persuasion. While hypnotized, the guard agrees to let Poorht into the house he guards as long as Poorht brings along some Rivercask ale to share. Poorht agrees. Poorht has Rank 3 Hypnotize, and so the effect lasts for 3 hours. At the end of that time, the guard comes to his senses. While he may not blame Poorht for having tricked him, the guard is no longer bound by his word."""
    },
]