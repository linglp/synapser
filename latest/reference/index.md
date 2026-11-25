# Package index

## Client

Functions for authenticating with and configuring the Synapse client.

- [`synLogin()`](https://linglp.github.io/synapser/latest/reference/synLogin.md)
  : synLogin
- [`synLogout()`](https://linglp.github.io/synapser/latest/reference/synLogout.md)
  : synLogout
- [`synSetEndpoints()`](https://linglp.github.io/synapser/latest/reference/synSetEndpoints.md)
  : synSetEndpoints

## Entities

Functions for getting, storing, querying, and managing Synapse entities.

- [`synGet()`](https://linglp.github.io/synapser/latest/reference/synGet.md)
  : synGet
- [`FileOptions()`](https://linglp.github.io/synapser/latest/reference/FileOptions.md)
  : FileOptions
- [`ActivityOptions()`](https://linglp.github.io/synapser/latest/reference/ActivityOptions.md)
  : ActivityOptions
- [`TableOptions()`](https://linglp.github.io/synapser/latest/reference/TableOptions.md)
  : TableOptions
- [`LinkOptions()`](https://linglp.github.io/synapser/latest/reference/LinkOptions.md)
  : LinkOptions
- [`synStore()`](https://linglp.github.io/synapser/latest/reference/synStore.md)
  : synStore
- [`synSetProperties()`](https://linglp.github.io/synapser/latest/reference/synSetProperties.md)
  : Set properties of an entity
- [`StoreFileOptions()`](https://linglp.github.io/synapser/latest/reference/StoreFileOptions.md)
  : StoreFileOptions
- [`StoreContainerOptions()`](https://linglp.github.io/synapser/latest/reference/StoreContainerOptions.md)
  : StoreContainerOptions
- [`StoreTableOptions()`](https://linglp.github.io/synapser/latest/reference/StoreTableOptions.md)
  : StoreTableOptions
- [`StoreJSONSchemaOptions()`](https://linglp.github.io/synapser/latest/reference/StoreJSONSchemaOptions.md)
  : StoreJSONSchemaOptions
- [`StoreGridOptions()`](https://linglp.github.io/synapser/latest/reference/StoreGridOptions.md)
  : StoreGridOptions
- [`synDelete()`](https://linglp.github.io/synapser/latest/reference/synDelete.md)
  : synDelete
- [`synFindEntityId()`](https://linglp.github.io/synapser/latest/reference/synFindEntityId.md)
  : synFindEntityId
- [`synIsSynapseId()`](https://linglp.github.io/synapser/latest/reference/synIsSynapseId.md)
  : synIsSynapseId
- [`synOnweb()`](https://linglp.github.io/synapser/latest/reference/synOnweb.md)
  : synOnweb
- [`synPrintEntity()`](https://linglp.github.io/synapser/latest/reference/synPrintEntity.md)
  : synPrintEntity
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_Query.md)
  : VirtualTable : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_QueryPartMask.md)
  : VirtualTable : query_part_mask
- [`synMd5Query()`](https://linglp.github.io/synapser/latest/reference/synMd5Query.md)
  : synMd5Query
- [`synSendMessage()`](https://linglp.github.io/synapser/latest/reference/synSendMessage.md)
  : synSendMessage

## REST API

Low-level functions for making direct REST calls to the Synapse server.

- [`synRestGet()`](https://linglp.github.io/synapser/latest/reference/synRestGet.md)
  : synRestGet
- [`synRestPost()`](https://linglp.github.io/synapser/latest/reference/synRestPost.md)
  : synRestPost
- [`synRestPut()`](https://linglp.github.io/synapser/latest/reference/synRestPut.md)
  : synRestPut
- [`synRestDelete()`](https://linglp.github.io/synapser/latest/reference/synRestDelete.md)
  : synRestDelete

## Agent

Represents a [Synapse Agent
Registration](https://rest-docs.synapse.org/rest/org/sagebionetworks/repo/model/agent/AgentRegistration.html).

- [`Agent()`](https://linglp.github.io/synapser/latest/reference/Agent.md)
  : Agent
- [`synGetChatHistory()`](https://linglp.github.io/synapser/latest/reference/Agent_GetChatHistory.md)
  : Agent : get_chat_history
- [`synGetSession()`](https://linglp.github.io/synapser/latest/reference/Agent_GetSession.md)
  : Agent : get_session
- [`synPrompt()`](https://linglp.github.io/synapser/latest/reference/Agent_Prompt.md)
  : Agent : prompt
- [`synRegister()`](https://linglp.github.io/synapser/latest/reference/Agent_Register.md)
  : Agent : register
- [`synStartSession()`](https://linglp.github.io/synapser/latest/reference/Agent_StartSession.md)
  : Agent : start_session

## AgentSession

Represents a [Synapse Agent
Session](https://rest-docs.synapse.org/rest/org/sagebionetworks/repo/model/agent/AgentSession.html).

- [`AgentSession()`](https://linglp.github.io/synapser/latest/reference/AgentSession.md)
  : AgentSession
- [`synPrompt()`](https://linglp.github.io/synapser/latest/reference/AgentSession_Prompt.md)
  : AgentSession : prompt
- [`synStart()`](https://linglp.github.io/synapser/latest/reference/AgentSession_Start.md)
  : AgentSession : start
- [`synUpdate()`](https://linglp.github.io/synapser/latest/reference/AgentSession_Update.md)
  : AgentSession : update

## AgentPrompt

Represents a prompt, response, and metadata within an AgentSession.

- [`AgentPrompt()`](https://linglp.github.io/synapser/latest/reference/AgentPrompt.md)
  : AgentPrompt

## Folder

Folder is a hierarchical container for organizing data in Synapse.

- [`Folder()`](https://linglp.github.io/synapser/latest/reference/Folder.md)
  : Folder
- [`synBindSchema()`](https://linglp.github.io/synapser/latest/reference/Folder_BindSchema.md)
  : Folder : bind_schema
- [`synCopy()`](https://linglp.github.io/synapser/latest/reference/Folder_Copy.md)
  : Folder : copy
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/Folder_DeletePermissions.md)
  : Folder : delete_permissions
- [`synDeleteProjectSetting()`](https://linglp.github.io/synapser/latest/reference/Folder_DeleteProjectSetting.md)
  : Folder : delete_project_setting
- [`synFlattenFileList()`](https://linglp.github.io/synapser/latest/reference/Folder_FlattenFileList.md)
  : Folder : flatten_file_list
- [`synGenerateSyncManifest()`](https://linglp.github.io/synapser/latest/reference/Folder_GenerateSyncManifest.md)
  : Folder : generate_sync_manifest
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/Folder_GetAcl.md)
  : Folder : get_acl
- [`synGetInvalidValidation()`](https://linglp.github.io/synapser/latest/reference/Folder_GetInvalidValidation.md)
  : Folder : get_invalid_validation
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/Folder_GetPermissions.md)
  : Folder : get_permissions
- [`synGetProjectSetting()`](https://linglp.github.io/synapser/latest/reference/Folder_GetProjectSetting.md)
  : Folder : get_project_setting
- [`synGetSchema()`](https://linglp.github.io/synapser/latest/reference/Folder_GetSchema.md)
  : Folder : get_schema
- [`synGetSchemaDerivedKeys()`](https://linglp.github.io/synapser/latest/reference/Folder_GetSchemaDerivedKeys.md)
  : Folder : get_schema_derived_keys
- [`synGetSchemaValidationStatistics()`](https://linglp.github.io/synapser/latest/reference/Folder_GetSchemaValidationStatistics.md)
  : Folder : get_schema_validation_statistics
- [`synGetStsStorageToken()`](https://linglp.github.io/synapser/latest/reference/Folder_GetStsStorageToken.md)
  : Folder : get_sts_storage_token
- [`synIndexFilesForMigration()`](https://linglp.github.io/synapser/latest/reference/Folder_IndexFilesForMigration.md)
  : Folder : index_files_for_migration
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/Folder_ListAcl.md)
  : Folder : list_acl
- [`synMapDirectoryToAllContainedFiles()`](https://linglp.github.io/synapser/latest/reference/Folder_MapDirectoryToAllContainedFiles.md)
  : Folder : map_directory_to_all_contained_files
- [`synMigrateIndexedFiles()`](https://linglp.github.io/synapser/latest/reference/Folder_MigrateIndexedFiles.md)
  : Folder : migrate_indexed_files
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/Folder_SetPermissions.md)
  : Folder : set_permissions
- [`synSetStorageLocation()`](https://linglp.github.io/synapser/latest/reference/Folder_SetStorageLocation.md)
  : Folder : set_storage_location
- [`synSyncFromSynapse()`](https://linglp.github.io/synapser/latest/reference/Folder_SyncFromSynapse.md)
  : Folder : sync_from_synapse
- [`synSyncToSynapse()`](https://linglp.github.io/synapser/latest/reference/Folder_SyncToSynapse.md)
  : Folder : sync_to_synapse
- [`synUnbindSchema()`](https://linglp.github.io/synapser/latest/reference/Folder_UnbindSchema.md)
  : Folder : unbind_schema
- [`synValidateSchema()`](https://linglp.github.io/synapser/latest/reference/Folder_ValidateSchema.md)
  : Folder : validate_schema
- [`synWalk()`](https://linglp.github.io/synapser/latest/reference/Folder_Walk.md)
  : Folder : walk

## File

A file within Synapse.

- [`File()`](https://linglp.github.io/synapser/latest/reference/File.md)
  : File
- [`synBindSchema()`](https://linglp.github.io/synapser/latest/reference/File_BindSchema.md)
  : File : bind_schema
- [`synChangeMetadata()`](https://linglp.github.io/synapser/latest/reference/File_ChangeMetadata.md)
  : File : change_metadata
- [`synCopy()`](https://linglp.github.io/synapser/latest/reference/File_Copy.md)
  : File : copy
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/File_DeletePermissions.md)
  : File : delete_permissions
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/File_GetAcl.md)
  : File : get_acl
- [`synGetFromId()`](https://linglp.github.io/synapser/latest/reference/File_GetFromId.md)
  : File : from_id
- [`synGetFromPath()`](https://linglp.github.io/synapser/latest/reference/File_GetFromPath.md)
  : File : from_path
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/File_GetPermissions.md)
  : File : get_permissions
- [`synGetSchema()`](https://linglp.github.io/synapser/latest/reference/File_GetSchema.md)
  : File : get_schema
- [`synGetSchemaDerivedKeys()`](https://linglp.github.io/synapser/latest/reference/File_GetSchemaDerivedKeys.md)
  : File : get_schema_derived_keys
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/File_ListAcl.md)
  : File : list_acl
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/File_SetPermissions.md)
  : File : set_permissions
- [`synUnbindSchema()`](https://linglp.github.io/synapser/latest/reference/File_UnbindSchema.md)
  : File : unbind_schema
- [`synValidateSchema()`](https://linglp.github.io/synapser/latest/reference/File_ValidateSchema.md)
  : File : validate_schema

## Project

A Project is a top-level container for organizing data in Synapse.

- [`Project()`](https://linglp.github.io/synapser/latest/reference/Project.md)
  : Project
- [`synBindSchema()`](https://linglp.github.io/synapser/latest/reference/Project_BindSchema.md)
  : Project : bind_schema
- [`synCopy()`](https://linglp.github.io/synapser/latest/reference/Project_Copy.md)
  : Project : copy
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/Project_DeletePermissions.md)
  : Project : delete_permissions
- [`synDeleteProjectSetting()`](https://linglp.github.io/synapser/latest/reference/Project_DeleteProjectSetting.md)
  : Project : delete_project_setting
- [`synFlattenFileList()`](https://linglp.github.io/synapser/latest/reference/Project_FlattenFileList.md)
  : Project : flatten_file_list
- [`synGenerateSyncManifest()`](https://linglp.github.io/synapser/latest/reference/Project_GenerateSyncManifest.md)
  : Project : generate_sync_manifest
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/Project_GetAcl.md)
  : Project : get_acl
- [`synGetInvalidValidation()`](https://linglp.github.io/synapser/latest/reference/Project_GetInvalidValidation.md)
  : Project : get_invalid_validation
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/Project_GetPermissions.md)
  : Project : get_permissions
- [`synGetProjectSetting()`](https://linglp.github.io/synapser/latest/reference/Project_GetProjectSetting.md)
  : Project : get_project_setting
- [`synGetSchema()`](https://linglp.github.io/synapser/latest/reference/Project_GetSchema.md)
  : Project : get_schema
- [`synGetSchemaDerivedKeys()`](https://linglp.github.io/synapser/latest/reference/Project_GetSchemaDerivedKeys.md)
  : Project : get_schema_derived_keys
- [`synGetSchemaValidationStatistics()`](https://linglp.github.io/synapser/latest/reference/Project_GetSchemaValidationStatistics.md)
  : Project : get_schema_validation_statistics
- [`synGetStsStorageToken()`](https://linglp.github.io/synapser/latest/reference/Project_GetStsStorageToken.md)
  : Project : get_sts_storage_token
- [`synIndexFilesForMigration()`](https://linglp.github.io/synapser/latest/reference/Project_IndexFilesForMigration.md)
  : Project : index_files_for_migration
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/Project_ListAcl.md)
  : Project : list_acl
- [`synMapDirectoryToAllContainedFiles()`](https://linglp.github.io/synapser/latest/reference/Project_MapDirectoryToAllContainedFiles.md)
  : Project : map_directory_to_all_contained_files
- [`synMigrateIndexedFiles()`](https://linglp.github.io/synapser/latest/reference/Project_MigrateIndexedFiles.md)
  : Project : migrate_indexed_files
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/Project_SetPermissions.md)
  : Project : set_permissions
- [`synSetStorageLocation()`](https://linglp.github.io/synapser/latest/reference/Project_SetStorageLocation.md)
  : Project : set_storage_location
- [`synSyncFromSynapse()`](https://linglp.github.io/synapser/latest/reference/Project_SyncFromSynapse.md)
  : Project : sync_from_synapse
- [`synSyncToSynapse()`](https://linglp.github.io/synapser/latest/reference/Project_SyncToSynapse.md)
  : Project : sync_to_synapse
- [`synUnbindSchema()`](https://linglp.github.io/synapser/latest/reference/Project_UnbindSchema.md)
  : Project : unbind_schema
- [`synValidateSchema()`](https://linglp.github.io/synapser/latest/reference/Project_ValidateSchema.md)
  : Project : validate_schema
- [`synWalk()`](https://linglp.github.io/synapser/latest/reference/Project_Walk.md)
  : Project : walk

## Evaluation

An Evaluation is the core object of the Evaluation API, used to support
collaborative data analysis challenges in Synapse.

- [`Evaluation()`](https://linglp.github.io/synapser/latest/reference/Evaluation.md)
  : Evaluation
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/Evaluation_GetAcl.md)
  : Evaluation : get_acl
- [`synGetAllEvaluations()`](https://linglp.github.io/synapser/latest/reference/Evaluation_GetAllEvaluations.md)
  : Evaluation : get_all_evaluations
- [`synGetAvailableEvaluations()`](https://linglp.github.io/synapser/latest/reference/Evaluation_GetAvailableEvaluations.md)
  : Evaluation : get_available_evaluations
- [`synGetEvaluationsByProject()`](https://linglp.github.io/synapser/latest/reference/Evaluation_GetEvaluationsByProject.md)
  : Evaluation : get_evaluations_by_project
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/Evaluation_GetPermissions.md)
  : Evaluation : get_permissions
- [`synUpdateAcl()`](https://linglp.github.io/synapser/latest/reference/Evaluation_UpdateAcl.md)
  : Evaluation : update_acl

## Submission

A `Submission` object represents a Synapse Submission, which is created
when a user submits an entity to an evaluation queue.

- [`Submission()`](https://linglp.github.io/synapser/latest/reference/Submission.md)
  : Submission
- [`synCancel()`](https://linglp.github.io/synapser/latest/reference/Submission_Cancel.md)
  : Submission : cancel
- [`synGetEvaluationSubmissions()`](https://linglp.github.io/synapser/latest/reference/Submission_GetEvaluationSubmissions.md)
  : Submission : get_evaluation_submissions
- [`synGetSubmissionCount()`](https://linglp.github.io/synapser/latest/reference/Submission_GetSubmissionCount.md)
  : Submission : get_submission_count
- [`synGetUserSubmissions()`](https://linglp.github.io/synapser/latest/reference/Submission_GetUserSubmissions.md)
  : Submission : get_user_submissions

## SubmissionStatus

A SubmissionStatus is a secondary, mutable object associated with a
Submission.

- [`SubmissionStatus()`](https://linglp.github.io/synapser/latest/reference/SubmissionStatus.md)
  : SubmissionStatus
- [`synBatchUpdateSubmissionStatuses()`](https://linglp.github.io/synapser/latest/reference/SubmissionStatus_BatchUpdateSubmissionStatuses.md)
  : SubmissionStatus : batch_update_submission_statuses
- [`synGetAllSubmissionStatuses()`](https://linglp.github.io/synapser/latest/reference/SubmissionStatus_GetAllSubmissionStatuses.md)
  : SubmissionStatus : get_all_submission_statuses

## SubmissionBundle

A `SubmissionBundle` object represents a bundle containing a Synapse
Submission and its accompanying SubmissionStatus.

- [`SubmissionBundle()`](https://linglp.github.io/synapser/latest/reference/SubmissionBundle.md)
  : SubmissionBundle
- [`synGetEvaluationSubmissionBundles()`](https://linglp.github.io/synapser/latest/reference/SubmissionBundle_GetEvaluationSubmissionBundles.md)
  : SubmissionBundle : get_evaluation_submission_bundles
- [`synGetUserSubmissionBundles()`](https://linglp.github.io/synapser/latest/reference/SubmissionBundle_GetUserSubmissionBundles.md)
  : SubmissionBundle : get_user_submission_bundles

## Table

A Table represents the metadata of a table.

- [`Table()`](https://linglp.github.io/synapser/latest/reference/Table.md)
  : Table
- [`synAddColumn()`](https://linglp.github.io/synapser/latest/reference/Table_AddColumn.md)
  : Table : add_column
- [`synBindSchema()`](https://linglp.github.io/synapser/latest/reference/Table_BindSchema.md)
  : Table : bind_schema
- [`synDeleteColumn()`](https://linglp.github.io/synapser/latest/reference/Table_DeleteColumn.md)
  : Table : delete_column
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/Table_DeletePermissions.md)
  : Table : delete_permissions
- [`synDeleteRows()`](https://linglp.github.io/synapser/latest/reference/Table_DeleteRows.md)
  : Table : delete_rows
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/Table_GetAcl.md)
  : Table : get_acl
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/Table_GetPermissions.md)
  : Table : get_permissions
- [`synGetSchema()`](https://linglp.github.io/synapser/latest/reference/Table_GetSchema.md)
  : Table : get_schema
- [`synGetSchemaDerivedKeys()`](https://linglp.github.io/synapser/latest/reference/Table_GetSchemaDerivedKeys.md)
  : Table : get_schema_derived_keys
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/Table_ListAcl.md)
  : Table : list_acl
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/Table_Query.md)
  : Table : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/Table_QueryPartMask.md)
  : Table : query_part_mask
- [`synReorderColumn()`](https://linglp.github.io/synapser/latest/reference/Table_ReorderColumn.md)
  : Table : reorder_column
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/Table_SetPermissions.md)
  : Table : set_permissions
- [`synSnapshot()`](https://linglp.github.io/synapser/latest/reference/Table_Snapshot.md)
  : Table : snapshot
- [`synStoreRows()`](https://linglp.github.io/synapser/latest/reference/Table_StoreRows.md)
  : Table : store_rows
- [`synUnbindSchema()`](https://linglp.github.io/synapser/latest/reference/Table_UnbindSchema.md)
  : Table : unbind_schema
- [`synUpsertRows()`](https://linglp.github.io/synapser/latest/reference/Table_UpsertRows.md)
  : Table : upsert_rows
- [`synValidateSchema()`](https://linglp.github.io/synapser/latest/reference/Table_ValidateSchema.md)
  : Table : validate_schema

## Column

A column model contains the metadata of a single column of a table or
view.

- [`Column()`](https://linglp.github.io/synapser/latest/reference/Column.md)
  : Column
- [`synList()`](https://linglp.github.io/synapser/latest/reference/Column_List.md)
  : Column : list
- [`JsonSubColumn()`](https://linglp.github.io/synapser/latest/reference/JsonSubColumn.md)
  : JsonSubColumn

## VirtualTable

A virtual table is a type of table that is dynamically built from a
Synapse SQL query.

- [`VirtualTable()`](https://linglp.github.io/synapser/latest/reference/VirtualTable.md)
  : VirtualTable
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_DeletePermissions.md)
  : VirtualTable : delete_permissions
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_GetAcl.md)
  : VirtualTable : get_acl
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_GetPermissions.md)
  : VirtualTable : get_permissions
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_ListAcl.md)
  : VirtualTable : list_acl
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_Query.md)
  : VirtualTable : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_QueryPartMask.md)
  : VirtualTable : query_part_mask
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/VirtualTable_SetPermissions.md)
  : VirtualTable : set_permissions

## Dataset

A `Dataset` object represents the metadata of a Synapse Dataset.

- [`Dataset()`](https://linglp.github.io/synapser/latest/reference/Dataset.md)
  : Dataset
- [`synAddColumn()`](https://linglp.github.io/synapser/latest/reference/Dataset_AddColumn.md)
  : Dataset : add_column
- [`synAddItem()`](https://linglp.github.io/synapser/latest/reference/Dataset_AddItem.md)
  : Dataset : add_item
- [`synDeleteColumn()`](https://linglp.github.io/synapser/latest/reference/Dataset_DeleteColumn.md)
  : Dataset : delete_column
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/Dataset_DeletePermissions.md)
  : Dataset : delete_permissions
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/Dataset_GetAcl.md)
  : Dataset : get_acl
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/Dataset_GetPermissions.md)
  : Dataset : get_permissions
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/Dataset_ListAcl.md)
  : Dataset : list_acl
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/Dataset_Query.md)
  : Dataset : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/Dataset_QueryPartMask.md)
  : Dataset : query_part_mask
- [`synRemoveItem()`](https://linglp.github.io/synapser/latest/reference/Dataset_RemoveItem.md)
  : Dataset : remove_item
- [`synReorderColumn()`](https://linglp.github.io/synapser/latest/reference/Dataset_ReorderColumn.md)
  : Dataset : reorder_column
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/Dataset_SetPermissions.md)
  : Dataset : set_permissions
- [`synSnapshot()`](https://linglp.github.io/synapser/latest/reference/Dataset_Snapshot.md)
  : Dataset : snapshot
- [`synUpdateRows()`](https://linglp.github.io/synapser/latest/reference/Dataset_UpdateRows.md)
  : Dataset : update_rows

## DatasetCollection

A `DatasetCollection` object represents the metadata of a Synapse
Dataset Collection.

- [`DatasetCollection()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection.md)
  : DatasetCollection
- [`synAddColumn()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_AddColumn.md)
  : DatasetCollection : add_column
- [`synAddItem()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_AddItem.md)
  : DatasetCollection : add_item
- [`synDeleteColumn()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_DeleteColumn.md)
  : DatasetCollection : delete_column
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_DeletePermissions.md)
  : DatasetCollection : delete_permissions
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_GetAcl.md)
  : DatasetCollection : get_acl
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_GetPermissions.md)
  : DatasetCollection : get_permissions
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_ListAcl.md)
  : DatasetCollection : list_acl
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_Query.md)
  : DatasetCollection : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_QueryPartMask.md)
  : DatasetCollection : query_part_mask
- [`synRemoveItem()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_RemoveItem.md)
  : DatasetCollection : remove_item
- [`synReorderColumn()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_ReorderColumn.md)
  : DatasetCollection : reorder_column
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_SetPermissions.md)
  : DatasetCollection : set_permissions
- [`synSnapshot()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_Snapshot.md)
  : DatasetCollection : snapshot
- [`synUpdateRows()`](https://linglp.github.io/synapser/latest/reference/DatasetCollection_UpdateRows.md)
  : DatasetCollection : update_rows
- [`EntityRef()`](https://linglp.github.io/synapser/latest/reference/EntityRef.md)
  : EntityRef

## EntityView

A view of Entities within a defined scope.

- [`EntityView()`](https://linglp.github.io/synapser/latest/reference/EntityView.md)
  : EntityView
- [`synAddColumn()`](https://linglp.github.io/synapser/latest/reference/EntityView_AddColumn.md)
  : EntityView : add_column
- [`synBindSchema()`](https://linglp.github.io/synapser/latest/reference/EntityView_BindSchema.md)
  : EntityView : bind_schema
- [`synDeleteColumn()`](https://linglp.github.io/synapser/latest/reference/EntityView_DeleteColumn.md)
  : EntityView : delete_column
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/EntityView_DeletePermissions.md)
  : EntityView : delete_permissions
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/EntityView_GetAcl.md)
  : EntityView : get_acl
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/EntityView_GetPermissions.md)
  : EntityView : get_permissions
- [`synGetSchema()`](https://linglp.github.io/synapser/latest/reference/EntityView_GetSchema.md)
  : EntityView : get_schema
- [`synGetSchemaDerivedKeys()`](https://linglp.github.io/synapser/latest/reference/EntityView_GetSchemaDerivedKeys.md)
  : EntityView : get_schema_derived_keys
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/EntityView_ListAcl.md)
  : EntityView : list_acl
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/EntityView_Query.md)
  : EntityView : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/EntityView_QueryPartMask.md)
  : EntityView : query_part_mask
- [`synReorderColumn()`](https://linglp.github.io/synapser/latest/reference/EntityView_ReorderColumn.md)
  : EntityView : reorder_column
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/EntityView_SetPermissions.md)
  : EntityView : set_permissions
- [`synSnapshot()`](https://linglp.github.io/synapser/latest/reference/EntityView_Snapshot.md)
  : EntityView : snapshot
- [`synUnbindSchema()`](https://linglp.github.io/synapser/latest/reference/EntityView_UnbindSchema.md)
  : EntityView : unbind_schema
- [`synUpdateRows()`](https://linglp.github.io/synapser/latest/reference/EntityView_UpdateRows.md)
  : EntityView : update_rows
- [`synValidateSchema()`](https://linglp.github.io/synapser/latest/reference/EntityView_ValidateSchema.md)
  : EntityView : validate_schema

## MaterializedView

A materialized view is a type of table that is automatically built from
a Synapse SQL query.

- [`MaterializedView()`](https://linglp.github.io/synapser/latest/reference/MaterializedView.md)
  : MaterializedView
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/MaterializedView_DeletePermissions.md)
  : MaterializedView : delete_permissions
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/MaterializedView_GetAcl.md)
  : MaterializedView : get_acl
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/MaterializedView_GetPermissions.md)
  : MaterializedView : get_permissions
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/MaterializedView_ListAcl.md)
  : MaterializedView : list_acl
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/MaterializedView_Query.md)
  : MaterializedView : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/MaterializedView_QueryPartMask.md)
  : MaterializedView : query_part_mask
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/MaterializedView_SetPermissions.md)
  : MaterializedView : set_permissions

## SubmissionView

A `SubmissionView` object represents the metadata of a Synapse
Submission View.

- [`SubmissionView()`](https://linglp.github.io/synapser/latest/reference/SubmissionView.md)
  : Constructor for objects of type SubmissionView
- [`synAddColumn()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_AddColumn.md)
  : SubmissionView : add_column
- [`synDeleteColumn()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_DeleteColumn.md)
  : SubmissionView : delete_column
- [`synDeletePermissions()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_DeletePermissions.md)
  : SubmissionView : delete_permissions
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_GetAcl.md)
  : SubmissionView : get_acl
- [`synGetPermissions()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_GetPermissions.md)
  : SubmissionView : get_permissions
- [`synListAcl()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_ListAcl.md)
  : SubmissionView : list_acl
- [`synQuery()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_Query.md)
  : SubmissionView : query
- [`synQueryPartMask()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_QueryPartMask.md)
  : SubmissionView : query_part_mask
- [`synReorderColumn()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_ReorderColumn.md)
  : SubmissionView : reorder_column
- [`synSetPermissions()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_SetPermissions.md)
  : SubmissionView : set_permissions
- [`synSnapshot()`](https://linglp.github.io/synapser/latest/reference/SubmissionView_Snapshot.md)
  : SubmissionView : snapshot

## Activity

An activity is a Synapse object that helps to keep track of what objects
were used in an analysis step, as well as what objects were generated.

- [`Activity()`](https://linglp.github.io/synapser/latest/reference/Activity.md)
  : Activity
- [`synDisassociateActivityFromEntity()`](https://linglp.github.io/synapser/latest/reference/Activity_DisassociateActivityFromEntity.md)
  : Activity : disassociate_from_entity
- [`synGetFromParent()`](https://linglp.github.io/synapser/latest/reference/Activity_GetFromParent.md)
  : Activity : from_parent
- [`UsedEntity()`](https://linglp.github.io/synapser/latest/reference/UsedEntity.md)
  : UsedEntity
- [`UsedURL()`](https://linglp.github.io/synapser/latest/reference/UsedURL.md)
  : UsedURL

## Team

Represents a [Synapse
Team](https://rest-docs.synapse.org/rest/org/sagebionetworks/repo/model/Team.html).

- [`Team()`](https://linglp.github.io/synapser/latest/reference/Team.md)
  : Team
- [`synCreate()`](https://linglp.github.io/synapser/latest/reference/Team_Create.md)
  : Team : create
- [`synDeleteInvitation()`](https://linglp.github.io/synapser/latest/reference/Team_DeleteInvitation.md)
  : Team : delete_invitation
- [`synGetFromId()`](https://linglp.github.io/synapser/latest/reference/Team_GetFromId.md)
  : Team : from_id
- [`synGetFromName()`](https://linglp.github.io/synapser/latest/reference/Team_GetFromName.md)
  : Team : from_name
- [`synGetOpenInvitations()`](https://linglp.github.io/synapser/latest/reference/Team_GetOpenInvitations.md)
  : Team : open_invitations
- [`synGetTeamMembers()`](https://linglp.github.io/synapser/latest/reference/Team_GetTeamMembers.md)
  : Team : members
- [`synGetUserMembershipStatus()`](https://linglp.github.io/synapser/latest/reference/Team_GetUserMembershipStatus.md)
  : Team : get_user_membership_status
- [`synInviteToTeam()`](https://linglp.github.io/synapser/latest/reference/Team_InviteToTeam.md)
  : Team : invite

## UserProfile

UserProfile represents a user’s profile in the system.

- [`UserProfile()`](https://linglp.github.io/synapser/latest/reference/UserProfile.md)
  : UserProfile
- [`synGetFromId()`](https://linglp.github.io/synapser/latest/reference/UserProfile_GetFromId.md)
  : UserProfile : from_id
- [`synGetFromUsername()`](https://linglp.github.io/synapser/latest/reference/UserProfile_GetFromUsername.md)
  : UserProfile : from_username
- [`synIsCertified()`](https://linglp.github.io/synapser/latest/reference/UserProfile_IsCertified.md)
  : UserProfile : is_certified

## UserPreference

UserPreference represents a user preference in the system.

- [`UserPreference()`](https://linglp.github.io/synapser/latest/reference/UserPreference.md)
  : UserPreference

## Link

A Link entity within Synapse that references another entity.

- [`Link()`](https://linglp.github.io/synapser/latest/reference/Link.md)
  : Link

## Organization

Represents an
[Organization](https://rest-docs.synapse.org/rest/org/sagebionetworks/repo/model/Organization.html).

- [`Organization()`](https://linglp.github.io/synapser/latest/reference/Organization.md)
  : Organization
- [`synGetAcl()`](https://linglp.github.io/synapser/latest/reference/Organization_GetAcl.md)
  : Organization : get_acl
- [`synGetJsonSchemas()`](https://linglp.github.io/synapser/latest/reference/Organization_GetJsonSchemas.md)
  : Organization : get_json_schemas
- [`synUpdateAcl()`](https://linglp.github.io/synapser/latest/reference/Organization_UpdateAcl.md)
  : Organization : update_acl

## JSONSchema

Represents a [JSON
Schema](https://rest-docs.synapse.org/rest/org/sagebionetworks/repo/model/schema/JsonSchemaInfo.html).

- [`JSONSchema()`](https://linglp.github.io/synapser/latest/reference/JSONSchema.md)
  : JSONSchema
- [`synFromUri()`](https://linglp.github.io/synapser/latest/reference/JSONSchema_FromUri.md)
  : JSONSchema : from_uri
- [`synGetBody()`](https://linglp.github.io/synapser/latest/reference/JSONSchema_GetBody.md)
  : JSONSchema : get_body
- [`synGetVersions()`](https://linglp.github.io/synapser/latest/reference/JSONSchema_GetVersions.md)
  : JSONSchema : get_versions

## WikiPage

Represents a [Wiki
Page](https://rest-docs.synapse.org/rest/org/sagebionetworks/repo/model/v2/wiki/V2WikiPage.html).

- [`WikiPage()`](https://linglp.github.io/synapser/latest/reference/WikiPage.md)
  : WikiPage
- [`synCopy()`](https://linglp.github.io/synapser/latest/reference/WikiPage_Copy.md)
  : WikiPage : copy
- [`synGetAttachment()`](https://linglp.github.io/synapser/latest/reference/WikiPage_GetAttachment.md)
  : WikiPage : get_attachment
- [`synGetAttachmentHandles()`](https://linglp.github.io/synapser/latest/reference/WikiPage_GetAttachmentHandles.md)
  : WikiPage : get_attachment_handles
- [`synGetAttachmentPreview()`](https://linglp.github.io/synapser/latest/reference/WikiPage_GetAttachmentPreview.md)
  : WikiPage : get_attachment_preview
- [`synGetMarkdownFile()`](https://linglp.github.io/synapser/latest/reference/WikiPage_GetMarkdownFile.md)
  : WikiPage : get_markdown_file
- [`synReformatAttachmentFileName()`](https://linglp.github.io/synapser/latest/reference/WikiPage_ReformatAttachmentFileName.md)
  : WikiPage : reformat_attachment_file_name
- [`synRestore()`](https://linglp.github.io/synapser/latest/reference/WikiPage_Restore.md)
  : WikiPage : restore
- [`synUnzipGzippedFile()`](https://linglp.github.io/synapser/latest/reference/WikiPage_UnzipGzippedFile.md)
  : WikiPage : unzip_gzipped_file

## WikiOrderHint

A WikiOrderHint contains the order hint for the root wiki that
corresponds to the given owner ID and type.

- [`WikiOrderHint()`](https://linglp.github.io/synapser/latest/reference/WikiOrderHint.md)
  : WikiOrderHint

## WikiHistorySnapshot

A WikiHistorySnapshot contains basic information about an update to a
WikiPage.

- [`WikiHistorySnapshot()`](https://linglp.github.io/synapser/latest/reference/WikiHistorySnapshot.md)
  : WikiHistorySnapshot

## WikiHeader

A WikiHeader contains basic metadata about a WikiPage.

- [`WikiHeader()`](https://linglp.github.io/synapser/latest/reference/WikiHeader.md)
  : WikiHeader

## Download List

Functions for working with the Synapse download list (cart).

- [`DownloadListItem()`](https://linglp.github.io/synapser/latest/reference/DownloadListItem.md)
  : DownloadListItem
- [`synDownloadListAdd()`](https://linglp.github.io/synapser/latest/reference/synDownloadListAdd.md)
  : synDownloadListAdd
- [`synDownloadListRemove()`](https://linglp.github.io/synapser/latest/reference/synDownloadListRemove.md)
  : synDownloadListRemove
- [`synDownloadListClear()`](https://linglp.github.io/synapser/latest/reference/synDownloadListClear.md)
  : synDownloadListClear
- [`synDownloadListManifest()`](https://linglp.github.io/synapser/latest/reference/synDownloadListManifest.md)
  : synDownloadListManifest
- [`synDownloadListFiles()`](https://linglp.github.io/synapser/latest/reference/synDownloadListFiles.md)
  : synDownloadListFiles

## Storage Locations

Storage locations describe where files are uploaded to and downloaded
from via Synapse.

- [`StorageLocation()`](https://linglp.github.io/synapser/latest/reference/StorageLocation.md)
  : StorageLocation
- [`StorageLocationType()`](https://linglp.github.io/synapser/latest/reference/StorageLocationType.md)
  : StorageLocationType
