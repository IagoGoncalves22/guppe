"""

.....................

# print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')

print(list(metadados_pip))

print(metadados_pip['Project-URL'])


.....................

.....................

.....................

.....................

.....................

.....................

"""


from importlib import metadata

# print(len(metadata.files('pip')))

# print(metadata.requires('pip'))

print(metadata.requires('django'))
