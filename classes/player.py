from gem import gem
from rock import rock


class player():
    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        
    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result