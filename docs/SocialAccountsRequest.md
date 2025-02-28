# SocialAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SocialAccountsResource**](SocialAccountsResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.social_accounts_request import SocialAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAccountsRequest from a JSON string
social_accounts_request_instance = SocialAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(SocialAccountsRequest.to_json())

# convert the object into a dict
social_accounts_request_dict = social_accounts_request_instance.to_dict()
# create an instance of SocialAccountsRequest from a dict
social_accounts_request_from_dict = SocialAccountsRequest.from_dict(social_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


