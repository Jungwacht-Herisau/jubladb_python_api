# InvoicesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Invoices**](Invoices.md) |  | [optional] 
**relationships** | [**InvoicesRelationships**](InvoicesRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoices_resource import InvoicesResource

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesResource from a JSON string
invoices_resource_instance = InvoicesResource.from_json(json)
# print the JSON string representation of the object
print(InvoicesResource.to_json())

# convert the object into a dict
invoices_resource_dict = invoices_resource_instance.to_dict()
# create an instance of InvoicesResource from a dict
invoices_resource_from_dict = InvoicesResource.from_dict(invoices_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


