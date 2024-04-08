from data_loader import _FvmOpenFOAM
from config import CFG

testing = _FvmOpenFOAM(CFG['DATA_ROOT'])



print(type(testing))

print(testing.files)