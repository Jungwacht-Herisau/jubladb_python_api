# DatesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Dates**](Dates.md) |  | [optional] 
**relationships** | [**DatesRelationships**](DatesRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.dates_resource import DatesResource

# TODO update the JSON string below
json = "{}"
# create an instance of DatesResource from a JSON string
dates_resource_instance = DatesResource.from_json(json)
# print the JSON string representation of the object
print(DatesResource.to_json())

# convert the object into a dict
dates_resource_dict = dates_resource_instance.to_dict()
# create an instance of DatesResource from a dict
dates_resource_from_dict = DatesResource.from_dict(dates_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


