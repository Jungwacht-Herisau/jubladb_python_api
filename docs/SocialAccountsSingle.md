# SocialAccountsSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SocialAccountsResource**](SocialAccountsResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.social_accounts_single import SocialAccountsSingle

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAccountsSingle from a JSON string
social_accounts_single_instance = SocialAccountsSingle.from_json(json)
# print the JSON string representation of the object
print(SocialAccountsSingle.to_json())

# convert the object into a dict
social_accounts_single_dict = social_accounts_single_instance.to_dict()
# create an instance of SocialAccountsSingle from a dict
social_accounts_single_from_dict = SocialAccountsSingle.from_dict(social_accounts_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


