import re

from pydenodo.models.vqlModels import VqlBaseView

pattern = r'CREATE OR REPLACE TABLE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?WRAPPER\s+\((\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)\)[\s\S]*?;+'

def parse(vql_str: str) -> list[VqlBaseView]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        result.append(VqlBaseView(id, match.group(1), match.group(3), match.group(4), match.group(0)))

    return result
