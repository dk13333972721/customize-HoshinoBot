from hoshino import Service

sv_help = '''
[谁是霸瞳] 角色别称查询
[黄骑充能] 由加莉1动规律
[角色站位] 角色站位表
'''.strip()

sv = Service('pcr-query', help_=sv_help, bundle='pcr查询')

from .query import *
from .whois import *
from .miner import *
from .rank import *