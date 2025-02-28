# AdditionalEmailsSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AdditionalEmailsResource**](AdditionalEmailsResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.additional_emails_single import AdditionalEmailsSingle

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalEmailsSingle from a JSON string
additional_emails_single_instance = AdditionalEmailsSingle.from_json(json)
# print the JSON string representation of the object
print(AdditionalEmailsSingle.to_json())

# convert the object into a dict
additional_emails_single_dict = additional_emails_single_instance.to_dict()
# create an instance of AdditionalEmailsSingle from a dict
additional_emails_single_from_dict = AdditionalEmailsSingle.from_dict(additional_emails_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


