talent_seeds_g = [
    {
        "id":
        "TG1",
        "name":
        "Gliding Stride",
        "attribute":
        "dexterity",
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
        "discipline_talent": ["warrior"],
        "description":
        """Gliding Stride is a movement talent that allows the character to move in a graceful glide through the air. For each use of this talent, the character makes a Gliding Stride Test. A successful result gives the maximum horizontal distance the character can move in 1 round using this talent, though the character still cannot move further horizontally than his Combat Movement. The effects of Gliding Stride last for a number of rounds equal to the character's rank in Gliding Stride. Gliding Stride suspends a character in midair, but cannot suspend him higher than a number of feet above the ground equal to 10 times the character's talent rank. If the character is suspended more than rank x 10 feet above the ground (say he stepped off a cliff), he falls to the ground, but only takes the damage he would have suffered from falling a distance equal to the difference between the Gliding Stride suspension limit and the actual height. The character also modifies the falling damage by a number of Armor Points equal to his rank in Gliding Stride.
Example: The Warrior Fezwit has Rank 2 Gliding Stride. His grappling partner pushes him off the top of a 100-foot tower. He falls all 100 feet to the ground, but takes only 80 feet worth of falling damage. He also modifies the falling damage by 2 Armor Points. (See Falling Damage)
If a character using Gliding Stride stands still at more than 2 feet above the ground, he slowly sinks toward the ground. The character loses 1D6 inches of altitude each round he remains stationary until he lands on the ground.
A character may use the Gliding Stride talent to move horizontally without suffering Strain; moving upward, however, does cause Strain. The character attempting to move vertically makes a Gliding Stride Test as above; a successful result gives the total number of feet (in this case both horizontal and vertical) the character may move using Gliding Stride. For each foot the character moves vertically, he must move 2 feet horizontally. Divide the Gliding Stride result by 3 to determine the maximum distance the character can move vertically using Gliding Stride."""
    },
    {
        "id":
        "TG2",
        "name":
        "Graceful Exit",
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
        """A character can escape combat by making an enchanted, Graceful Exit. To determine the Difficulty Number for the Talent Test, use the highest Social Defense Rating among the targeted group +1 for every other character in the group. Each targeted opponent must understand what the character says or else Graceful Exit has no effect. If the Graceful Exit Test is successful, the character must move away from the combat; he may not take any other action but that. The characters bedazzled by the Graceful Exit can take no action against the character using the talent for a number of rounds equal to the character's rank in Graceful Exit. Graceful Exit protects only the character using it; his or her associates must fend for themselves.
If the character returns to the combat after making a Graceful Exit, the characters affected by this talent become enraged. They try to attack the character, and are immune to all tests made against their Social Defense (any attempts to further influence them). Their anger adds +1 step to all their tests."""
    },
    {
        "id":
        "TG3",
        "name":
        "Great Leap",
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
        0,
        "discipline_talent": ["sky_raider"],
        "description":
        """The Great Leap talent allows characters to jump across large distances. Sky Raiders often use this talent to cross the chasms between airships and to leap clear of burning rigging and debris. To use this talent, the character rolls his Great Leap dice. The result is the number of yards he can jump, up to a maximum of his Combat Movement. Up to one-half the jump distance may be vertical. Great Leap may be used to avoid falling rigging, burning sails, or similar hazards. The Great Leap result replaces the character's Physical Defense Rating for the round in which the character uses the talent, even if that number is less than the character's normal Physical Defense."""
    },
]
