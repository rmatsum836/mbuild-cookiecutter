"""
Primary function of recipe here
"""

import mbuild as mb

class {{cookiecutter.first_plugin_name}}(mb.Compound):
    """
    Example class that would go in your recipe.

    Parameters
    ----------
    your_argument: int
        This is an example argument

    """
    def __init__(self):
        super({{cookiecutter.first_plugin_name}}, self).__init__()
        # Sample of how a compound would be added in mBuild
        sample = mb.Particle(pos=[0.0, 0.0, 0.0], name='test')
        self.add(bead)
