import pkg_resources

installed_packages = pkg_resources.working_set
sorted_packages = sorted([f'{i.key}=={i.version}' for i in installed_packages])
print(sorted_packages)
