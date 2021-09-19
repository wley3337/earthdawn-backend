talent_seeds_e = [
    {
        "id":
        "TE1",
        "name":
        "Eagle Eye",
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
        "discipline_talent": ["archer"],
        "description":
        """A character uses the Eagle Eye talent to aim at distant targets. If the character makes a successful test against the Spell Defense of the target, Eagle Eye will enable him to fire at the target as if it were at close range, ignoring any range modifier penalties that would normally apply. Each use of the Eagle Eye talent lasts a number of rounds equal to the character's talent rank. The talent takes effect in the first round after the successful Eagle Eye Test. The Eagle Eye talent only gives a character a better chance of hitting a target; it does not actually increase the range of missile weapons."""
    },
    {
        "id":
        "TE2",
        "name":
        "Earth Skin",
        "attribute":
        "",
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
        "discipline_talent": [],
        "description":
        """The Earth Skin talent makes a character much more resistant to damage. Earth Skin requires one of the character's Recovery Tests each day it is used. The character can only use this talent once per day, and must have ranks in the Wood Skin talent in order to use Earth Skin. The character's rank in Earth Skin may not exceed his or her rank in Wood Skin. The character must use the Wood Skin talent on the same day he uses Earth Skin. Earth Skin lasts for a full 24 hours, until Wood Skin wears off or until the character ends the effect.
Earth Skin adds to the effectiveness of a character's Wood Skin talent, making the character's skin even tougher. Earth Skin allows the character to take even more damage before falling unconscious or dying. Its primary magic increases the character's Spell Defense. As with Wood Skin, the character's skin still appears bark-like or wood-like, but with veins the color of dark earth.
The character's Spell Defense and Death Ratings increase by a number equal to his rank in Earth Skin."""
    },
    {
        "id":
        "TE3",
        "name":
        "Elemental Hold",
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
        """The Elemental Hold talent allows a character to prevent an elemental from moving or taking any action other than communicating. The character must possess the Elemental Tongues talent and be able to speak the elemental's language to use this talent. The elemental must be within 40 yards of the character. The character boldly faces the elemental and orders it to halt, then makes a Talent Test against the Spell Defense of the elemental. A successful test holds the elemental for a number of rounds equal to the character's rank in Elemental Hold. The character must concentrate to hold the elemental; he cannot move, cast spells, or take any action other than communication."""
    },
    {
        "id":
        "TE4",
        "name":
        "Elemental Tongues",
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
        "discipline_talent": ["elementalist"],
        "description":
        """The Elemental Tongues talent allows a character to speak the languages of air, earth, fire, and water--the four elemental tongues. Characters cannot communicate with wood or plant elementals using this talent, because it requires a special spell to unravel their peculiar tongue. Each rank in Elemental Tongues gives the speaker an additional elemental language. Rank 1 Elemental Tongues allows the character to speak one elemental language of his choice. At Rank 4, he can speak all four basic elemental languages. When speaking the language, the character makes a Talent Test against the Spell Defense of the elemental. The success level determines how well the character communicates with the elemental. On an Average or Good success, the elemental basically understands what the character is talking about, but the character is not able to ask complex questions or make requests. An Excellent or better success means the elemental completely understands the character. The character can discuss complex topics with the elemental and ask it detailed questions."""
    },
    {
        "id":
        "TE5",
        "name":
        "Emotion Song",
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
        "discipline_talent": ["troubadour"],
        "description":
        """The Emotion Song talent uses a character's powerful voice to sing songs that arouse an audience to a basic emotion such as fear, love, hate, happiness, anger, and joy. The audience directs the basic emotion at the subject of the song; if the character sings about a king, the audience feels the emotion about the king.
To perform Emotion Song requires at least half an hour. At the end of each half-hour the character makes a Talent Test against the highest Social Defense among the members of the audience. The success level determines how many members of the audience the character affects. An Average success indicates that one-quarter of the audience is affected by the song. A Good success affects half the audience, an Excellent success affects three-quarters, and an Extraordinary success means the entire audience is affected by the song.
Consecutive uses of Emotion Song create a cumulative effect. For example, two consecutive Average successes have the same effect as one Good success, two Good successes create the same effect as one Excellent success, and so on.
The effects of the song last a number of days equal to the character's rank in Emotion Song. During this time, affected characters are more susceptible to suggestions related to the emotion of the song. Characters making such suggestions add +1 step to any Interaction Tests. Characters making suggestions counter to the Emotion Song suffer a -1 step to Interaction Tests. See Gamemastering Earthdawn for information about Interaction Tests.
If a character fails an Emotion Song Test, he or she must immediately stop performing. The crowd has grown weary of the performance, and the character may not use Emotion Song again until the following morning."""
    },
    {
        "id":
        "TE6",
        "name":
        "Empathic Command",
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
        "discipline_talent": ["cavalryman"],
        "description":
        """The Empathic Command talent allows a character to command a mount through emotion and mental images. The character need not speak the commands, but must be in contact with the mount to use Empathic Command. The talent will not affect any other animal except his mount. A mount uses the character's Empathic Command step instead of its own Willpower step when making a Willpower Test to resist fear, charm, or spells directed at the mount or its rider"""
    },
    {
        "id":
        "TE7",
        "name":
        "Empathic Sense",
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
        "discipline_talent": ["troubadour"],
        "description":
        """The Empathic Sense talent allows a character to sense the feelings or emotions of another character. In order to use Empathic Sense, the character must "attune" the talent to a target character. This attuning remains in effect for a year and a day, or until the character changes the attunement. A character may attune to one character per rank of Empathic Sense. For example, a character with Rank 4 Empathic Sense could attune to up to four characters. To attune with a target character, the character must spend three minutes of quiet meditation with that character.
To use Empathic Sense, the character makes an Empathic Sense Test against the Spell Defense of the attuned target character to sense emotions or feelings. Empathic Sense also gives a character a vague sense of the location of an attuned character, within a 90-degree arc, but does not reveal distance. Empathic Sense is effective up to a range of miles equal to the character's Empathic Sense Rank."""
    },
    {
        "id":
        "TE8",
        "name":
        "Endure Cold",
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
        "discipline_talent": [],
        "description":
        """The Endure Cold talent allows characters to withstand damage caused by ice or cold temperatures. Each time a character takes freezing or cold damage, the character should immediately make an Endure Cold Test. A successful test result immediately reduces the damage by that amount, up to the amount of cold damage taken. Reduce the damage before determining Wounds, unconsciousness, or death.
Example: Cedric takes 9 points of cold damage from a Blizzard Sphere spell. His player rolls an 11 on an Endure Cold Test, removing all 9 points of damage, and so Cedric takes no damage from Blizzard Sphere. The remaining 2 points worth of the Endure Cold talent cannot be used to reduce any other damage Cedric may have taken.
A character can use Endure Cold a number of times each day equal to his talent rank. For example, a character with Rank 4 Endure Cold could use the talent 4 times per day."""
    },
    {
        "id":
        "TE9",
        "name":
        "Engaging Banter",
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
        1,
        "discipline_talent": ["troubadour"],
        "description":
        """The Engaging Banter talent allows a character to use his charming style and a touch of magical suggestion to distract an opponent. The target character must be able to understand what the character is saying in order for the talent to work. Engaging Banter may also be used in combat. The character makes an Engaging Banter Test against the target's Social Defense. If the test is successful, the target and the character spend time in witty, idle chatter. The banter lasts for a number of rounds equal to the character's rank in Engaging Banter. During this time, the target is distracted, suffering a -1 step to all tests and reducing all combat ratings (Physical Defense and so on) by -1. The character using Engaging Banter may end the banter any time, but this will also end the effect.
The talent can be used against targets under attack, but a successful attack that causes a Wound negates the effect of Engaging Banter, making the target character immune to further Engaging Banter for the next 24 hours."""
    },
    {
        "id":
        "TE10",
        "name":
        "Enhanced Matrix",
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
        0,
        "discipline_talent": [],
        "description":
        """Magicians learn the Enhanced Matrix talent to make better use of spells requiring threads. An Enhanced Matrix holds the pattern of a spell. Unlike a regular spell matrix, an Enhanced Matrix also holds one spell thread as well as the spell pattern. The magician weaves this thread when he attunes the Enhanced Matrix. This allows him to cast the spell without weaving the held thread."""
    },
    {
        "id":
        "TE11",
        "name":
        "Evidence Analysis",
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
        1,
        "discipline_talent": ["wizard"],
        "description":
        """A character uses the Evidence Analysis talent to examine physical evidence. This examination consists of equal parts observation, logic, and divination. A character might be able to examine a bed, for example, and determine that its occupant had not slept well, or he might be able to identify a weapon as a murder weapon. As a general rule, Evidence Analysis can only answer questions regarding what happened to an object or place or how something happened to an object or place. The character makes an Evidence Analysis Test against the Spell Defense of the person responsible for the physical evidence. In the above example, he would use the Spell Defense of the person who had slept in the bed. If the activity occurred in the previous 24 hours, the character using the talent can get a general impression of when the event happened (i.e., morning, afternoon, or evening). When using the Evidence Analysis talent to evaluate evidence more than 1 day old, add +1 to the target's Spell Defense for the Difficulty Number. This talent cannot help the character answer the questions of 'who' or 'why.'"""
    },
]
