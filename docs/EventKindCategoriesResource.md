# EventKindCategoriesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**EventKindCategories**](EventKindCategories.md) |  | [optional] 
**relationships** | **object** | Members of the relationships object (\&quot;relationships\&quot;) represent references from the resource object in which it&#39;s defined to other resource objects. | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kind_categories_resource import EventKindCategoriesResource

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindCategoriesResource from a JSON string
event_kind_categories_resource_instance = EventKindCategoriesResource.from_json(json)
# print the JSON string representation of the object
print(EventKindCategoriesResource.to_json())

# convert the object into a dict
event_kind_categories_resource_dict = event_kind_categories_resource_instance.to_dict()
# create an instance of EventKindCategoriesResource from a dict
event_kind_categories_resource_from_dict = EventKindCategoriesResource.from_dict(event_kind_categories_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


