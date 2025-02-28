# InvoicesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**recipient** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**invoice_items** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoices_relationships import InvoicesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesRelationships from a JSON string
invoices_relationships_instance = InvoicesRelationships.from_json(json)
# print the JSON string representation of the object
print(InvoicesRelationships.to_json())

# convert the object into a dict
invoices_relationships_dict = invoices_relationships_instance.to_dict()
# create an instance of InvoicesRelationships from a dict
invoices_relationships_from_dict = InvoicesRelationships.from_dict(invoices_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


