import re


def detect_relationships(sentence):

    relations = []

    subset_pattern = r"(.+?) is a subset of (.+)"
    usage_pattern = r"(.+?) is used in (.+)"

    subset = re.search(subset_pattern, sentence)

    if subset:

        relations.append({

            "type": "subset",
            "source": subset.group(1),
            "target": subset.group(2)
        })

    usage = re.search(usage_pattern, sentence)

    if usage:

        relations.append({

            "type": "usage",
            "source": usage.group(1),
            "target": usage.group(2)
        })

    return relations
