# PhoneNumbers

Phone number attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**contactable_id** | **int** |  | [optional] 
**contactable_type** | **str** |  | [optional] 
**number** | **str** |  | [optional] 

## Example

```python
from jubladb_api.models.phone_numbers import PhoneNumbers

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumbers from a JSON string
phone_numbers_instance = PhoneNumbers.from_json(json)
# print the JSON string representation of the object
print(PhoneNumbers.to_json())

# convert the object into a dict
phone_numbers_dict = phone_numbers_instance.to_dict()
# create an instance of PhoneNumbers from a dict
phone_numbers_from_dict = PhoneNumbers.from_dict(phone_numbers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


