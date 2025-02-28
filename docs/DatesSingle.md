# DatesSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DatesResource**](DatesResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.dates_single import DatesSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DatesSingle from a JSON string
dates_single_instance = DatesSingle.from_json(json)
# print the JSON string representation of the object
print(DatesSingle.to_json())

# convert the object into a dict
dates_single_dict = dates_single_instance.to_dict()
# create an instance of DatesSingle from a dict
dates_single_from_dict = DatesSingle.from_dict(dates_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


