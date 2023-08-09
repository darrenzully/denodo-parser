import re

from pydenodo.models.vqlModels import VqlType

pattern = r'CREATE OR REPLACE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'

def parse(vql_str: str) -> list[VqlType]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "TYPE":
            result.append(VqlType(id, match.group(2), match.group(0)))

    return result
