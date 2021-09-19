talent_seeds_r = [
    {
        "id":
        "TR1",
        "name":
        "Read and Write Language",
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
        "discipline_talent": ["troubadour", "wizard"],
        "description":
        """The Read and Write Language talent allows a character to learn one new language for each rank of the talent. To learn a language, your character must first have access to one written page of text in that language. If the character has a rank of Read and Write Language available and the written page of text, he can then learn a new language. To learn a language, the character makes a Read and Write Language Test against the Difficulty Number of the language as shown below. (The Difficulty Numbers refer to the standard versions of these languages. Each racial language has many variations. If a character is attempting to learn a variation of a language, add +2 to the Difficulty Number.) A successful test result means the character can now use the talent to read and write the language. Once a rank is assigned to a language, it cannot be used to learn any other language. Record the languages your character learns on the Character Record Sheet.
Language/Difficulty
Dwarven 5
Elvish (Sperethiel) 6
Human 6
Obsidimen 7
Ork 6
Troll 6
T'skrang 7
Windling 7
When reading another language, the character makes a Read and Write Language Test to see how well he understands what he is reading. The result determines the level of understanding. To understand simple sentences or ideas, such as "The sheriff's house lies east of here," only requires a result of 2. Histories or legends containing some idioms or flowery phrases require a result of 6. Magical manuals or other books filled with jargon specific to a field of study require a result of 10. To understand philosophical treatises on the nature of magic or other writing filled with specialized academic language and abstract ideas requires a result of 13. When writing a language, use the same Difficulty Numbers as required for reading, depending on the complexity of the topic the character is writing about. Each Read and Write Language Test lasts for a number of hours equal to the character's rank in Read and Write Language. Reading a page takes 1 minute. Writing a page takes 10 minutes."""
    },
    {
        "id":
        "TR2",
        "name":
        "Read and Write Magic",
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
        "discipline_talent":
        ["elementalist", "illusionist", "nethermancer", "wizard"],
        "description":
        """The Read and Write Magic talent allows a magician to learn new spells and write them in his or her grimoire. Without the Read and Write Magic talent, a magician cannot learn new spells. A magician can attempt to learn only one spell per day. To learn a new spell, the magician makes a Read and Write Magic Test against the Difficulty Number of the spell. If the test is successful, the magician has learned the spell and can write it in his grimoire. See the Spell Magic section for information regarding spell difficulties and limits on learning new spells. This talent also allows magicians to read and write magical writing such as that on scrolls or magical glyphs. The character makes a Read and Write Magic Test using the Difficulty Number of the writing. The success level determines how well the magician understands the writing. An Average success allows the magician to understand the basic gist of the text, but not any subtle or complex ideas it contains. A Good or Excellent success means the magician understands the subtleties of the text, though he might misinterpret obscure clues or riddles. An Extraordinary success means the magician completely understands the magical writing and easily deciphers any hints, clues, or hidden meanings. A magician may attempt to read or write one sample (up to approximately one manuscript page) of magical writing a number of times a day equal to his rank in Read and Write Magic."""
    },
    {
        "id":
        "TR3",
        "name":
        "Reshape Object",
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
        2,
        "discipline_talent": ["elementalist"],
        "description":
        """The Reshape Object talent allows a character to change the shape, but not the mass, of an object. The character makes a Reshape Object Test against the Physical Armor Rating of the object to be reshaped (see Barriers and Structures in Adventuring In Earthdawn). If the object is magical, make the test against either the object's Barrier Rating or Spell Defense, whichever is higher. A successful result allows the character to reshape the object. The character can reshape a number of pounds of material equal to 20 x his or her Reshape Object Rank with a single use of the talent. Reshape Object is permanent. This talent does not work against living beings, including plants. """
    },
    {
        "id":
        "TR4",
        "name":
        "Resist Taunt",
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
        1,
        "discipline_talent": ["calvalryman", "troubadour"],
        "description":
        """The Resist Taunt talent allows a character to resist the effects of Interaction Tests. Any time another character's social action affects a character, the victim may make a Resist Taunt Test to ignore the effect. If the test result equals or exceeds the result of the opponent's Interaction Test, the character resists the effect. On a successful use of Resist Taunt, it is as if the target character steeled himself and reconsidered his action at the last minute. The Resist Taunt Talent works much like Avoid Blow, except that it operates against social attacks such as persuasion, taunts, or intimidation. Resist Taunt may be used only once per opponent.
Example: Segue, a t'skrang Troubadour, has a Social Defense of 7. A soldier taunts him, rolling a test result of 14. Segue decides to use his Resist Taunt talent. His player rolls a 9, and so his attempt to Resist Taunt fails. Segue's tail flails in frustration."""
    },
    {
        "id":
        "TR5",
        "name":
        "Reposte",
        "attribute":
        "dexterity",
        "base_modifier":
        3,
        "action":
        True,
        "skill_use":
        True,
        "requires_karma":
        True,
        "strain":
        2,
        "discipline_talent": ["swordmaster"],
        "description":
        """The Riposte talent allows a character to turn an attack back on his attacker. The character makes a Riposte Test against the result of the Attack Test made by a single opponent. If the Riposte result is higher than the Attack Test result, the attacked character avoids the blow, then immediately attacks using the Riposte Test result as an Attack Test. If the Riposte result is higher than the opponent's Physical Defense Rating, the Riposte hits the opponent. The riposting character then makes a normal Damage Test. Riposte Tests can result in Armor-Defeating Hits. A character may use the Riposte talent in the same round as an attack. A character may only use Riposte once per round, regardless of how many attacks he suffers in that round. A character can only use the Riposte talent against attacks made with melee weapons."""
    },
]
