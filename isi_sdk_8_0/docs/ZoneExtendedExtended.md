# ZoneExtendedExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_system_provider** | **str** | Specifies an alternate system provider. | [optional] 
**auth_providers** | **list[str]** | Specifies the list of authentication providers available on this access zone. | [optional] 
**cache_entry_expiry** | **int** | Specifies amount of time in seconds to cache a user/group. | [optional] 
**create_path** | **bool** | Determines if a path is created when a path does not exist. | [optional] 
**groupnet** | **str** | Groupnet identitier | [optional] 
**home_directory_umask** | **int** | Specifies the permissions set on automatically created user home directories. | [optional] 
**id** | **str** | Specifies the system-assigned ID for the access zone. This value is returned when an access zone is created through the POST method | [optional] 
**ifs_restricted** | [**list[GroupMember]**](GroupMember.md) | Specifies a list of users and groups that have read and write access to /ifs. | [optional] 
**map_untrusted** | **str** | Maps untrusted domains to this NetBIOS domain during authentication. | [optional] 
**name** | **str** | Specifies the access zone name. | [optional] 
**netbios_name** | **str** | Specifies the NetBIOS name. | [optional] 
**path** | **str** | Specifies the access zone base directory path. | [optional] 
**skeleton_directory** | **str** | Specifies the skeleton directory that is used for user home directories. | [optional] 
**system** | **bool** | True if the access zone is built-in. | [optional] 
**system_provider** | **str** | Specifies the system provider for the access zone. | [optional] 
**user_mapping_rules** | **list[str]** | Specifies the current ID mapping rules. | [optional] 
**zone_id** | **int** | Specifies the access zone ID on the system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


