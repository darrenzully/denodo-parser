import re

from pydenodo.models.vqlModels import VqlMap

pattern = r'CREATE MAP\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'

def parse(vql_str: str) -> list[VqlMap]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        result.append(VqlMap(id, match.group(2), match.group(0)))

    return result
