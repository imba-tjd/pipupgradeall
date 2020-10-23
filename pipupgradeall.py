import pkg_resources, subprocess
def _main():
    subprocess.run(['pip','install','-U',
        *[dist.project_name for dist in pkg_resources.working_set]
    ])
