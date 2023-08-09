import re

from pydenodo.models.vqlModels import VqlWrapper

pattern = r'CREATE OR REPLACE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S][\s\S]*?;+'

def parse(vql_str: str) -> list[VqlWrapper]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "WRAPPER":
            result.append(VqlWrapper(id, match.group(3), match.group(1), match.group(0)))

    return result
