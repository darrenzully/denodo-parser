from __future__ import annotations
from dataclasses import dataclass

import parsers.vqlDatasourceParser as vqlDatasourceParser
import parsers.vqlWebserviceParser as vqlWebserviceParser
import parsers.vqlWidgetParser as vqlWidgetParser
import parsers.vqlWrapperParser as vqlWrapperParser
import parsers.vqlListenerParser as vqlListenerParser
import parsers.vqlViewParser as vqlViewParser
import parsers.vqlBaseViewParser as vqlBaseViewParser
import parsers.vqlInterfaceParser as vqlInterfaceParser
import parsers.vqlDatabaseParser as vqlDatabaseParser
import parsers.vqlUserParser as vqlUserParser
import parsers.vqlRoleParser as vqlRoleParser
import parsers.vqlProcedureParser as vqlProcedureParser
import parsers.vqlTypeParser as vqlTypeParser
import parsers.vqlFolderParser as vqlFolderParser
import parsers.vqlMapParser as vqlMapParser
import parsers.vqlAssociationParser as vqlAssociationParser

from models.vqlFile import VqlFile


@dataclass
class VqlParser:
    @staticmethod
    def parse_from_path(file_path: str) -> VqlFile:
      vql_str = ""
      with open(file_path, 'r', encoding="utf-8") as f:
         vql_str = f.read()

      return VqlParser.parse_from_str(vql_str)

    @staticmethod
    def parse_from_str(vql_str: str) -> VqlFile:
      database = vqlDatabaseParser.parse_create(vql_str)
      vql_file = VqlFile(database.name)    
      vql_file.create_users = vqlUserParser.parse_create(vql_str)
      vql_file.create_roles = vqlRoleParser.parse_create(vql_str)
      vql_file.create_folders = vqlFolderParser.parse(vql_str)
      vql_file.create_listeners = vqlListenerParser.parse(vql_str)
      vql_file.create_datasources = vqlDatasourceParser.parse(vql_str)
      vql_file.create_database = database
      vql_file.alter_database = vqlDatabaseParser.parse_alter(vql_str)
      vql_file.create_wrappers = vqlWrapperParser.parse(vql_str)
      vql_file.create_procedures = vqlProcedureParser.parse(vql_str)
      vql_file.create_types = vqlTypeParser.parse( vql_str)
      vql_file.create_maps = vqlMapParser.parse(vql_str)
      vql_file.create_base_views = vqlBaseViewParser.parse(vql_str)
      vql_file.create_views = vqlViewParser.parse(vql_str)
      vql_file.create_interfaces = vqlInterfaceParser.parse(vql_str)
      vql_file.create_associations = vqlAssociationParser.parse(vql_str)
      vql_file.create_widgets = vqlWidgetParser.parse_create(vql_str)
      vql_file.create_services = vqlWebserviceParser.parse_create(vql_str)
      vql_file.deploy_services = vqlWebserviceParser.parse_deploy(vql_str)
      vql_file.deploy_widgets = vqlWidgetParser.parse_deploy(vql_str)
      vql_file.undeploy_services = vqlWebserviceParser.parse_undeploy(vql_str)
      vql_file.undeploy_widgets = vqlWidgetParser.parse_undeploy(vql_str)
      vql_file.alter_roles = vqlRoleParser.parse_alter(vql_str)
      vql_file.alter_users = vqlUserParser.parse_alter(vql_str)

      return vql_file