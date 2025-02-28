# PhoneNumbersResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**PhoneNumbers**](PhoneNumbers.md) |  | [optional] 
**relationships** | **object** | Members of the relationships object (\&quot;relationships\&quot;) represent references from the resource object in which it&#39;s defined to other resource objects. | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.phone_numbers_resource import PhoneNumbersResource

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumbersResource from a JSON string
phone_numbers_resource_instance = PhoneNumbersResource.from_json(json)
# print the JSON string representation of the object
print(PhoneNumbersResource.to_json())

# convert the object into a dict
phone_numbers_resource_dict = phone_numbers_resource_instance.to_dict()
# create an instance of PhoneNumbersResource from a dict
phone_numbers_resource_from_dict = PhoneNumbersResource.from_dict(phone_numbers_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


