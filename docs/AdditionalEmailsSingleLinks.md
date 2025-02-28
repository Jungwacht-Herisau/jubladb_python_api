# AdditionalEmailsSingleLinks

Link members related to the primary data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 
**last** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 
**prev** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 
**next** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.additional_emails_single_links import AdditionalEmailsSingleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalEmailsSingleLinks from a JSON string
additional_emails_single_links_instance = AdditionalEmailsSingleLinks.from_json(json)
# print the JSON string representation of the object
print(AdditionalEmailsSingleLinks.to_json())

# convert the object into a dict
additional_emails_single_links_dict = additional_emails_single_links_instance.to_dict()
# create an instance of AdditionalEmailsSingleLinks from a dict
additional_emails_single_links_from_dict = AdditionalEmailsSingleLinks.from_dict(additional_emails_single_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


