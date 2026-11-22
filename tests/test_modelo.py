import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from modelo import CampanaP

DEFECTOS = [28, 23, 22, 17, 16, 12, 12, 9]
def testgoelzero():
    c = CampanaP(DEFECTOS)
    assert c.goel(0, 150, 0.2) == 0
def testayrpositivos():
    c = CampanaP(DEFECTOS)
    assert c.acum[-1] == 139
    c.ajustar()
    assert c.restantes() > 0
