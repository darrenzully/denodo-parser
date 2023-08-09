import re

from pydenodo.models.vqlModels import VqlFolder

pattern = r'CREATE OR REPLACE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\'[^\']*[^\']*\'|\S*\S*)[\s\S][\s\S]*?;+'

def parse(vql_str: str) -> list[VqlFolder]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "FOLDER":
            result.append(VqlFolder(id, match.group(2), match.group(0)))

    return result
