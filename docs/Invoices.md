# Invoices

Invoice attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**group_id** | **int** |  | [optional] 
**recipient_id** | **int** |  | [optional] 
**due_at** | **date** |  | [optional] 
**issued_at** | **date** |  | [optional] 
**recipient_email** | **str** |  | [optional] 
**payment_information** | **str** |  | [optional] 
**payment_purpose** | **str** |  | [optional] 
**hide_total** | **bool** |  | [optional] 

## Example

```python
from jubladb_api.models.invoices import Invoices

# TODO update the JSON string below
json = "{}"
# create an instance of Invoices from a JSON string
invoices_instance = Invoices.from_json(json)
# print the JSON string representation of the object
print(Invoices.to_json())

# convert the object into a dict
invoices_dict = invoices_instance.to_dict()
# create an instance of Invoices from a dict
invoices_from_dict = Invoices.from_dict(invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


