from .db import entries


def find_one(filter_dict):
    if not filter_dict:
        return entries[0]

    filtered_entries = []
    for entry in entries:
        for k, v in filter_dict.items():
            if k in entry and entry[k] == v:
                return entry

    return None


def find_all(filter_dict):
    if not filter_dict:
        return entries

    filtered_entries = []
    for entry in entries:
        for k, v in filter_dict.items():
            if k in entry and entry[k] == v:
                filtered_entries.append(entry)

    return filtered_entries
