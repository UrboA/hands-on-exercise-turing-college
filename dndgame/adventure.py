"""Adventure orchestration utilities.

Contains the `Adventure` class that manages encounters and story
progression for a single-player session.

Examples:
    >>> from dndgame.character import Character
    >>> from dndgame.adventure import Adventure
    >>> c = Character("Hero", "Human", 10)
    >>> c.roll_stats(); c.apply_racial_bonuses()
    >>> adv = Adventure("Intro", "A small quest.", c)
    >>> bool(adv.get_available_encounters_list())
    True
"""

from __future__ import annotations

from dndgame.character import Character


class Adventure:
    """A D&D adventure scenario with encounters and progression.

    Manages the overall adventure state, including player progression,
    encounters, and story elements.

    Attributes:
        name: The adventure's title/name.
        description: A description of the adventure's plot.
        player: The main character participating in the adventure.
        current_scene: The current location or scene in the adventure.
        completed_encounters: List of encounter names that have been completed.
        available_encounters: Dictionary of available encounters to choose from.
    """

    def __init__(self, name: str, description: str, player: Character) -> None:
        """Initialize a new adventure.

        Args:
            name: The adventure's title.
            description: A description of the adventure's main plot.
            player: The character who will participate in this adventure.
        """
        self.name: str = name
        self.description: str = description
        self.player: Character = player
        self.current_scene: str = "Starting Area"
        self.completed_encounters: list[str] = []
        self.available_encounters: dict[str, dict[str, str]] = {
            "goblin_ambush": {
                "name": "Goblin Ambush",
                "description": "A group of goblins blocks your path",
                "difficulty": "Easy"
            },
            "treasure_room": {
                "name": "Treasure Room",
                "description": "A room filled with treasure and traps",
                "difficulty": "Medium"
            },
            "dragon_lair": {
                "name": "Dragon's Lair",
                "description": "The final confrontation with an ancient dragon",
                "difficulty": "Hard"
            }
        }

    def start_adventure(self) -> None:
        """Begin the adventure and display the initial setup.

        Sets up the initial adventure state and provides the player
        with their starting scenario.
        """
        print(f"Beginning adventure: {self.name}")
        print(f"Description: {self.description}")
        print(f"Current location: {self.current_scene}")

    def choose_encounter(self, encounter_key: str) -> bool:
        """Attempt to start a specific encounter.

        Args:
            encounter_key: The key of the encounter to start.

        Returns:
            True if the encounter was successfully started, False if not available.

        Raises:
            KeyError: If the encounter_key doesn't exist in available_encounters.
        """
        if encounter_key not in self.available_encounters:
            raise KeyError(f"Encounter '{encounter_key}' not found")

        encounter = self.available_encounters[encounter_key]
        if encounter_key in self.completed_encounters:
            print(f"Encounter '{encounter['name']}' already completed!")
            return False

        print(f"Starting encounter: {encounter['name']}")
        print(f"Description: {encounter['description']}")
        print(f"Difficulty: {encounter['difficulty']}")
        return True

    def complete_encounter(self, encounter_key: str) -> None:
        """Mark an encounter as completed and provide rewards.

        Args:
            encounter_key: The key of the encounter that was completed.

        Raises:
            ValueError: If trying to complete an encounter that wasn't started
                       or doesn't exist.
        """
        if encounter_key not in self.available_encounters:
            raise ValueError(f"Encounter '{encounter_key}' not found")

        if encounter_key in self.completed_encounters:
            raise ValueError(f"Encounter '{encounter_key}' already completed")

        encounter = self.available_encounters[encounter_key]
        self.completed_encounters.append(encounter_key)

        # Provide rewards based on encounter difficulty
        if encounter["difficulty"] == "Easy":
            exp_gain = 100
        elif encounter["difficulty"] == "Medium":
            exp_gain = 250
        else:  # Hard
            exp_gain = 500

        print(f"Completed: {encounter['name']}")
        print(f"Experience gained: {exp_gain}")

    def get_available_encounters_list(self) -> list[str]:
        """Get a list of encounters that haven't been completed yet.

        Returns:
            List of encounter keys that are available to start.
        """
        return [key for key in self.available_encounters.keys()
                if key not in self.completed_encounters]

    def get_adventure_status(self) -> dict[str, str | list[str]]:
        """Get the current status of the adventure.

        Returns:
            Dictionary containing adventure name, current scene, completed
            encounters, and available encounters.
        """
        return {
            "name": self.name,
            "current_scene": self.current_scene,
            "completed_encounters": self.completed_encounters.copy(),
            "available_encounters": self.get_available_encounters_list()
        }