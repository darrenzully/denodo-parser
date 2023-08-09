import re

from pydenodo.models.vqlModels import VqlDatabase

pattern_create = r'CREATE OR REPLACE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'
pattern_alter = r'ALTER DATABASE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'


def parse_create(vql_str: str) -> VqlDatabase:
    pattern_compiled = re.compile(pattern_create)

    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "DATABASE":
            result = VqlDatabase(id, match.group(2), match.group(0))

    return result

def parse_alter(vql_str: str) -> list[VqlDatabase]:
    pattern_compiled = re.compile(pattern_alter)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        result.append(VqlDatabase(id, match.group(2), match.group(0)))

    return result