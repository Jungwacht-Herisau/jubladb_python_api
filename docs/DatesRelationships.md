# DatesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 

## Example

```python
from jubladb_api.models.dates_relationships import DatesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DatesRelationships from a JSON string
dates_relationships_instance = DatesRelationships.from_json(json)
# print the JSON string representation of the object
print(DatesRelationships.to_json())

# convert the object into a dict
dates_relationships_dict = dates_relationships_instance.to_dict()
# create an instance of DatesRelationships from a dict
dates_relationships_from_dict = DatesRelationships.from_dict(dates_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


