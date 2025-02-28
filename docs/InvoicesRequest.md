# InvoicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InvoicesResource**](InvoicesResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoices_request import InvoicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesRequest from a JSON string
invoices_request_instance = InvoicesRequest.from_json(json)
# print the JSON string representation of the object
print(InvoicesRequest.to_json())

# convert the object into a dict
invoices_request_dict = invoices_request_instance.to_dict()
# create an instance of InvoicesRequest from a dict
invoices_request_from_dict = InvoicesRequest.from_dict(invoices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


