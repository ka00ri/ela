import gym 
import minihack
import nle 

from minihack import MiniHackNavigation
from minihack.envs import register

class MiniHackNewTask(MiniHackNavigation):
    def __init__(self, *args, des_file, **kwargs):
        kwargs["max_episode_steps"] = kwargs.pop("max_episode_steps", 1000)
        super().__init__(*args, des_file=des_file, **kwargs)

register(
    id="MiniHack-FunTimes-v0",
    entry_point="path.to.file:MiniHackNewTask", 
)


MOVE_ACTIONS = tuple(nle.nethack.CompassDirection)
NAVIGATE_ACTIONS = MOVE_ACTIONS + (
    nle.nethack.Command.MOVE,
    nle.nethack.Command.DROP,
    nle.nethack.Command.OPEN,
    nle.nethack.Command.EAT,
    nle.nethack.Command.FIGHT,
)


des_file = """
MAZE: "mylevel", ' '
GEOMETRY:center,center
MAP
|||||||||||||     
|...........|  |||
|...........||||.|
|...LL...........|
|...LLL..........|
|....LL.....||||.|
|...........|  |.|
|||||..||||||  |||
    ||||          
ENDMAP
STAIR:(11, 1),down
BRANCH: (1,3,1,3),(2,4,2,4)
DOOR:locked,(1,10)
"""

env = gym.make(
    "MiniHack-Navigation-Custom-v0",
    des_file=des_file,
    max_episode_steps=50,
    actions=NAVIGATE_ACTIONS
)
env.reset()
env.step(1)
env.render()



