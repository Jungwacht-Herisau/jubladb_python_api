# PhoneNumbersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PhoneNumbersResource**](PhoneNumbersResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.phone_numbers_request import PhoneNumbersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumbersRequest from a JSON string
phone_numbers_request_instance = PhoneNumbersRequest.from_json(json)
# print the JSON string representation of the object
print(PhoneNumbersRequest.to_json())

# convert the object into a dict
phone_numbers_request_dict = phone_numbers_request_instance.to_dict()
# create an instance of PhoneNumbersRequest from a dict
phone_numbers_request_from_dict = PhoneNumbersRequest.from_dict(phone_numbers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


