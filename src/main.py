import bpy
from copy import deepcopy
from typing import Any, Iterable


class BlenderData:
    __slots__ = ["__entries"]

    def __init__(self):
        self.__entries: dict[str, Any] = {}

    @property
    def entries(self) -> dict[str, Any]:
        return deepcopy(self.__entries)

    def __setitem__(self, key: str, value: Any):
        self.__entries[key] = value


class BlenderObjects(BlenderData):
    def __init__(self, objects: Iterable):
        super().__init__()
        self.__add_object_entries(objects)

    def __add_object_entries(self, objects: Iterable):
        for obj in objects:
            entry: dict[str, Any] = self.create_object_entry(obj)
            self[obj.name] = entry

    def create_object_entry(self, obj: bpy.types.Object) -> dict[str, Any]:
        return {
            "type": obj.type,
            "data": obj.data.name,  # Can be used to point to the right data depending on object type
            "modifiers": [],
            "materials": []
        }


def blender_data_to_dict() -> dict[str, Any]:
    objects: BlenderObjects = BlenderObjects(bpy.data.objects)
    return {
        "objects": objects.entries
    }


if __name__ == "__main__":
    data: dict[str, Any] = blender_data_to_dict()
    print(data)
