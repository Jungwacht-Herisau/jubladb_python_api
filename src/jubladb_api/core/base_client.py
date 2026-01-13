import abc
import dataclasses
import itertools

import requests

import jubladb_api.metamodel
from jubladb_api.core import base_entity


class BaseClient(abc.ABC):
    def __init__(self,
                 url: str,
                 headers: dict[str, str]|None=None,):
        if url.endswith("/"):
            raise ValueError("URL must not end with a slash, use the format https://db.example.ch")
        self._url = url
        self._headers = headers or {}
        self._cache: dict[jubladb_api.metamodel.EntityName, dict[int, object]] = {}

    def _request_list(self,
                      type_: jubladb_api.metamodel.EntityName,
                      sort: list[str]|None=None,
                      include: list[str]|None=None,
                      filters: list[tuple[str, str, object]]|None=None):
        meta_type = jubladb_api.metamodel.ENTITIES[type_]
        if meta_type.url == "":
            raise ValueError(f"Entity {type_} has no url defined")
        params = []
        if sort:
            params.append(("sort", ",".join(s[:-len("_asc")] if s.endswith("_asc") else "-"+s[:-len("_desc")] for s in sort)))
        if include:
            params.append(("include", ",".join(include)))
        for ((field_name, filter_type), fis) in itertools.groupby(filters or [], lambda x: (x[0], x[1])):
            param_name = f"filter[{field_name}][{filter_type}]"
            param_value = ",".join(str(fi[2]) for fi in fis)
            params.append((param_name, param_value))

        return self._request_get(f"{self._url}{meta_type.url}", params)

    def _request_single_get(self,
                            type_: jubladb_api.metamodel.EntityName,
                            id_: int,
                            include: list[str]|None=None):
        meta_type = jubladb_api.metamodel.ENTITIES[type_]
        if meta_type.url == "":
            raise ValueError(f"Entity {type_} has no url defined")
        params = []
        if include:
            params.append(("include", ",".join(include)))
        return self._request_get(f"{self._url}{meta_type.url}/{id_}", params)

    def _request_get(self,
                     url: str,
                     params: list[tuple[str, str]]) -> dict:
        effective_headers = self._headers.copy()
        effective_headers["Accept"] = "application/vnd.api+json"
        res = requests.get(url=url,
                           params=params,
                           headers=effective_headers,
                           )
        return res.json()

    def _cache_add(self, entity: base_entity.BaseEntity) -> None:
        entity_key = entity.key
        self._cache.setdefault(entity_key.type, {})[entity_key.id] = entity

    def _cache_get(self, entity_key: base_entity.BaseEntityKey) -> base_entity.BaseEntity | None:
        return self._cache.get(entity_key.type, {}).get(entity_key.id)
