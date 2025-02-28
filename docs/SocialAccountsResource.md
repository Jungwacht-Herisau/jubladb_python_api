# SocialAccountsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**SocialAccounts**](SocialAccounts.md) |  | [optional] 
**relationships** | **object** | Members of the relationships object (\&quot;relationships\&quot;) represent references from the resource object in which it&#39;s defined to other resource objects. | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.social_accounts_resource import SocialAccountsResource

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAccountsResource from a JSON string
social_accounts_resource_instance = SocialAccountsResource.from_json(json)
# print the JSON string representation of the object
print(SocialAccountsResource.to_json())

# convert the object into a dict
social_accounts_resource_dict = social_accounts_resource_instance.to_dict()
# create an instance of SocialAccountsResource from a dict
social_accounts_resource_from_dict = SocialAccountsResource.from_dict(social_accounts_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


