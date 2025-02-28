# CoursesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Courses**](Courses.md) |  | [optional] 
**relationships** | [**CoursesRelationships**](CoursesRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.courses_resource import CoursesResource

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesResource from a JSON string
courses_resource_instance = CoursesResource.from_json(json)
# print the JSON string representation of the object
print(CoursesResource.to_json())

# convert the object into a dict
courses_resource_dict = courses_resource_instance.to_dict()
# create an instance of CoursesResource from a dict
courses_resource_from_dict = CoursesResource.from_dict(courses_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


