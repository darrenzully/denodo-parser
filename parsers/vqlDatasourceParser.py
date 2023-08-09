import re

from pydenodo.models.vqlModels import VqlDatasource

pattern = r'CREATE OR REPLACE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S][\s\S]*?;+'

def parse(vql_str: str) -> list[VqlDatasource]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "DATASOURCE":
            result.append(VqlDatasource(id, match.group(3), match.group(1),  match.group(0)))

    return result
