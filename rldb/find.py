from .db import entries


def find_one(filter_dict):
    if not filter_dict:
        return entries[0]

    filtered_entries = []
    for entry in entries:
        is_match = True
        for k, v in filter_dict.items():
            if k not in entry or entry[k] != v:
                is_match = False
                break
        if is_match:
            return entry

    return None


def find_all(filter_dict):
    if not filter_dict:
        return entries

    filtered_entries = []
    for entry in entries:
        is_match = True
        for k, v in filter_dict.items():
            if k not in entry or entry[k] != v:
                is_match = False
                break
        if is_match:
            filtered_entries.append(entry)

    return filtered_entries
