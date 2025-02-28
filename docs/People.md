# People

Person attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**town** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**primary_group_id** | **int** |  | [optional] [readonly] 
**gender** | **str** |  | [optional] 
**birthday** | **date** |  | [optional] 
**language** | **str** |  | [optional] 

## Example

```python
from jubladb_api.models.people import People

# TODO update the JSON string below
json = "{}"
# create an instance of People from a JSON string
people_instance = People.from_json(json)
# print the JSON string representation of the object
print(People.to_json())

# convert the object into a dict
people_dict = people_instance.to_dict()
# create an instance of People from a dict
people_from_dict = People.from_dict(people_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


