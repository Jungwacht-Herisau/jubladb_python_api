# AdditionalEmailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AdditionalEmailsResource**](AdditionalEmailsResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.additional_emails_request import AdditionalEmailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalEmailsRequest from a JSON string
additional_emails_request_instance = AdditionalEmailsRequest.from_json(json)
# print the JSON string representation of the object
print(AdditionalEmailsRequest.to_json())

# convert the object into a dict
additional_emails_request_dict = additional_emails_request_instance.to_dict()
# create an instance of AdditionalEmailsRequest from a dict
additional_emails_request_from_dict = AdditionalEmailsRequest.from_dict(additional_emails_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


