# JsonapiSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**JsonapiData**](JsonapiData.md) |  | 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_success import JsonapiSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiSuccess from a JSON string
jsonapi_success_instance = JsonapiSuccess.from_json(json)
# print the JSON string representation of the object
print(JsonapiSuccess.to_json())

# convert the object into a dict
jsonapi_success_dict = jsonapi_success_instance.to_dict()
# create an instance of JsonapiSuccess from a dict
jsonapi_success_from_dict = JsonapiSuccess.from_dict(jsonapi_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


