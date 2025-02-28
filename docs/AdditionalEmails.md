# AdditionalEmails

Additional email attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**contactable_id** | **int** |  | [optional] 
**contactable_type** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from jubladb_api.models.additional_emails import AdditionalEmails

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalEmails from a JSON string
additional_emails_instance = AdditionalEmails.from_json(json)
# print the JSON string representation of the object
print(AdditionalEmails.to_json())

# convert the object into a dict
additional_emails_dict = additional_emails_instance.to_dict()
# create an instance of AdditionalEmails from a dict
additional_emails_from_dict = AdditionalEmails.from_dict(additional_emails_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


