#!/usr/local/env python3


class BattleAction(object):
    """
    Models an action in a battle. This includes all actions that can
    possibly taken during a battle including, but not limited to:
    Moving, Attacking and using an Ability, Skill or Trait.
    """

    def __init__(self):
        pass

    def action_point_cost(self):
        """
        Should be implemented in subclasses. This method should
        return the amount of action points this action costs to
        execute.
        :rtype: int
        """
        return 0

    def can_execute(self, combatant):
        """
        Checks whether a combatant can execute an anction or not
        :param Combatant combatant: The combatant
        :rtype: bool
        """
        return combatant.current_action_points() >= self.action_point_cost()

    def execute(self):
        """
        Should be implemented in subclasses.
        """
        pass

class WaitAction(BattleAction):
    """
    Implements an action that does nothing
    """

    def __init__(self):
        super(WaitAction, self).__init__()

    def action_point_cost(self):
        return 1

    def execute(self):
        pass


class EndTurnAction(BattleAction):
    """
    Implements the action that ends the turn
    """

    def __init__(self):
        super(EndTurnAction, self).__init__()

    def action_point_cost(self):
        return 0

    def execute(self):
        pass


class MoveAction(BattleAction):
    """
    Implements an action that moves a combatant

    :type _path: Path
    :type _combatant: Combatant
    """

    def __init__(self, combatant, path):
        """
        :param Combatant combatant: The combatant to move
        :param Path path: The path the combatant takes to move
        """
        super(MoveAction, self).__init__()
        self._combatant = combatant
        self._path = path

    def execute(self):
        start = self._path.first()
        end = self._path.last()
        start.remove_occupation(self._combatant)
        end.add_occupation(self._combatant)

    def can_execute(self, combatant):
        has_enough_action_points = super(MoveAction, self).can_execute(combatant)
        return self._path is not None and has_enough_action_points


class UseSkillAction(BattleAction):
    """
    Implements an action that uses a skill

    :type _character: Character
    :type _target: Combatant
    :type _skill_name: string
    """

    def __init__(self, character, target, skill_name):
        """
        :param Character character: The character that executes the skill
        :param Combatant target: The target to use the skill on
        """
        super(UseSkillAction, self).__init__()
        self._character = character
        self._target = target
        self._skill_name = skill_name

    def action_point_cost(self):
        return 1

    def execute(self):
        self._character.use_skill(self._skill_name)
