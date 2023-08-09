import re

from pydenodo.models.vqlModels import VqlRole

pattern_create = r'CREATE OR REPLACE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'
pattern_alter = r'ALTER\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'

def parse_create(vql_str: str) -> list[VqlRole]:
    pattern_compiled = re.compile(pattern_create)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "ROLE":
            result.append(VqlRole(id, match.group(2), match.group(0)))

    return result

def parse_alter(vql_str: str) -> list[VqlRole]:
    pattern_compiled = re.compile(pattern_alter)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "ROLE":
            result.append(VqlRole(id, match.group(2), match.group(0)))

    return result