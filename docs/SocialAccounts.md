# SocialAccounts

Social account attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**contactable_id** | **int** |  | [optional] 
**contactable_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from jubladb_api.models.social_accounts import SocialAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAccounts from a JSON string
social_accounts_instance = SocialAccounts.from_json(json)
# print the JSON string representation of the object
print(SocialAccounts.to_json())

# convert the object into a dict
social_accounts_dict = social_accounts_instance.to_dict()
# create an instance of SocialAccounts from a dict
social_accounts_from_dict = SocialAccounts.from_dict(social_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


