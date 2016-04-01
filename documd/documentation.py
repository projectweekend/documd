from collections import defaultdict
import textwrap

route_docs = defaultdict(list)


def register(section):
    def wrapper(resource):
        route_docs[section].append(textwrap.dedent(resource.__doc__))
        return resource
    return wrapper
