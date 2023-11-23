from Cartographie import Cartographie
from MissionControl import MissionControl
from SocketAdapter import SocketAdapter


if __name__ == "__main__":
    carto = Cartographie()
    houston = MissionControl(carto)
    houston.launchMission()
    
