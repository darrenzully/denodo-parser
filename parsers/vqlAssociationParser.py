import re

from pydenodo.models.vqlModels import VqlAssociation

pattern = r'CREATE OR REPLACE ASSOCIATION\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;\n\nALTER\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'


def parse(vql_str: str) -> list[VqlAssociation]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        result.append(VqlAssociation(id, match.group(4), match.group(0)))

    return result
