# AdditionalEmailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**AdditionalEmails**](AdditionalEmails.md) |  | [optional] 
**relationships** | **object** | Members of the relationships object (\&quot;relationships\&quot;) represent references from the resource object in which it&#39;s defined to other resource objects. | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.additional_emails_resource import AdditionalEmailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalEmailsResource from a JSON string
additional_emails_resource_instance = AdditionalEmailsResource.from_json(json)
# print the JSON string representation of the object
print(AdditionalEmailsResource.to_json())

# convert the object into a dict
additional_emails_resource_dict = additional_emails_resource_instance.to_dict()
# create an instance of AdditionalEmailsResource from a dict
additional_emails_resource_from_dict = AdditionalEmailsResource.from_dict(additional_emails_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


