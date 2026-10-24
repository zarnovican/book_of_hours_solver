# load the modules in a specific order. Model first..
from . import model

# ..then data
from . import (
    opportunity,
    recipe,
    room,
)
