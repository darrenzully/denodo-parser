import re

from pydenodo.models.vqlModels import VqlWidget

pattern_create = r'CREATE OR REPLACE\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S][\s\S]*?;+'
pattern_undeploy_service = r'UNDEPLOY IF EXISTS\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)*?;+'
pattern_deploy_service = r'^DEPLOY\s+(\"[^\"]*[^\"]*\"|\S*\S*)\s+(\"[^\"]*[^\"]*\"|\S*\S*)[\s\S]*?;+'

def parse_create(vql_str: str) -> list[VqlWidget]:
    pattern_compiled = re.compile(pattern_create)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(2) == "WIDGET":
            result.append(VqlWidget(id, match.group(3), match.group(0)))

    return result

def parse_undeploy(vql_str: str) -> list[VqlWidget]:
    pattern_compiled = re.compile(pattern_undeploy_service)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "WIDGET":
            result.append(VqlWidget(id, match.group(2), match.group(0)))

    return result

def parse_deploy(vql_str: str) -> list[VqlWidget]:
    pattern_compiled = re.compile(pattern_deploy_service)

    result = []
    for id, match in enumerate(pattern_compiled.finditer(vql_str)):
        if match.group(1) == "WIDGET":
            result.append(VqlWidget(id, match.group(2), match.group(0)))

    return result