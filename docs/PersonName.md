# PersonName

Name attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] [readonly] 
**last_name** | **str** |  | [optional] [readonly] 

## Example

```python
from jubladb_api.models.person_name import PersonName

# TODO update the JSON string below
json = "{}"
# create an instance of PersonName from a JSON string
person_name_instance = PersonName.from_json(json)
# print the JSON string representation of the object
print(PersonName.to_json())

# convert the object into a dict
person_name_dict = person_name_instance.to_dict()
# create an instance of PersonName from a dict
person_name_from_dict = PersonName.from_dict(person_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


