import re

from pydenodo.models.vqlModels import VqlInterfaceView

pattern = r'CREATE OR REPLACE INTERFACE VIEW\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+[\s\S]*?;\n\nALTER VIEW\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+[\s\S]*?;+'

def parse(vql_str: str) -> list[VqlInterfaceView]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "INTERFACE":
            result.append(VqlInterfaceView(id, match.group(1), match.group(0)))

    return result
