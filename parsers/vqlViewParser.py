import re

from pydenodo.models.vqlModels import VqlView

pattern = r'CREATE OR REPLACE VIEW\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+[\s\S]*?;+'

def parse(vql_str: str) -> list[VqlView]:
    pattern_compiled = re.compile(pattern)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        has_dt = "DATAMOVEMENTPLAN" in match.group(0)
        is_remote = "REMOTE TABLE" in match.group(0)
        is_cons = "(SET IMPLEMENTATION)" in match.group(0)
        result.append(VqlView(id, match.group(1), has_dt, is_cons, is_remote, match.group(0)))

    return result
