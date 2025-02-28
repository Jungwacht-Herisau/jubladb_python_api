# PeopleResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**People**](People.md) |  | [optional] 
**relationships** | [**PeopleRelationships**](PeopleRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.people_resource import PeopleResource

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleResource from a JSON string
people_resource_instance = PeopleResource.from_json(json)
# print the JSON string representation of the object
print(PeopleResource.to_json())

# convert the object into a dict
people_resource_dict = people_resource_instance.to_dict()
# create an instance of PeopleResource from a dict
people_resource_from_dict = PeopleResource.from_dict(people_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


